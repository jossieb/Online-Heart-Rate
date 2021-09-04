############################################################################################
# Python JossieB's Heart Rate Monitor
# End project for the Harvard CS50X course
# By:   Jos van der Have
# Date: summer 2021
# Special kudoos for: Harvard for briljant lecture and Adafruit for their work on HR sensors
############################################################################################
import os
import sys
import sqlite3
import logging
from flask import Flask, flash, redirect, render_template, request, session, g, jsonify
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import json
import datetime
import time
# The adafruit modules handles the working with the HR sensor
import adafruit_ble
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_ble_heart_rate import HeartRateService

from helpers import apology, login_required

# PyLint can't find BLERadio for some reason so special case it here.
ble = adafruit_ble.BLERadio()  # pylint: disable=no-member

# Configure application
app = Flask(__name__)

# configure logging level
logging.basicConfig(level=logging.DEBUG)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure SQLite database
con = sqlite3.connect("monitor.db", check_same_thread=False) 
print ("Opened database successfully")


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/connect", methods=["GET", "POST"])
def connect():
    print(request.method)
    conntext = []
    if request.method == "POST":
        hr_connection = None

        while True:
            # Scanning
            for adv in ble.start_scan(ProvideServicesAdvertisement, timeout=5):
                if HeartRateService in adv.services:
                    conntext.append("found a HeartRateService advertisement")
                    hr_connection = ble.connect(adv)
                    break

            # Stop scanning whether or not we are connected.
            ble.stop_scan()

            if hr_connection and hr_connection.connected:
                # There is a connection with the sensor
                if DeviceInfoService in hr_connection:
                    dis = hr_connection[DeviceInfoService]
                    try:
                        manufacturer = dis.manufacturer
                    except AttributeError:
                        manufacturer = "(Manufacturer Not specified)"
                    try:
                        model_number = dis.model_number
                    except AttributeError:
                        model_number = "(Model number not specified)"
                    text = ("Device:", manufacturer, model_number)
                    conntext.append(text)

                else:
                    print("No device information")
            
                hr_service = hr_connection[HeartRateService]
                text = ("Location:", hr_service.location)
                conntext.append(text)
                #Keep adding values to the database

                while hr_connection.connected:
                    values = hr_service.measurement_values
                    print("3: " + str(values))  # returns the full heart_rate data set
                    if values != None:
                        # generate timestamp
                        datetm = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
                        bpm = (values.heart_rate)
                        rri = (values.rr_intervals)
                        con.execute(
                            "INSERT INTO heart_rates (rate, timestamp, intervals) VALUES (?, ?, ?)",
                            (            
                            str(bpm),
                            str(datetm),
                            str(rri)
                            )
                        ) 
                        con.commit()
                        #print("Added BPM: " +  str(bpm)  +  "  timestamp: " +  str(datetm) + " interval: " + str(rri))
                    time.sleep(1)

                return render_template("connect.html", conntext=conntext)
    else:
        return render_template("connect.html", conntext=conntext)


@app.route("/monitor", methods=["GET", "POST"])
def monitor():

    while True:

        rates = []
        tsts = []
        # retrieve latest 60 records form table to show in chart
        data = con.execute(
        "SELECT rate, timestamp FROM heart_rates order by timestamp DESC LIMIT 60"
                )
        x = 1
        for row in data:
            if x == 1:
                rate = row[0]
                x = x + 1
            rates.append(row[0])
            tsts.append(row[1])

        return render_template("monitor.html", rate = rate, rates=rates, tsts=tsts)
        con.close()
        time.sleep(1)


@app.route("/design")
def design():

    return render_template("design.html")


@app.route("/specs")
def specs():

    return render_template("specs.html")


@app.route("/test", methods=["GET", "POST"])
def test():
    """Test de database"""
    # User reached route via POST (as by submitting a form via POST)

    if request.method == "POST":
         # Ensure rate was submitted
        if not request.form.get("rate"):
            return apology("Provide rate", 400)
        rate = request.form.get("rate")
        if rate.isdigit() == False:
            return apology("must provide number for rate", 400)

        # generate timestamp
        datetm = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

        con.execute(
            "INSERT INTO heart_rates (rate, timestamp) VALUES (?, ?)",
            (            
            request.form.get("rate"),
            str(datetm)
            )
        ) 
        con.commit()
        
        """Show fresh rates"""
        rate = request.form.get("rate")
        rates = con.execute(
            "SELECT * FROM heart_rates order by timestamp DESC"
            )
        return render_template("test.html", rate=rate, rates=rates)
        con.close() 

    else:
        """Show rates"""
        rates = con.execute(
            "SELECT * FROM heart_rates order by timestamp DESC"
            )
        rate = 69
        return render_template("test.html", rate=rate, rates=rates)
        con.close()


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

# Project Title: ONLINE HEART RATE MONITOR

## ABOUT THE ONLINE HEART RATE MONITOR
The <b>Online Heart Rate Monitor</b> has been realised as part of my online Harvard CS50X course.
    I started that cource because I was recovering from a heart attack and had lots of spare time.
    Besides that I was looking for a training that could help me starting with Flask.
    During the course I learned that at the end there was a final project to showcase your skills.
    So I tried to combine the one and the other...</p>
    <p>After a heart attack you become aware of the importance of the motor that drives you; your <b><span class="w3-text-red">HEART</b></span>! During sporting I sometimes use a heart rate sensor so I came up with the idea of monitoring my heart rate with the help of a full stack website.</p>
    <p>Also... this kind of functionality becomes more and more main stream. Companies like <a href="https://www.zwift.com/eu" target="_blank">Zwift</a> (virtual sporting), use all kind of sensors to feed the virtual environment.</p>

## DESIGN OF THE ONLINE HEART RATE MONITOR
<p><b>Visual design</b></p>
        <img src="static/hrm.jpg" style="width:600px;border: 2px solid #555;">
        <br>
<p><b>Textual design</b></p>
<b>1)</b> To measure my heart rate I use a chest band sensor from ‘XAND’.  This sensor is able to use both Bluetooth and ANT.
        In my case I use the Bluetooth protocol to gather the measured heart rate data.
        <br><br>
        <b>2)</b> Since my laptop doesn’t support Bluetooth I use a cheap dongle to receive the data over Bluetooth on my laptop.
        <br><br>
        <b>3)</b> On my laptop a Flask application is running. This application supports a couple of routes:
        <br>
        - <i>Home;</i> a short description on the background of the application<br>
        - <i>Connect;</i> makes a connection between the application and the sensor. Kudo’s for Adafruit for sharing the Python code to do this. The app is notified if the connection has been made. Once the connection is there the sensor data is received and stored in a sqlite database.<br>
        - <i>Monitor;</i> displays in a streaming mode the received heart rate data together with a chart displaying the last 60 heart rates received in the database.<br>
        - <i>Design;</i> a more functional description about the design of the application.<br>
        - <i>Specs;</i> a more technical description about the components used.<br>
        - <i>Test;</i> where you can manually add a heart rate to the database table heart_rates.
        <br>
        <p><b>Screen shot of the monitoring tab</b></p>
        <img src="static/jb_monitor.jpg" style="width:600px;border: 2px solid #555;">
        <br>
        <br>
        <b>4)</b> Since the application is using a local webserver the front-end can be reached through the browser at URL http://127.0.0.1:50000
        <p><b>Running local</b></p>
        <img src="static/flask_run.jpg" style="width:600px;border: 2px solid #555;">
        <br>
        <b>5)</b> To use the monitor functionality you must first connect the application to the sensor and then choose monitor.
        <br><br>
        <b>6)</b> <b>To do</b>: since this is the MVP version of the application there is still a wish list of functionality like:<br>
        a.	seamlessly refresh the data instead of the complete page refresh<br>
        b.	change the colors of the rate and data points based on heart rate<br>
        c.	activate alert based on high measured heart rate<br>
        d.	activate/deactivate monitor button/tab based on connection<br>
        e.	be able to drop the connection with the sensor<br>
        f.  improve the front end to better adapt to multiple devices<br>
        g.  make app available within my local network<br>
        h.  give more feedback about the connection made
    </p>

## SPECS OF THE ONLINE HEART RATE MONITOR
The MVC application consists of the following components:<br><br>
        <b>1)	Python app (<i>app.py</i>) as Controller</b><br>
        Main modules that are used within the Python application are:<br>
        a.	<b>Flask</b>; A full stack microframework for Python.<br>
        b.	<b>Adafrui</b>t BLE; Adafruit shared the code for BLE (Bluetooth Low Energy) functionality.<br>
        c.	<b>Sqlite3</b>; the most used database engine in the world (according to sqlite).<br>
        d.  <b>helpers.py</b>; mainly for error handling<br>
        <br>
        <p><b>Code for connecting to the sensor and storing the rates in the database</b></p>
        <img src="static/code_connect1.jpg" style="width:600px;border: 2px solid #555;">
        <br>
        <img src="static/code_connect2.jpg" style="width:600px;border: 2px solid #555;">
        <br>
        <b>2)	HTML files (<i>layout, index, connect, monitor, design, specs, test, apology</i>) as View</b><br>
        The front end is using Javascript and Javascript libraries to deliver a nice UX:<br>
        a.	<b>jQuery</b>; to simplify the HTML handling<br>
        b.	<b>Chart.js</b>; to create a nice graphic chart with heart rates<br><br>
        Front end also uses:<br>
        a.	<b>CSS</b>; to control the layout of the web pages<br>
        b.	<b>Bootstrap</b>; as HTML, CSS, and JavaScript framework<br>
        <br>
        <b>3)	Database (<i>monitor.db</i>) as Model</b><br>
        The database consists of only one file heart_rates to hold the received heart rates.<br>
        <img src="static/monitordb.jpg" style="width:600px;border: 2px solid #555;">
    </p>

## KUDO'S GO TO:
<p> - Harvard CS50X for there great free offer of this course<br>
    - David and Brian for there great lecture<br>
    - Adafruit for sharing there BLE code<br>
    - Python community for all the great content that is out there<br>
    - Other communities for other great content that got me to a working app<br>
    - Community around the great IDE Visual Studio Code
</p>

## ABOUT ME
<p><b>Author:  </b> Jos van der Have</p>
    <p><b>City:    </b> Vlaardingen</p>
    <p><b>Country: </b> The Netherlands</p>
    <p><b>e-mail:  </b> jvdhnl@hotmail.com</p>
    <p><b>on Git:  </b> https://github.com/jossieb</p>

#### VIDEO DEMO:  https://youtu.be/ZIPBLPZ-mKs

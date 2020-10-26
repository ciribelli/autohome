
<h3>About Autohome:</h3>
Project Autohome aims to provide a set of modules to acquire, storage, analyse and make ajust suggestion to conciliate home ambient confort and energy comsumption. It basically uses a <b>raspberry pi</b> with components combined to <b>python AI</b> tools. A <b>Webapp</b> supplies interaction to user commands and feedback insights.

<h4>Web app</h4>
<p>To provide a user interface with temperature and humidity trends information for n ambients. Also to collect user feedback and classification data to improve ML classifiers.</p>

<h4>motorHome.py</h4>
Temperature and Humidity data aquisition is made every each minute in motorHome.py. Information is stored in sql database provided by Django server.

<h4>motorIA.py</h4>
Classification routine is made every each minute in motorIA.py. It raises the MLPClassifier available in svm_model.pkl file. This feature is still being developed.



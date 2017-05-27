# ue4-socketio-crash
Test project for demonstrating crash on SocketIO in UnrealEngine 4.15.2 using Flask-SocketIO.

# Requirements
* Python 2.7
* (Windows only) Install the VC++ compiler for Python 2.7 (http://www.microsoft.com/en-us/download/details.aspx?id=44266)

# Install instructions

1. Download PyCharm (https://www.jetbrains.com/pycharm/download/) - Community Edition is sufficient
1. Open this repository
1. Set interpreter to Python2.7

    1. Go to "File" -> "Settings"
    1. Search for "Interpreter"
    1. Set to Python 2.7

1. Open ue-crash-dummy.py
1. PyCharm should now display that some requirements are missing -> click "Install requirements"

# Steps to reproduce
1. In UnrealEngine 4 create a SocketIO client

    1. Connect to Address and Port: ws://localhost:5000

1. Emit the following event: testEvent

    1. UnrealEngine should crash

1. Restart UnrealEngine
1. Emit the following event: testEventWithException

    1. In this event I raise an Exception within the event in Python. This (at least that's what I guess) causes the server to not return anything
    1. UnrealEngine should not crash

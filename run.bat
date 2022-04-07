@echo on
echo starting...
python -m pip install paho-mqtt pymongo dnspython
echo running
python server_sub.py

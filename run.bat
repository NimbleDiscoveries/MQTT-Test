@echo on
echo starting...
python -m pip install paho-mqtt pymongo
echo running
python server_sub.py

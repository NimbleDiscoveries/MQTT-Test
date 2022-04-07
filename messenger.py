import pymongo
from time import sleep
class cli():
  #client = pymongo.MongoClient("mongodb+srv://esp-th:Blazer1@mqtt-test.nl8qr.mongodb.net/mqtt-test?retryWrites=true&w=majority")
  #db = client.test
  def __init__(self):
    sleep(20)
    print('10 more sec')
    sleep(10)
    self.client = pymongo.MongoClient("mongodb+srv://esp-th:Blazer1@mqtt-test.nl8qr.mongodb.net/mqtt-test?retryWrites=true&w=majority")
    self.db = self.client.test
    print("setting up pymongo...")
  def msg_send(self,msg,type='t'):
    if type=='t':
      self.db.esp.insert_one({'temp':msg})
    elif type=='h':
      self.db.esp.insert_one({'humid':msg})
    

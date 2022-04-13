import pymongo
from time import sleep
import os
class cli():
  def __init__(self):
    sleep(20)
    print('10 more sec')
    sleep(10)
    self.client = pymongo.MongoClient(f"mongodb+srv://{os.environ['USER_MONGODB']}:{os.environ['PASSWORD_MONGODB']}@esp-test.nl8qr.mongodb.net/esp-test?retryWrites=true&w=majority")
    self.db = self.client.testing
    print("setting up pymongo...")
  def msg_send(self,msg,type='t'):
    if type=='t':
      self.db.esp.insert_one({'temp':msg})
    elif type=='h':
      self.db.esp.insert_one({'humid':msg})
    

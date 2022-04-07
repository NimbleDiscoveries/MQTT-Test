import pymongo

class cli():
  client = pymongo.MongoClient("mongodb+srv://esp-th:Blazer1@mqtt-test.nl8qr.mongodb.net/mqtt-test?retryWrites=true&w=majority")
  db = client.test
  def msg_send(self,msg,type='t'):
    if type=='t':
      self.db.esp.insert_one({'temp':msg})
    elif type=='h':
      self.db.esp.insert_one({'humid':msg})
  def __init__(self):
    print('hit enter')
    input()
    self.client = pymongo.MongoClient("mongodb+srv://esp-th:Blazer1@mqtt-test.nl8qr.mongodb.net/mqtt-test?retryWrites=true&w=majority")
    self.db = self.client.test
    print("setting up pymongo...")

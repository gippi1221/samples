import pymongo

class MongoDBService:

  def __init__(self, db_url, db_name):
    self.client = pymongo.MongoClient(db_url)
    self.db = self.client[db_name]

  def close_connection(self):
    self.client.close()
  
  def insert_document(self, document):
    self.db.jokes.insert_one(document)

import pymongo
import os

class mongodb_connect():
    def __init__(self):
        self.dbhost = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
        self.dbpw = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
        self.client = pymongo.MongoClient(f"mongodb://{self.dbhost}:{self.dbpw}@localhost:27017")
        self.dblist = self.client.list_database_names()
    
    def insert_doc(self,dbname,docname,dict_insert):
        mydb = self.client[dbname]
        mycol = mydb[docname]

        value = mycol.insert_one(dict_insert)
        print(value.inserted_id)
    
    def insert_many_doc(self,dbname,docname,dict_insert):
        mydb = self.client[dbname]
        mycol = mydb[docname]

        x = mycol.insert_many(dict_insert)
        print(x.inserted_ids)

    @property
    def get_db(self):
        return self.dblist

if __name__ == "__main__":
    db = mongodb_connect()
    mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
    db.insert_many_doc("runoobdb","sites",mylist)
    

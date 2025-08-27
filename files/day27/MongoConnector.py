from pymongo import MongoClient

class MongoConnectManager:
    def __init__(self, hostname="localhost", port=27017, db_name="", collection_name=""):
        self.hostname = hostname
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name
        # placeholders
        self.client = None
        self.mongo_db = None
        self.collection = None    

    def __enter__(self):
        self.client = MongoClient(self.hostname, self.port)
        self.mongo_db = MongoClient(self.hostname, self.port)[self.db_name]
        self.collection = MongoClient(self.hostname, self.port)[self.db_name][self.collection_name]
        return self.client

    # def getDatabase(self):
    #     return self.mongo_db

    # def getCollection(self):
    #     return self.collection
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()
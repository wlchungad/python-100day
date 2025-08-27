from FileManager import FileManager

with FileManager('./test.txt', 'w') as f:
    f.write('Test')
print(f.closed)

from MongoConnector import *

with MongoConnectManager('localhost', 27017, 'iot_device_data', 'sensor_data') as mongo:
    try:
        db = mongo.mongo_db
        collection = db.collection
        print(type(db))
        print(type(collection))
    except Exception as e:
        print(e)
import motor.motor_asyncio

class MongoDb():

    _client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")

    def getDb(self):
        return self._client.products
        

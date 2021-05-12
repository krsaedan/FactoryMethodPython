from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint = "endpoint"
key = 'keyinbase64'

client = CosmosClient(endpoint, key)

database_name = 'products'
database = client.create_database_if_not_exists(id=database_name)

container_name = 'products'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/products"),
    offer_throughput=400
)
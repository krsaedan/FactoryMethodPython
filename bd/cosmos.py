from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint = "https://cosmosdb-krsaedan.documents.azure.com:443/"
key = 'j7Lzfp8iSxb1mHcHVdEkS6sL7y7jZxNHzY2Myzmu6AlEr98YAho3vXuok4asUWb1maSCtVWFYZ6MM5ppdaJFKg=='

client = CosmosClient(endpoint, key)

database_name = 'products'
database = client.create_database_if_not_exists(id=database_name)

container_name = 'products'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/products"),
    offer_throughput=400
)
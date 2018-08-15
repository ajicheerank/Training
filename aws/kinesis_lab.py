import boto3 as bt
import json
import time as t

session=bt.Session(profile_name="default")
cli_ken = session.client("kinesis")

def create_stream(name,shards):
    res_create_stream = cli_ken.create_stream(StreamName=name, ShardCount = shards)
    return res_create_stream

def describe_stream(stream_name):
    res_desc_stream = cli_ken.describe_stream(StreamName=stream_name)
    return res_desc_stream

def list_stream(limit):
    res_list_stream = cli_ken.list_streams(Limit = limit)
    return res_list_stream

def get_kinesis_shards(stream_name, shard_id):
    res_shard_iter = cli_ken.get_shard_iterator(StreamName = stream_name, ShardId = shard_id, ShardIteratorType = 'LATEST')
    return res_shard_iter

def list_shards(stream_name):
    res_shard_lst = cli_ken.list_shards(StreamName = stream_name)
    lst_shards = [shard_id['ShardId'] for shard_id in res_shard_lst['Shards']]     
    return lst_shards

def get_record(shard_key):
    res_get_rec =  cli_ken.get_records(ShardIterator = shard_key, Limit = 10)
    return res_get_rec['Records']

def put_record(stream_name, data, key):
    res_put_rec = cli_ken.put_record(StreamName = stream_name, Data = data, PartitionKey = key)
    print ("Results from PUT: ShardId = {} and Sequence Number = {}".format (res_put_rec ['ShardId'], res_put_rec['SequenceNumber']))
    return [res_put_rec ['ShardId'], res_put_rec['SequenceNumber']]
    
def del_stream(stream_name):
    res_stream_del =cli_ken.delete_stream(StreamName=stream_name)
    return res_stream_del

if __name__ == '__main__':
    
    found=False
    stream_name = "Aji_Stream"
    shards = 1
    #Create a stream   
    create_stream(stream_name,shards)    
    #Descrive a stream to get the Stream Status
    stream_status = describe_stream(stream_name)['StreamDescription'] ['StreamStatus']
    #Loop in till the stream is active
    while stream_status != "ACTIVE":
        print("Waiting for the stream to be active....")
        t.sleep(10)
        if describe_stream(stream_name)['StreamDescription'] ['StreamStatus'] == "ACTIVE":
            found=True
            break
    #If the Stream is Active.. Get the Shard ID
    if found==True:        
        shard_id  = describe_stream(stream_name)['StreamDescription'] ['Shards'][0]['ShardId']
    #If it gets a Shard ID.. Create the Shard Iterator
    if shard_id != "":    
        shard_key = get_kinesis_shards(stream_name, shard_id)['ShardIterator']
    
    #If the Get Data returns null.. Input a record to the stream    
    if len(get_record(shard_key)) == 0:
        shard_seq = put_record(stream_name,"Aji_Test_Data", "1")
    
    #Get the result of the data put inside the stream in the earlier command        
    if len(get_record(shard_key)) != 0:            
        result = [str(val['Data']) for val in get_record(shard_key)]
        print(result)
    # Delete the Stream        
    del_stream(stream_name)    
  
    #Verify whether the stream is deleated.
    stream_status = describe_stream(stream_name)['StreamDescription'] ['StreamStatus']        
    while stream_status != 'ACTIVE':
        try:
            print("Waiting for the stream to be deleted....")
            t.sleep(10)         
            stream_status = describe_stream(stream_name)['StreamDescription'] ['StreamStatus']
            if stream_status != 'DELETING':            
                break
        except ResourceNotFoundException:
            print("Stream Deleted.....")
            break




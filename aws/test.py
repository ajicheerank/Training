import boto3 as bt
import csv
import json
from itertools import islice
import operator

dydb = bt.resource("dynamodb")
tbl_store = dydb.Table("aji_store")
tbl_trans = dydb.Table("aji_trans")
tbl_trans_v1 = dydb.Table("aji_trans_v1")

def create_json_store():
    fs_csv = open("master.csv","r")
    fs_json = open ("master.json","w")
    
    field_name = ('StoreID','RegionID','StateID','CityID')
    reader = csv.DictReader(fs_csv, field_name)
    for row in reader:
        json.dump(row,fs_json)
        fs_json.write("\n")
    fs_json.close()
    
def create_json_trans():
    fs_csv = open("trans_data.csv","r")
    fs_json = open ("trans_data.json","w")
    
    field_name = ('Transaction','Store','Product','Customer')
    reader = csv.DictReader(fs_csv, field_name)
    for row in reader:
        json.dump(row,fs_json)
        fs_json.write("\n")
    fs_json.close()    


def put_item_store():
    fs_item = open ("master.json","r")  
    with tbl_store.batch_writer() as batch:
        for rows in fs_item:
            x = json.loads(rows)
            batch.put_item(Item = x)
    fs_item.close()

def put_item_trans():
    with tbl_trans.batch_writer() as batch:
        with open ("trans_data.json","r") as fs_item:
            for row in islice(fs_item, 1000):
                x = json.loads(row)
                batch.put_item(Item = x)
    fs_item.close()

def put_item_trans_v1():
    fs_item = open ("trans_data.json","r")  
    with tbl_trans_v1.batch_writer() as batch:
        with open ("trans_data.json","r") as fs_item:
            for row in islice(fs_item, 10000):
                x = json.loads(row)
                item = tbl_store.get_item(Key = {'StoreID': x['Store']})                
                sub_data = item["Item"]
                result = {"product_id+store_id": x['Product']+"+"+x['Store'] , "transaction_id" : x['Transaction'] ,"customer_id" : x['Customer'], "RegionID": sub_data['RegionID'], "StateID": sub_data['StateID'], "CityID" :sub_data['CityID']}
                batch.put_item(Item = result)
        fs_item.close()

def query(in_param):
    qry = tbl_trans_v1.query(KeyConditionExpression = Key('product_id+store_id').eq(in_param))
    result = qry['Items']
    print(len(result))

def query_top_5():
    qry = tbl_trans_v1.scan()
    result = qry['Items']
    
    dict_product = {}
    
    for prod in result:
        product = prod['product_id+store_id'].split("+")[0]
        
        if product not in dict_product:
            dict_product[product] = 0
        dict_product[product] += 1
    lst_items = sorted(dict_product, key= dict_product.__getitem__) 
    print ("Top five products: {}".format(lst_items [-5:]))#[for sorted(dict_product.values())[-5:]

if __name__ == "__main__":
    #create_json_store() 
    #put_item_store()
    #create_json_trans()  
    #put_item_trans_v1()
    #put_item_trans_v1()
    #in_query = input("input the store and product seperate by + : ")
    query("86+33")
    query("86+13")
    query_top_5()
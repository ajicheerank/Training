import boto3 as bt
from boto3.dynamodb.conditions import Key, Attr



dydb = bt.resource("dynamodb")
table = dydb.Table("aji_store")

#table.put_item(Item={'emp_name':'test_emp', 'emp_id':234567, 'department':'science'})

#df_data = table.scan()
#print(df_data)

item = table.get_item(Key = {'StoreID': "1"})
data = item["Item"]
print(type(data))

'''
qry = table.query(KeyConditionExpression = Key('emp_name').eq('Aji'))
emp_name = qry['Items']
print(emp_name)

tbl_scan = table.scan(FilterExpression = Attr("emp_id").contains([124304, 234567]))
trans = tbl_scan["Items"]

for trn in trans:
    print(trn['emp_name'])

'''
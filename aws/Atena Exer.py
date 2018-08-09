import boto3
import pprint as pp
import time

cli_athena = boto3.client("athena")

def list_named_queries(saved_qry_name):
    qry_string=""
    lst = cli_athena.list_named_queries()
    for qry_id in lst['NamedQueryIds']:        
        qry = cli_athena.get_named_query(NamedQueryId = qry_id)
        if saved_qry_name == qry['NamedQuery']['Name']:
            qry_string = qry['NamedQuery']['QueryString'].replace("\n"," ")
            break
    return qry_string

def start_qry_exec(qry_string):
    result = cli_athena.start_query_execution(QueryString = qry_string, ResultConfiguration={'OutputLocation':'s3://aji-invesco-bucket/sales_data'})
    #print([name for name  in qry['NamedQuery'].items() if name[0] in ('Name','QueryString','NamedQueryId')])
    return str(result['QueryExecutionId'])

def get_query_exec(query_id):
    result = cli_athena.get_query_execution(QueryExecutionId = query_id)    
    return result['QueryExecution']['Status']['State']

def get_query_result(query_id):
    result = cli_athena.get_query_results(QueryExecutionId = query_id)
    pp.pprint(result)

if __name__ == '__main__':
    state, retry = "", 1
    
    qry_string = list_named_queries('aji_saved_1')
    
    exe_id = start_qry_exec(qry_string)
    
    while state != "SUCCEEDED" or retry == 5:
        state = get_query_exec(exe_id)
        retry+=1
        time.sleep(5)
    
    if state == "SUCCEEDED":
       get_query_result(exe_id) 
    else:
       print("Failed to retrive the query results")
        
    #if state == "SUCCEEDED": 
    #    break
        
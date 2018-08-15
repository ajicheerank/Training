import boto3
import pprint
import time

cli_glue = boto3.client("glue")

def get_jobs():
    list_jobs = cli_glue.get_jobs()
    for job in list_jobs['Jobs']:
        pprint.pprint(job['Name'])
        
def start_job(job_name):
    response = cli_glue.start_job_run(JobName=job_name)
    return response
    
def get_job_run(job_name, run_id):
    response = cli_glue.get_job_run(JobName=job_name, RunId=run_id)
    return response['JobRun']['JobRunState']
    

if __name__ == '__main__':
    
    status = ""
    
    #get_jobs()
    
    response = start_job('aji_glue_sales')['JobRunId']
    
    while status != "SUCCEEDED":
        status = get_job_run('aji_glue_sales', response)
        print(status)
        time.sleep(10)
        

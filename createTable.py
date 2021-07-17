# Usage -
# python createTable.py "locationOf/Abc.hql"

import boto3
import sys
import time
import logging

def readHQL(fileLocation: str):
    """
        Read Query inside HQL File
        Input:
        fileLocation: Location of HQL File
        Output:
        Return Schema of the file.
    """
    try:
        query = ""
        with open(fileLocation) as fr:
            query = fr.read()
        logger.info('SQL Query inside HQL File : %s' % json.dumps(query))
        return query
    except Exception:
        print(traceback.print_exc())

def athenaQuery(fileLocation: str, database: str, outputLocation: str):
    """
        Run Athena Query to execute the query inside HQL File
        Input:
        fileLocation - Location of HQL File
        database - Database in which table is to be made
        outputLocation - S3 Location where output of Athena Query would be saved.
    """
    try:
        client = boto3.client('athena', region_name='us-east-1')
        queryStart = client.start_query_execution(
            QueryString = readHQL(fileLocation),
            QueryExecutionContext = {
                'Database': database
            },
            ResultConfiguration = { 'OutputLocation': outputLocation}
        )
        time.sleep(1)
        logger.info('Athena Query Execution Id: %s' % json.dumps(queryStart['QueryExecutionId']))
        return queryStart['QueryExecutionId']
    except Exception:
        print(traceback.print_exc())

if __name__ == "__main__":
    fileLocation = sys.argv[1]
    database = sys.argv[2]
    outputLocation = sys.argv[3]
    athenaQuery(fileLocation, database, outputLocation)
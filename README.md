# createTableFromHQLinAWS
Script to Create Glue Table from HQL File 

Creating Table in Glue Data Catalog is essential as all the other services will connect to Glue for Data Catalog purpose. 

In general, Glue Data Catalog stores all the metadata of files stored in AWS. 

There are various way to create a Glue Data Catalog Table in AWS - 
1) Create it manually
2) Create it using the Cloudformation Template.
3) Create it using the Crawler running on files. 
4) Create it using running Athena Query

We are going to connect to Athena API using Python Boto3 SDK where the qeury will be taken from HQL file which will create Glue Data Catalog Table. 

Usage -
python createTable.py "locationOf/Abc.hql" "database" "s3OutputLocation"

Test Code for the Same is also provided. 

# cloud_db_mgmt_pooling_migrations
HHA 504 Assignment 4C


# Setup Azure


I set up Azure Database for MySQL flexible server. I made sure to change the firewall rule to 0.0.0.0 in order to allow for outside connections to the server. I also made sure to turn off the require_secure_transport parameter to have additional flexibility in the connections.


# Setup GCP


I set up GCP database using a flexible server with the lowest settings to make it run at a cheaper price. I allowed for 0.0.0.0/0 as an allowed network to make it easier to connect from Cloud Shell and MySQL Workbench.


# Azure Errors


I was able to establish a connection with the database in both Google Shell and MySQL Workbench. With only some spelling mistakes I was able to fix any errors that I faced.


# GCP Errors


I had a similar outcome with GCP as I did with Azure establishing a connection and not running into many major issues


# Azure Schema and Data Population


For the schema, I created two tables called 'patients' and 'medical records' that had their own columns. The 'patients' table had the columns (first_name, last_name, date_of_birth, gender, contact_number). The 'medical records' table had the columns (patient_id, diagnosis, treatment, admission_date, discharge_date). Each had its own primary keys called 'id' and the 'medical_records' table had the foreign key of 'patient_id'.


I also populated the tables with fake information such as names, dates, and diagnoses. I put in 4 rows worth of information.


# GCP Schema and Data Population


For the schema, I used the same schema as the one in Azure.


I had also put in the same amount of fake information to populate the tables in GCP as I did in Azure.


# Flask Errors


With the flask setup after a lot of trial and error, I was able to get it to run with the homepage I had set up for my app. However, I was not able to get my tables to show on my app. I kept having the error where it couldn’t find the column called ‘patients_name’ however I couldn’t find as to where it was trying to find that specific column. Overall I was able to get the app to launch, but just not the table to show up. 




# Alembic Setup


For the Alembic setup, I went through the following steps for both Azure and GCP.


First I set up Alembic using the command ` alembic init migrations `


Second I established the connection using ` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `


Third within the newly created env.py file I uncommented and changed the lines `from db_schema import Base` and `target_metadata = Base.metadata `.


After that I used the command ` alembic revision --autogenerate -m "create tables" `. This will allow alembic to keep track of the changes I make by creating a table within my database.




For the GCP migration I changed the 'patients' table to have a new column called "is_alive"
For the Azure migrations I changed the 'patients' table to have the new columns called 'is_alive' and 'is_breathing'.


I then ran the migration using ` alembic upgrade head `. This created an instance of the migration.


To see a history of the migrations made I used ` alembic upgrade head --sql > migration.sql ` and it created a new sql file with the changes and comments that I made.



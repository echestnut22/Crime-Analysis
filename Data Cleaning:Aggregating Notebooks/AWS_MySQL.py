#!/usr/bin/env python
# coding: utf-8

# ## This work book is for using the AWS crimedbmysql datababase
# 
# 
# This is the raw connection information
# """
# host="crimedbmysql.cspoouh9lugd.us-east-2.rds.amazonaws.com"
# user="crimeadmin"
# password="4DAnuuSBWVQ92w!F"
# database="crimedb_mysql"
# 
# """
# #### SM Example usage to connect to DB with a cursor
# #Connect to db
# db_connection, cursor = connect_to_database()
# print(f"Connected to MySQL database: {db_connection}")

# In[84]:


#!pip install mysql-connector-python requests


# In[85]:


import mysql.connector
import csv 


# In[86]:


#SM Define some standard functions

#SM Function to connect to the Database
def connect_to_database():
    # Crime Analysis AWS MySQL server details
    db_config = {
        'host': 'crimedbmysql.cspoouh9lugd.us-east-2.rds.amazonaws.com',
        'user': 'crimeadmin',
        'password': '4DAnuuSBWVQ92w!F',
        'database': 'crimedb_mysql',
    }

    try:
        # Connect to the MySQL server
        db_connection = mysql.connector.connect(**db_config)

        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()

        print("Connected to the database.")
        return db_connection, cursor

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None

def close_connection(db_connection, cursor):
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if db_connection:
        db_connection.close()
        print("Connection closed.")

def delete_table(cursor, table_name):
    # Delete the table
    delete_table_query = f"DROP TABLE IF EXISTS {table_name}"
    cursor.execute(delete_table_query)
    print(f"Table '{table_name}' deleted successfully.")
    
def create_table_if_not_exists(table_name, columns):
    #MySQL server details
    db_config = {
        'host': 'crimedbmysql.cspoouh9lugd.us-east-2.rds.amazonaws.com',
        'user': 'crimeadmin',
        'password': '4DAnuuSBWVQ92w!F',
        'database': 'crimedb_mysql',
    }

    # Construct the table creation query based on parameters
    table_creation_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            {', '.join([f'{col} {data_type}' for col, data_type in columns])}
        )
    '''

    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute the table creation query
        cursor.execute(table_creation_query)

        # Commit the changes
        connection.commit()

        print(f"Table '{table_name}' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()



# In[ ]:





# In[ ]:





# In[97]:


#SM show all table names by connecting to db and fetching all table names and then close the conneciton
# Check if the connection is successful and print db object name
#Connect to db
db_connection, cursor = connect_to_database()

if db_connection.is_connected():
    print(f"Connected to MySQL database: {db_connection}")

    # Create a cursor
    cursor = db_connection.cursor()

    # Get the list of tables in the database
    cursor.execute("SHOW TABLES")

    # Fetch and print the results
    tables = cursor.fetchall()
    print("\nTables in the database:")
    for table in tables:
        print(table[0])

    # Close the cursor and connection
    cursor.close()
    db_connection.close()
    print("closed cursor and connection to db")
else:
    print("Connection failed")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # SM Change Log Dec 18 added all cleaned datasets to DB and did a count of rows to match the csv minus the header. Might need to tweak the data types as we work the the data. The Latitude and Longitude data types SQL insert query was not accepting the POINT or GEOMETRY place holders. There is likely be a better way to do these inserts, but didn't want to delay any further.
# 
# You should see these table names:
# Clean_Train_Data
# Cleaned_Bus_Stop_Locations
# Cleaned_Bus_Stop_Ridership
# Cleaned_Census_Data
# Cleaned_CommAreas
# Cleaned_Crime_IUCR_Codes
# Cleaned_Grocery_Stores_2013
# Cleaned_Housing_Developments
# Cleaned_Police_Sentiment_Scores

# In[71]:


#Police Sentiment Score Code. Saving for later in case needed as it was long to write
#1 of 2

#SM made this markdown when no new tables need to be created. Run when needed.
#This will create a table

def main():
    
    db_config = {
        'host': 'crimedbmysql.cspoouh9lugd.us-east-2.rds.amazonaws.com',
        'user': 'crimeadmin',
        'password': '4DAnuuSBWVQ92w!F',
        'database': 'crimedb_mysql',
    }
    # Specify the table name and columns with their data types
    table_name = 'Cleaned_Police_Sentiment_Scores'
    columns = [
        ('id', 'INT AUTO_INCREMENT PRIMARY KEY'),
        ('AREA', 'DECIMAL(3, 3)'),  
        ('DISTRICT', 'DECIMAL(3, 3)'),
        ('SECTOR', 'DECIMAL(3, 3)'),
        ('SAFETY', 'DECIMAL(3, 3)'),
        ('S_RACE_AFRICAN_AMERICAN', 'DECIMAL(3, 3)'),
        ('S_RACE_ASIAN_AMERICAN', 'DECIMAL(3, 3)'),
        ('S_RACE_HISPANIC', 'DECIMAL(3, 3)'),
        ('S_RACE_WHITE', 'DECIMAL(3, 3)'),
        ('S_RACE_OTHER', 'DECIMAL(3, 3)'),
        ('S_AGE_LOW', 'DECIMAL(3, 3)'),
        ('S_AGE_MEDIUM', 'DECIMAL(3, 3)'),
        ('S_AGE_HIGH', 'DECIMAL(3, 3)'),
        ('S_SEX_FEMALE', 'DECIMAL(3, 3)'),
        ('S_SEX_MALE', 'DECIMAL(3, 3)'),
        ('S_EDUCATION_LOW', 'DECIMAL(3, 3)'),
        ('S_EDUCATION_MEDIUM', 'DECIMAL(3, 3)'),
        ('S_EDUCATION_HIGH', 'DECIMAL(3, 3)'),
        ('S_INCOME_LOW', 'DECIMAL(3, 3)'),
        ('S_INCOME_MEDIUM', 'DECIMAL(3, 3)'),
        ('S_INCOME_HIGH', 'DECIMAL(3, 3)'),
        ('TRUST', 'DECIMAL(3, 3)'),
        ('T_RACE_AFRICAN_AMERICAN', 'DECIMAL(3, 3)'),
        ('T_RACE_ASIAN_AMERICAN', 'DECIMAL(3, 3)'),
        ('T_RACE_HISPANIC', 'DECIMAL(3, 3)'),
        ('T_RACE_WHITE', 'DECIMAL(3, 3)'),
        ('T_RACE_OTHER', 'DECIMAL(3, 3)'),
        ('T_AGE_LOW', 'DECIMAL(3, 3)'),
        ('T_AGE_MEDIUM', 'DECIMAL(3, 3)'),
        ('T_AGE_HIGH', 'DECIMAL(3, 3)'),
        ('T_SEX_FEMALE', 'DECIMAL(3, 3)'),
        ('T_SEX_MALE', 'DECIMAL(3, 3)'),
        ('T_EDUCATION_LOW', 'DECIMAL(3, 3)'),
        ('T_EDUCATION_MEDIUM', 'DECIMAL(3, 3)'),
        ('T_EDUCATION_HIGH', 'DECIMAL(3, 3)'),
        ('T_INCOME_LOW', 'DECIMAL(3, 3)'),
        ('T_INCOME_MEDIUM', 'DECIMAL(3, 3)'),
        ('T_INCOME_HIGH', 'DECIMAL(3, 3)'),
        ('T_LISTEN', 'DECIMAL(3, 3)'),
        ('T_LISTEN_RACE_AFRICAN_AMERICAN', 'DECIMAL(3, 3)'),
        ('T_LISTEN_RACE_ASIAN_AMERICAN', 'DECIMAL(3, 3)'),
        ('T_LISTEN_RACE_HISPANIC', 'DECIMAL(3, 3)'),
        ('T_LISTEN_RACE_WHITE', 'DECIMAL(3, 3)'),
        ('T_LISTEN_RACE_OTHER', 'DECIMAL(3, 3)'),
        ('T_LISTEN_AGE_LOW', 'DECIMAL(3, 3)'),
        ('T_LISTEN_AGE_MEDIUM', 'DECIMAL(3, 3)'),
        ('T_LISTEN_AGE_HIGH', 'DECIMAL(3, 3)'),
        ('T_LISTEN_SEX_FEMALE', 'DECIMAL(3, 3)'),
        ('T_LISTEN_SEX_MALE', 'DECIMAL(3, 3)'),
        ('T_LISTEN_EDUCATION_LOW', 'DECIMAL(3, 3)'),
        ('T_LISTEN_EDUCATION_MEDIUM', 'DECIMAL(3, 3)'),
        ('T_LISTEN_EDUCATION_HIGH', 'DECIMAL(3, 3)'),
        ('T_LISTEN_INCOME_LOW', 'DECIMAL(3, 3)'),
        ('T_LISTEN_INCOME_MEDIUM', 'DECIMAL(3, 3)'),
        ('T_LISTEN_INCOME_HIGH', 'DECIMAL(3, 3)'),
        ('T_RESPECT', 'DECIMAL(3, 3)'),
        ('T_RESPECT_RACE_AFRICAN_AMERICAN', 'DECIMAL(3, 3)'),
        ('T_RESPECT_RACE_ASIAN_AMERICAN', 'DECIMAL(3, 3)'),
        ('T_RESPECT_RACE_HISPANIC', 'DECIMAL(3, 3)'),
        ('T_RESPECT_RACE_WHITE', 'DECIMAL(3, 3)'),
        ('T_RESPECT_RACE_OTHER', 'DECIMAL(3, 3)'),
        ('T_RESPECT_AGE_LOW', 'DECIMAL(3, 3)'),
        ('T_RESPECT_AGE_MEDIUM', 'DECIMAL(3, 3)'),
        ('T_RESPECT_AGE_HIGH', 'DECIMAL(3, 3)'),
        ('T_RESPECT_SEX_FEMALE', 'DECIMAL(3, 3)'),
        ('T_RESPECT_SEX_MALE', 'DECIMAL(3, 3)'),
        ('T_RESPECT_EDUCATION_LOW', 'DECIMAL(3, 3)'),
        ('T_RESPECT_EDUCATION_MEDIUM', 'DECIMAL(3, 3)'),
        ('T_RESPECT_EDUCATION_HIGH', 'DECIMAL(3, 3)'),
        ('T_RESPECT_INCOME_LOW', 'DECIMAL(3, 3)'),
        ('T_RESPECT_INCOME_MEDIUM', 'DECIMAL(3, 3)'),
        ('T_RESPECT_INCOME_HIGH', 'DECIMAL(3, 3)'),
        ('START_DATE', 'DATE'),
        ('END_DATE', 'DATE')
    ]
    create_table_if_not_exists(table_name, columns)
    
if __name__ == "__main__":
    main()


# In[88]:


#Police Sentiment Score Code. Saving for later in case needed as it was long to write
#2 of 2
#EW: # Change Summary:
# - Updated the data insertion process to use batch processing instead of inserting data row by row.
# - This method groups multiple rows into batches (set up currently with 1000 rows per batch), reduces the number of separate database operations and transactions, enhancing performance.
# - Took about insertion time to about 3 mins and 24 seconds to insert 32696 rows. I deleted the table and re-did it and it took 26 seconds

# Specify the path to your CSV file
#EW - Had to update to point to where I had the files because it was giving me errors. Change back to the file below
csv_file_path = '/Users/shawnadmin/Workspace/capstone/data/Cleaned/CleanedDatasets/Police_Sentiment_Scores.csv' 


# SQL query to insert data into the table 
#Typically values are NUll for auto incrementing, %s for commons, ST_GeomFromText(%s) for GEOMETRY
insert_query = """
INSERT INTO Cleaned_Police_Sentiment_Scores
(id, AREA, DISTRICT, SECTOR, SAFETY, S_RACE_AFRICAN_AMERICAN, S_RACE_ASIAN_AMERICAN, S_RACE_HISPANIC, S_RACE_WHITE, S_RACE_OTHER, 
S_AGE_LOW, S_AGE_MEDIUM, S_AGE_HIGH, S_SEX_FEMALE, S_SEX_MALE, S_EDUCATION_LOW, S_EDUCATION_MEDIUM, S_EDUCATION_HIGH, S_INCOME_LOW, 
S_INCOME_MEDIUM, S_INCOME_HIGH, TRUST, T_RACE_AFRICAN_AMERICAN, T_RACE_ASIAN_AMERICAN, T_RACE_HISPANIC, T_RACE_WHITE, T_RACE_OTHER, 
T_AGE_LOW, T_AGE_MEDIUM, T_AGE_HIGH, T_SEX_FEMALE, T_SEX_MALE, T_EDUCATION_LOW, T_EDUCATION_MEDIUM, T_EDUCATION_HIGH, T_INCOME_LOW, 
T_INCOME_MEDIUM, T_INCOME_HIGH, T_LISTEN, T_LISTEN_RACE_AFRICAN_AMERICAN, T_LISTEN_RACE_ASIAN_AMERICAN, T_LISTEN_RACE_HISPANIC, 
T_LISTEN_RACE_WHITE, T_LISTEN_RACE_OTHER, T_LISTEN_AGE_LOW, T_LISTEN_AGE_MEDIUM, T_LISTEN_AGE_HIGH, T_LISTEN_SEX_FEMALE, T_LISTEN_SEX_MALE, 
T_LISTEN_EDUCATION_LOW, T_LISTEN_EDUCATION_MEDIUM, T_LISTEN_EDUCATION_HIGH, T_LISTEN_INCOME_LOW, T_LISTEN_INCOME_MEDIUM, T_LISTEN_INCOME_HIGH, 
T_RESPECT, T_RESPECT_RACE_AFRICAN_AMERICAN, T_RESPECT_RACE_ASIAN_AMERICAN, T_RESPECT_RACE_HISPANIC, T_RESPECT_RACE_WHITE, T_RESPECT_RACE_OTHER, 
T_RESPECT_AGE_LOW, T_RESPECT_AGE_MEDIUM, T_RESPECT_AGE_HIGH, T_RESPECT_SEX_FEMALE, T_RESPECT_SEX_MALE, T_RESPECT_EDUCATION_LOW, T_RESPECT_EDUCATION_MEDIUM, 
T_RESPECT_EDUCATION_HIGH, T_RESPECT_INCOME_LOW, T_RESPECT_INCOME_MEDIUM, T_RESPECT_INCOME_HIGH, START_DATE, END_DATE)
VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
# Connect to the MySQL database
try:
    # Connect to db
    db_connection, cursor = connect_to_database()
    cursor = db_connection.cursor()

    # Open and read data from the CSV file
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row

#EW - Updated code using the Batch insert operation, instead of inserting each row individually, collect a batch of rows and insert them together. This reduces the number of database operations.
        batch_size = 1000  # Adjust this number based on your environment, currently batch size is 1000 rows
        batch = []

        # Execute the insert query in batches
        for row in csv_reader:
            batch.append(tuple(row))
            if len(batch) == batch_size:
                cursor.executemany(insert_query, batch)
                batch = []

        # Insert any remaining rows
        if batch:
            cursor.executemany(insert_query, batch)

    # Commit the changes
    db_connection.commit()
    print("Data inserted successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the database connection
    if db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("Connection closed.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # The below code will create a new table

# #SM made this markdown when no new tables need to be created. Run when needed.
# #This will create a table
# 
# def main():
#     
#     db_config = {
#         'host': 'crimedbmysql.cspoouh9lugd.us-east-2.rds.amazonaws.com',
#         'user': 'crimeadmin',
#         'password': '4DAnuuSBWVQ92w!F',
#         'database': 'crimedb_mysql',
#     }
#     # Specify the table name and columns with their data types
#     table_name = 'Cleaned_SomeTable'
#     columns = [
#         ('id', 'INT AUTO_INCREMENT PRIMARY KEY'),
#         ('Community_Area_Name', 'VARCHAR(255)'),
#         ('Community_Area_Number', 'INT'),
#         ('Property_Type', 'VARCHAR(255)'),
#         ('Property_Name', 'VARCHAR(255)'),
#         ('ADDRESS', 'VARCHAR(255)'),
#         ('ZIP_CODE', 'INT'),
#         ('Phone_Number', 'VARCHAR(255)'),
#         ('Management_Company', 'VARCHAR(255)'),
#         ('Units', 'INT'),
#         ('X_COORDINATE', 'VARCHAR(255)'),
#         ('Y_COORDINATE', 'VARCHAR(255)'),
#         ('LATITUDE', 'VARCHAR(255)'),
#         ('LONGITUDE', 'VARCHAR(255)'),
#         ('LOCATION', 'VARCHAR(255)'),
#         ]
# 
#     create_table_if_not_exists(table_name, columns)
#     
# if __name__ == "__main__":
#     main()

# # The below code will drop a table

# #SM made this markdown so that it is only run when needed.
# #NOTE TAKE EXTRA CAUTION - This will delete a table
# 
# 
# #MySQL server details
# db_config = {
#         'host': 'crimedbmysql.cspoouh9lugd.us-east-2.rds.amazonaws.com',
#         'user': 'crimeadmin',
#         'password': '4DAnuuSBWVQ92w!F',
#         'database': 'crimedb_mysql',
# }
# #Make sure to update this to the table you want to delete
# deletethis_table_name = 'tablename'
#    
#     
# try:
#     # Connect to the MySQL server
#     connection = mysql.connector.connect(**db_config)
#     cursor = connection.cursor()
# 
#     # Execute the table creation query
#     cursor.execute(f"DROP TABLE IF EXISTS {deletethis_table_name}")
# 
#     # Commit the changes
#     connection.commit()
# 
#     print(f"Table '{deletethis_table_name}'  deleted!")
# 
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# 
# finally:
#     # Close the cursor and connection
#     if 'cursor' in locals() and cursor:
#         cursor.close()
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()

# In[ ]:





# In[89]:


#SM Used this to count rows in a CSV and view the headers replace file path as needed
#Count the number of rows in a specified CSV file
def count_csv_rows(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Use the built-in `sum` function to count rows efficiently
            row_count = sum(1 for row in csv_reader)
            
            return row_count

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0

# Specify the path to your CSV file
csv_file_path = '/Users/shawnadmin/Workspace/capstone/data/Cleaned/CleanedDatasets/Police_Sentiment_Scores.csv'

# Call the function to count rows
num_rows = count_csv_rows(csv_file_path)

print(f"Number of rows in the CSV file: {num_rows}")

#Print header of csv file
with open(f'{csv_file_path}', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

print(header)


# In[ ]:





# In[50]:





# In[92]:


#EW: Run Query to Validate Number of Rows In The Table 
def count_rows_in_table(cursor, table_name):
    # SQL query to count rows in the table
    count_query = f"SELECT COUNT(*) FROM {table_name}"

    # Execute the query
    cursor.execute(count_query)

    # Fetch the result
    return cursor.fetchone()[0]

# Connect to the MySQL database and count rows
try:
    db_connection, cursor = connect_to_database()

    # Count rows in the Clean_Train_Data table
    row_count = count_rows_in_table(cursor, "Cleaned_Police_Sentiment_Scores")
    print(f"Number of rows in the table: {row_count}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the database connection
    if db_connection and db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("Connection closed.")


# 

# In[ ]:





# In[98]:


#SM connect to db and fetch and print all Tables, columns, and rows
#this could take a long time now now that data has been inserted in tables

#Connect to db
db_connection, cursor = connect_to_database()

# Check if the connection is successful
if db_connection.is_connected():
    print(f"Connected to MySQL database: {db_connection}")

    # Create a cursor
    cursor = db_connection.cursor()

    # Get the list of tables in the database
    cursor.execute("SHOW TABLES")

    # Fetch and print the results
    tables = cursor.fetchall()
    print("\nTables in the database:")
    for table in tables:
        table_name = table[0]
        print(f"\nData in table '{table_name}':")

        # Fetch all rows from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Fetch column names
        cursor.execute(f"DESC {table_name}")
        columns = [column[0] for column in cursor.fetchall()]

        # Print column names
        print("\t".join(columns))

        # Print data
        for row in rows:
            print("\t".join(str(value) for value in row))

    # Close the cursor and connection
    cursor.close()
    db_connection.close()
else:
    print("Connection failed")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Code Snippets below 
# 
# #SM will clean up in a future verison
# 

# #Example read header csv
# with open('/Users/shawnadmin/Workspace/capstone/data/Cleaned/CleanedDatasets/Crime_IUCR_Codes.csv', 'r') as f:
#     reader = csv.reader(f)
#     header = next(reader)
# 
# print(header)

# ## CENSUS DATA EXAMPLE

# In[ ]:





# In[ ]:





# #SM attempting to Insert Clean_Train_DATA data into table named Clean_Train_Data
# #SM this hangs when running this cell 
# #EW: # Change Summary:
# # - Updated the data insertion process to use batch processing instead of inserting data row by row.
# # - This method groups multiple rows into batches (set up currently with 1000 rows per batch), reduces the number of separate database operations and transactions, enhancing performance.
# # - Took about insertion time to about 3 mins and 24 seconds to insert 32696 rows. I deleted the table and re-did it and it took 26 seconds
# 
# # Specify the path to your CSV file
# #EW - Had to update to point to where I had the files because it was giving me errors. Change back to the file below
# csv_file_path = '/Users/shawnadmin/Workspace/capstone/data/Cleaned/CleanedDatasets/.csv' 
# 
# 
# # SQL query to insert data into the table 
# #Typically values are NUll for auto incrementing, %s for commons, ST_GeomFromText(%s) for GEOMETRY
# insert_query = """
# INSERT INTO Cleaned_
# (id, STORE_NAME, LICENSE_ID, ACCOUNT_NUMBER, SQUARE_FEET, BUFFER_SIZE, ADDRESS, ZIP_CODE, COMMUNITY_AREA_NAME, COMMUNITY_AREA, WARD, CENSUS_TRACT, CENSUS_BLOCK, X_COORDINATE, Y_COORDINATE, LATITUDE, LONGITUDE, LOCATION)
# VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
# """
# 
# # Connect to the MySQL database
# try:
#     # Connect to db
#     db_connection, cursor = connect_to_database()
#     cursor = db_connection.cursor()
# 
#     # Open and read data from the CSV file
#     with open(csv_file_path, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)  # Skip header row
# 
# #EW - Updated code using the Batch insert operation, instead of inserting each row individually, collect a batch of rows and insert them together. This reduces the number of database operations.
#         batch_size = 1000  # Adjust this number based on your environment, currently batch size is 1000 rows
#         batch = []
# 
#         # Execute the insert query in batches
#         for row in csv_reader:
#             batch.append(tuple(row))
#             if len(batch) == batch_size:
#                 cursor.executemany(insert_query, batch)
#                 batch = []
# 
#         # Insert any remaining rows
#         if batch:
#             cursor.executemany(insert_query, batch)
# 
#     # Commit the changes
#     db_connection.commit()
#     print("Data inserted successfully!")
# 
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# 
# finally:
#     # Close the database connection
#     if db_connection.is_connected():
#         cursor.close()
#         db_connection.close()
#         print("Connection closed.")

# In[ ]:





# #SM 1 of 2 Example Census Data 
# 
# #This will create a table
# def main():
#     
#     db_config = {
#         'host': 'crimedbmysql.cspoouh9lugd.us-east-2.rds.amazonaws.com',
#         'user': 'crimeadmin',
#         'password': '4DAnuuSBWVQ92w!F',
#         'database': 'crimedb_mysql',
#     }
#     # Specify the table name and columns with their data types
#     table_name = 'Cleaned_Census_Data'
#     columns = [
#         ('id', 'INT AUTO_INCREMENT PRIMARY KEY'),
#         ('Community_Area_Number', 'INT'),
#         ('COMMUNITY_AREA_NAME', 'VARCHAR(255)'),
#         ('PERCENT_OF_HOUSING_CROWDED', 'DECIMAL(5, 2)'),
#         ('PERCENT_HOUSEHOLDS_BELOW_POVERTY', 'DECIMAL(5, 2)'),
#         ('PERCENT_AGED_16_UNEMPLOYED', 'DECIMAL(5, 2)'),
#         ('PERCENT_AGED_25_WITHOUT_HIGH_SCHOOL_DIPLOMA', 'DECIMAL(5, 2)'),
#         ('PERCENT_AGED_UNDER_18_OR_OVER_64', 'DECIMAL(5, 2)'),
#         ('PER_CAPITA_INCOME', 'INT'),
#         ('HARDSHIP_INDEX', 'INT')
#         ]
# 
#     create_table_if_not_exists(table_name, columns)
#     
# if __name__ == "__main__":
#     main()

# #SM 2 of 2 #SM attempting to Insert Clean_Train_DATA data into table named Clean_Train_Data
# #SM this hangs when running this cell 
# #EW: # Change Summary:
# # - Updated the data insertion process to use batch processing instead of inserting data row by row.
# # - This method groups multiple rows into batches (set up currently with 1000 rows per batch), reduces the number of separate database operations and transactions, enhancing performance.
# # - Took about insertion time to about 3 mins and 24 seconds to insert 32696 rows. I deleted the table and re-did it and it took 26 seconds
# 
# # Specify the path to your CSV file
# #EW - Had to update to point to where I had the files because it was giving me errors. Change back to the file below
# csv_file_path = '/Users/shawnadmin/Workspace/capstone/data/Cleaned/CleanedDatasets/Census_Data.csv' 
# 
# 
# # SQL query to insert data into the table
# insert_query = """
# INSERT INTO Cleaned_Census_Data
# (id, Community_Area_Number, COMMUNITY_AREA_NAME, PERCENT_OF_HOUSING_CROWDED, PERCENT_HOUSEHOLDS_BELOW_POVERTY, 
#  PERCENT_AGED_16_UNEMPLOYED, PERCENT_AGED_25_WITHOUT_HIGH_SCHOOL_DIPLOMA, PERCENT_AGED_UNDER_18_OR_OVER_64, 
#  PER_CAPITA_INCOME, HARDSHIP_INDEX)
# VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s);
# """
# 
# # Connect to the MySQL database
# try:
#     # Connect to db
#     db_connection, cursor = connect_to_database()
#     cursor = db_connection.cursor()
# 
#     # Open and read data from the CSV file
#     with open(csv_file_path, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)  # Skip header row
# 
# #EW - Updated code using the Batch insert operation, instead of inserting each row individually, collect a batch of rows and insert them together. This reduces the number of database operations.
#         batch_size = 1000  # Adjust this number based on your environment, currently batch size is 1000 rows
#         batch = []
# 
#         # Execute the insert query in batches
#         for row in csv_reader:
#             batch.append(tuple(row))
#             if len(batch) == batch_size:
#                 cursor.executemany(insert_query, batch)
#                 batch = []
# 
#         # Insert any remaining rows
#         if batch:
#             cursor.executemany(insert_query, batch)
# 
#     # Commit the changes
#     db_connection.commit()
#     print("Data inserted successfully!")
# 
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# 
# finally:
#     # Close the database connection
#     if db_connection.is_connected():
#         cursor.close()
#         db_connection.close()
#         print("Connection closed.")

# In[ ]:





# #COMMASREA
# 
# #SM made this markdown when no new tables need to be created. Run when needed.
# #This will create a table
# 
# def main():
#     
#     db_config = {
#         'host': 'crimedbmysql.cspoouh9lugd.us-east-2.rds.amazonaws.com',
#         'user': 'crimeadmin',
#         'password': '4DAnuuSBWVQ92w!F',
#         'database': 'crimedb_mysql',
#     }
#     # Specify the table name and columns with their data types
#     table_name = 'Cleaned_CommAreas'
#     columns = [
#         ('id', 'INT AUTO_INCREMENT PRIMARY KEY'),
#         ('the_geom', 'VARCHAR(255)'),  
#         ('PERIMETER', 'DECIMAL(10, 2)'),
#         ('AREA', 'DECIMAL(10, 2)'),
#         ('COMAREA_', 'DECIMAL(10, 2)'),
#         ('COMAREA_ID', 'DECIMAL(10, 2)'),
#         ('AREA_NUMBE', 'DECIMAL(10, 2)'),
#         ('COMMUNITY', 'VARCHAR(255)'),
#         ('AREA_NUM_1', 'DECIMAL(10, 2)'),
#         ('SHAPE_AREA', 'DECIMAL(10, 10)'),
#         ('SHAPE_LEN', 'DECIMAL(10, 10)'),
#         ]
# 
#     create_table_if_not_exists(table_name, columns)
#     
# if __name__ == "__main__":
#     main()
# #SM attempting to Insert Clean_Train_DATA data into table named Clean_Train_Data
# #SM this hangs when running this cell 
# #EW: # Change Summary:
# # - Updated the data insertion process to use batch processing instead of inserting data row by row.
# # - This method groups multiple rows into batches (set up currently with 1000 rows per batch), reduces the number of separate database operations and transactions, enhancing performance.
# # - Took about insertion time to about 3 mins and 24 seconds to insert 32696 rows. I deleted the table and re-did it and it took 26 seconds
# 
# # Specify the path to your CSV file
# #EW - Had to update to point to where I had the files because it was giving me errors. Change back to the file below
# csv_file_path = '/Users/shawnadmin/Workspace/capstone/data/Cleaned/CleanedDatasets/CommAreas.csv' 
# 
# 
# # SQL query to insert data into the table 
# #Typically values are NUll for auto incrementing, %s for commons, ST_GeomFromText(%s) for GEOMETRY
# insert_query = """
# INSERT INTO Cleaned_CommAreas
# (id, the_geom, PERIMETER, AREA, COMAREA_, COMAREA_ID, AREA_NUMBE, COMMUNITY, AREA_NUM_1, SHAPE_AREA, SHAPE_LEN)
# VALUES(NULL, ST_GeomFromText(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s);
# """
# 
# # Connect to the MySQL database
# try:
#     # Connect to db
#     db_connection, cursor = connect_to_database()
#     cursor = db_connection.cursor()
# 
#     # Open and read data from the CSV file
#     with open(csv_file_path, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)  # Skip header row
# 
# #EW - Updated code using the Batch insert operation, instead of inserting each row individually, collect a batch of rows and insert them together. This reduces the number of database operations.
#         batch_size = 1000  # Adjust this number based on your environment, currently batch size is 1000 rows
#         batch = []
# 
#         # Execute the insert query in batches
#         for row in csv_reader:
#             batch.append(tuple(row))
#             if len(batch) == batch_size:
#                 cursor.executemany(insert_query, batch)
#                 batch = []
# 
#         # Insert any remaining rows
#         if batch:
#             cursor.executemany(insert_query, batch)
# 
#     # Commit the changes
#     db_connection.commit()
#     print("Data inserted successfully!")
# 
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# 
# finally:
#     # Close the database connection
#     if db_connection.is_connected():
#         cursor.close()
#         db_connection.close()
#         print("Connection closed.")

# In[ ]:





# In[ ]:





# #Police Sentiment Score Code. Saving for later in case needed as it was long to write
# #1 of 2
# 
# #SM made this markdown when no new tables need to be created. Run when needed.
# #This will create a table
# 
# def main():
#     
#     db_config = {
#         'host': 'crimedbmysql.cspoouh9lugd.us-east-2.rds.amazonaws.com',
#         'user': 'crimeadmin',
#         'password': '4DAnuuSBWVQ92w!F',
#         'database': 'crimedb_mysql',
#     }
#     # Specify the table name and columns with their data types
#     table_name = 'Cleaned_Police_Sentiment_Scores'
#     columns = [
#         ('id', 'INT AUTO_INCREMENT PRIMARY KEY'),
#         ('AREA', 'DECIMAL(3, 3)'),  
#         ('DISTRICT', 'DECIMAL(3, 3)'),
#         ('SECTOR', 'DECIMAL(3, 3)'),
#         ('SAFETY', 'DECIMAL(3, 3)'),
#         ('S_RACE_AFRICAN_AMERICAN', 'DECIMAL(3, 3)'),
#         ('S_RACE_ASIAN_AMERICAN', 'DECIMAL(3, 3)'),
#         ('S_RACE_HISPANIC', 'DECIMAL(3, 3)'),
#         ('S_RACE_WHITE', 'DECIMAL(3, 3)'),
#         ('S_RACE_OTHER', 'DECIMAL(3, 3)'),
#         ('S_AGE_LOW', 'DECIMAL(3, 3)'),
#         ('S_AGE_MEDIUM', 'DECIMAL(3, 3)'),
#         ('S_AGE_HIGH', 'DECIMAL(3, 3)'),
#         ('S_SEX_FEMALE', 'DECIMAL(3, 3)'),
#         ('S_SEX_MALE', 'DECIMAL(3, 3)'),
#         ('S_EDUCATION_LOW', 'DECIMAL(3, 3)'),
#         ('S_EDUCATION_MEDIUM', 'DECIMAL(3, 3)'),
#         ('S_EDUCATION_HIGH', 'DECIMAL(3, 3)'),
#         ('S_INCOME_LOW', 'DECIMAL(3, 3)'),
#         ('S_INCOME_MEDIUM', 'DECIMAL(3, 3)'),
#         ('S_INCOME_HIGH', 'DECIMAL(3, 3)'),
#         ('TRUST', 'DECIMAL(3, 3)'),
#         ('T_RACE_AFRICAN_AMERICAN', 'DECIMAL(3, 3)'),
#         ('T_RACE_ASIAN_AMERICAN', 'DECIMAL(3, 3)'),
#         ('T_RACE_HISPANIC', 'DECIMAL(3, 3)'),
#         ('T_RACE_WHITE', 'DECIMAL(3, 3)'),
#         ('T_RACE_OTHER', 'DECIMAL(3, 3)'),
#         ('T_AGE_LOW', 'DECIMAL(3, 3)'),
#         ('T_AGE_MEDIUM', 'DECIMAL(3, 3)'),
#         ('T_AGE_HIGH', 'DECIMAL(3, 3)'),
#         ('T_SEX_FEMALE', 'DECIMAL(3, 3)'),
#         ('T_SEX_MALE', 'DECIMAL(3, 3)'),
#         ('T_EDUCATION_LOW', 'DECIMAL(3, 3)'),
#         ('T_EDUCATION_MEDIUM', 'DECIMAL(3, 3)'),
#         ('T_EDUCATION_HIGH', 'DECIMAL(3, 3)'),
#         ('T_INCOME_LOW', 'DECIMAL(3, 3)'),
#         ('T_INCOME_MEDIUM', 'DECIMAL(3, 3)'),
#         ('T_INCOME_HIGH', 'DECIMAL(3, 3)'),
#         ('T_LISTEN', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_RACE_AFRICAN_AMERICAN', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_RACE_ASIAN_AMERICAN', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_RACE_HISPANIC', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_RACE_WHITE', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_RACE_OTHER', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_AGE_LOW', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_AGE_MEDIUM', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_AGE_HIGH', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_SEX_FEMALE', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_SEX_MALE', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_EDUCATION_LOW', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_EDUCATION_MEDIUM', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_EDUCATION_HIGH', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_INCOME_LOW', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_INCOME_MEDIUM', 'DECIMAL(3, 3)'),
#         ('T_LISTEN_INCOME_HIGH', 'DECIMAL(3, 3)'),
#         ('T_RESPECT', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_RACE_AFRICAN_AMERICAN', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_RACE_ASIAN_AMERICAN', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_RACE_HISPANIC', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_RACE_WHITE', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_RACE_OTHER', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_AGE_LOW', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_AGE_MEDIUM', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_AGE_HIGH', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_SEX_FEMALE', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_SEX_MALE', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_EDUCATION_LOW', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_EDUCATION_MEDIUM', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_EDUCATION_HIGH', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_INCOME_LOW', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_INCOME_MEDIUM', 'DECIMAL(3, 3)'),
#         ('T_RESPECT_INCOME_HIGH', 'DECIMAL(3, 3)'),
#         ('START_DATE', 'DATE'),
#         ('END_DATE', 'DATE')
#     ]
#     create_table_if_not_exists(table_name, columns)
#     
# if __name__ == "__main__":
#     main()

# #Police Sentiment Score Code. Saving for later in case needed as it was long to write
# #2 of 2
# #EW: # Change Summary:
# # - Updated the data insertion process to use batch processing instead of inserting data row by row.
# # - This method groups multiple rows into batches (set up currently with 1000 rows per batch), reduces the number of separate database operations and transactions, enhancing performance.
# # - Took about insertion time to about 3 mins and 24 seconds to insert 32696 rows. I deleted the table and re-did it and it took 26 seconds
# 
# # Specify the path to your CSV file
# #EW - Had to update to point to where I had the files because it was giving me errors. Change back to the file below
# csv_file_path = '/Users/shawnadmin/Workspace/capstone/data/Cleaned/CleanedDatasets/Police_Sentiment_Scores.csv' 
# 
# 
# # SQL query to insert data into the table 
# #Typically values are NUll for auto incrementing, %s for commons, ST_GeomFromText(%s) for GEOMETRY
# insert_query = """
# INSERT INTO Cleaned_Police_Sentiment_Scores
# (id, AREA, DISTRICT, SECTOR, SAFETY, S_RACE_AFRICAN_AMERICAN, S_RACE_ASIAN_AMERICAN, S_RACE_HISPANIC, S_RACE_WHITE, S_RACE_OTHER, 
# S_AGE_LOW, S_AGE_MEDIUM, S_AGE_HIGH, S_SEX_FEMALE, S_SEX_MALE, S_EDUCATION_LOW, S_EDUCATION_MEDIUM, S_EDUCATION_HIGH, S_INCOME_LOW, 
# S_INCOME_MEDIUM, S_INCOME_HIGH, TRUST, T_RACE_AFRICAN_AMERICAN, T_RACE_ASIAN_AMERICAN, T_RACE_HISPANIC, T_RACE_WHITE, T_RACE_OTHER, 
# T_AGE_LOW, T_AGE_MEDIUM, T_AGE_HIGH, T_SEX_FEMALE, T_SEX_MALE, T_EDUCATION_LOW, T_EDUCATION_MEDIUM, T_EDUCATION_HIGH, T_INCOME_LOW, 
# T_INCOME_MEDIUM, T_INCOME_HIGH, T_LISTEN, T_LISTEN_RACE_AFRICAN_AMERICAN, T_LISTEN_RACE_ASIAN_AMERICAN, T_LISTEN_RACE_HISPANIC, 
# T_LISTEN_RACE_WHITE, T_LISTEN_RACE_OTHER, T_LISTEN_AGE_LOW, T_LISTEN_AGE_MEDIUM, T_LISTEN_AGE_HIGH, T_LISTEN_SEX_FEMALE, T_LISTEN_SEX_MALE, 
# T_LISTEN_EDUCATION_LOW, T_LISTEN_EDUCATION_MEDIUM, T_LISTEN_EDUCATION_HIGH, T_LISTEN_INCOME_LOW, T_LISTEN_INCOME_MEDIUM, T_LISTEN_INCOME_HIGH, 
# T_RESPECT, T_RESPECT_RACE_AFRICAN_AMERICAN, T_RESPECT_RACE_ASIAN_AMERICAN, T_RESPECT_RACE_HISPANIC, T_RESPECT_RACE_WHITE, T_RESPECT_RACE_OTHER, 
# T_RESPECT_AGE_LOW, T_RESPECT_AGE_MEDIUM, T_RESPECT_AGE_HIGH, T_RESPECT_SEX_FEMALE, T_RESPECT_SEX_MALE, T_RESPECT_EDUCATION_LOW, T_RESPECT_EDUCATION_MEDIUM, 
# T_RESPECT_EDUCATION_HIGH, T_RESPECT_INCOME_LOW, T_RESPECT_INCOME_MEDIUM, T_RESPECT_INCOME_HIGH, START_DATE, END_DATE)
# VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# """
# # Connect to the MySQL database
# try:
#     # Connect to db
#     db_connection, cursor = connect_to_database()
#     cursor = db_connection.cursor()
# 
#     # Open and read data from the CSV file
#     with open(csv_file_path, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)  # Skip header row
# 
# #EW - Updated code using the Batch insert operation, instead of inserting each row individually, collect a batch of rows and insert them together. This reduces the number of database operations.
#         batch_size = 1000  # Adjust this number based on your environment, currently batch size is 1000 rows
#         batch = []
# 
#         # Execute the insert query in batches
#         for row in csv_reader:
#             batch.append(tuple(row))
#             if len(batch) == batch_size:
#                 cursor.executemany(insert_query, batch)
#                 batch = []
# 
#         # Insert any remaining rows
#         if batch:
#             cursor.executemany(insert_query, batch)
# 
#     # Commit the changes
#     db_connection.commit()
#     print("Data inserted successfully!")
# 
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# 
# finally:
#     # Close the database connection
#     if db_connection.is_connected():
#         cursor.close()
#         db_connection.close()
#         print("Connection closed.")

# # Example CODE FOR SQL  to insert data into the table
# insert_query = """
# INSERT INTO Cleaned_Crime_IUCR_Codes
# (ICUR, Month, Station_ID, Station_Name, Avg_Weekday_Rides, Avg_Saturday_Rides, Avg_Sunday_Holiday_Rides, Monthly_Total, Lat_Lon, Community, Comm_Num, SHAPE_AREA, SHAPE_LEN)
# VALUES (%s, %s, %s, %s, %s, %s, %s, %s, ST_GeomFromText(%s), %s, %s, %s, %s)
# """

# #SM example code for simple functions, but not written to allow for different data
# 
# def create_table(cursor, table_name):
#     # Create a sample table
#     create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         crime_type VARCHAR(255) NOT NULL,
#         location VARCHAR(255) NOT NULL,
#         date_reported DATE
#     )
#     """
# 
#     cursor.execute(create_table_query)
#     print(f"Table '{table_name}' created successfully.")
#     
#     """
# def insert_data(cursor, table_name, data):
#     # Insert data into the table
#     insert_query = f"INSERT INTO {table_name} (crime_type, location, date_reported) VALUES (%s, %s, %s)"
#     cursor.execute(insert_query, data)
#     print("Data inserted successfully.")
# 
# def update_data(cursor, table_name, data):
#     # Update data in the table
#     update_query = f"UPDATE {table_name} SET crime_type = %s WHERE location = %s"
#     cursor.execute(update_query, data)
#     print(f"Data updated successfully in '{table_name}'.")
# 
# def delete_data(cursor, table_name, data):
#     # Delete data from the table
#     delete_query = f"DELETE FROM {table_name} WHERE location = %s"
#     cursor.execute(delete_query, data)
#     print(f"Data deleted successfully from '{table_name}'.")
# 
# def select_data(cursor, table_name):
#     # Select data from the table
#     select_query = f"SELECT * FROM {table_name}"
#     cursor.execute(select_query)
#     print(f"Selected data from '{table_name}'.")

# #Connect to db
# db_connection, cursor = connect_to_database()
# 
# # Check if the connection is successful
# if db_connection.is_connected():
#     print(f"Connected to MySQL database: {db_connection}")
# 
#     # Create a cursor
#     cursor = db_connection.cursor()
# 
#     # Close the cursor and connection
#     cursor.close()
#     db_connection.close()
# else:
#     print("Connection failed")

# #SM for Train data
# 
# import csv
# import mysql.connector
# 
# 
# # Define the table creation query
# create_table_query = """
# CREATE TABLE your_table_name (
#     ID INT AUTO_INCREMENT PRIMARY KEY,
#     Year INT,
#     Month DATE,
#     Station_ID INT,
#     Station_Name VARCHAR(255),
#     Avg_Weekday_Rides FLOAT,
#     Avg_Saturday_Rides FLOAT,
#     Avg_Sunday_Holiday_Rides FLOAT,
#     Monthly_Total INT,
#     Lat_Lon POINT,
#     Community VARCHAR(255),
#     Comm_Num INT,
#     SHAPE_AREA DOUBLE,
#     SHAPE_LEN DOUBLE
# );
# """
# 
# 
# # Specify the path to your CSV file
# csv_file_path = '/data/Cleaned/CleanedDatasets/Train_Data.csv'
# 
# # SQL query to insert data into the table
# insert_query = """
# INSERT INTO your_table_name 
# (Year, Month, Station_ID, Station_Name, Avg_Weekday_Rides, Avg_Saturday_Rides, Avg_Sunday_Holiday_Rides, Monthly_Total, Lat_Lon, Community, Comm_Num, SHAPE_AREA, SHAPE_LEN)
# VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# """
# 
# # Connect to the MySQL database
# try:
#     #Connect to db
#     db_connection, cursor = connect_to_database()
#     cursor = db_connection.cursor()
# 
#     # Open and read data from the CSV file
#     with open(csv_file_path, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)  # Skip header row
# 
#         # Execute the insert query for each row of data
#         for row in csv_reader:
#             cursor.execute(insert_query, tuple(row))
# 
#     # Commit the changes
#     connection.commit()
#     print("Data inserted successfully!")
# 
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# 
# finally:
#     # Close the database connection
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("Connection closed.")

# # Define the table creation query
# create_table_train_data = """
# CREATE TABLE Clean_Train_Data (
#     ID INT AUTO_INCREMENT PRIMARY KEY,
#     Year INT,
#     Month DATE,
#     Station_ID INT,
#     Station_Name VARCHAR(255),
#     Avg_Weekday_Rides FLOAT,
#     Avg_Saturday_Rides FLOAT,
#     Avg_Sunday_Holiday_Rides FLOAT,
#     Monthly_Total INT,
#     Lat_Lon POINT,
#     Community VARCHAR(255),
#     Comm_Num INT,
#     SHAPE_AREA DOUBLE,
#     SHAPE_LEN DOUBLE
# );
# """
# 
# # Connect to the MySQL database
# try:
#     db_connection, cursor = connect_to_database()
#     cursor = connection.cursor()
# 
#     # Execute the table creation query
#     cursor.execute(create_table_train_data)
#     print("Table created successfully!")
# 
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# 
# finally:
#     # Close the database connection
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("Connection closed.")

# ####TESING CREATE TABLE CODE
# 
# CREATE TABLE transit_data (
#     Year INT,
#     Month DATE,
#     Station_ID INT,
#     Station_Name VARCHAR(255),
#     Avg_Weekday_Rides DECIMAL(10, 2),
#     Avg_Saturday_Rides DECIMAL(10, 2),
#     Avg_Sunday_Holiday_Rides DECIMAL(10, 2),
#     Monthly_Total INT,
#     Lat_Lon POINT,
#     Community VARCHAR(255),
#     Comm_Num INT,
#     SHAPE_AREA DECIMAL(18, 2),
#     SHAPE_LEN DECIMAL(18, 5)
# );
# 
# -- Load data from CSV file into the table
# LOAD DATA INFILE '/path/to/your/file.csv'
# INTO TABLE transit_data
# FIELDS TERMINATED BY ',' ENCLOSED BY '"'
# LINES TERMINATED BY '\r\n'
# IGNORE 1 LINES; -- Ignore the header row

# #### SM Example code to import data into the
# #SM getting error on types compare to dataset 
# #SM enter data from Crimes_-_2001_to_Present_20231108 csv file
# # Check if the connection is successful
# if connection.is_connected():
#     print(f"Connected to MySQL database: {database}")
# 
#     # Create a cursor
#     cursor = connection.cursor()
# 
#     # Create a new table (if not exists)
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS CrimeData (
#         ID INT PRIMARY KEY,
#         CaseNumber VARCHAR(255),
#         Date DATE,
#         Block VARCHAR(255),
#         IUCR VARCHAR(10),
#         PrimaryType VARCHAR(255),
#         Description VARCHAR(255),
#         LocationDescription VARCHAR(255),
#         Arrest BOOLEAN,
#         Domestic BOOLEAN,
#         Beat INT,
#         District INT,
#         Ward INT,
#         CommunityArea INT,
#         FBICode VARCHAR(5),
#         XCoordinate FLOAT,
#         YCoordinate FLOAT,
#         Year INT,
#         UpdatedOn TIMESTAMP,
#         Latitude FLOAT,
#         Longitude FLOAT,
#         Location VARCHAR(255),
#         HistoricalWards20032015 INT,
#         ZipCodes INT,
#         CommunityAreas INT,
#         CensusTracts INT,
#         Wards INT,
#         BoundariesZIPCodes INT,
#         PoliceDistricts INT,
#         PoliceBeats INT
#     )
#     """
#     cursor.execute(create_table_query)
#     print("CrimeData table created successfully.")
# 
#     # Read data from the CSV file and insert into the 'CrimeData' table
#     with open(csv_file_path, 'r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
# 
#         # Skip the header row
#         next(csv_reader, None)
# 
#         insert_query = """
#         INSERT INTO CrimeData (
#             ID, CaseNumber, Date, Block, IUCR, PrimaryType, Description,
#             LocationDescription, Arrest, Domestic, Beat, District, Ward,
#             CommunityArea, FBICode, XCoordinate, YCoordinate, Year, UpdatedOn,
#             Latitude, Longitude, Location, HistoricalWards20032015, ZipCodes,
#             CommunityAreas, CensusTracts, Wards, BoundariesZIPCodes,
#             PoliceDistricts, PoliceBeats
#         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """
# 
#         for row in csv_reader:
#             data_to_insert = (
#                 int(row['ID']),
#                 row['Case Number'],
#                 row['Date'],
#                 row['Block'],
#                 row['IUCR'],
#                 row['Primary Type'],
#                 row['Description'],
#                 row['Location Description'],
#                 row['Arrest'].lower() == 'true',  # Assuming 'Arrest' is 'true' or 'false' in the CSV
#                 row['Domestic'].lower() == 'true',
#                 int(row['Beat']),
#                 int(row['District']),
#                 int(row['Ward']),
#                 int(row['Community Area']),
#                 row['FBI Code'],
#                 float(row['X Coordinate']),
#                 float(row['Y Coordinate']),
#                 int(row['Year']),
#                 row['Updated On'],
#                 float(row['Latitude']),
#                 float(row['Longitude']),
#                 row['Location'],
#                 int(row['Historical Wards 2003-2015']),
#                 int(row['Zip Codes']),
#                 int(row['Community Areas']),
#                 int(row['Census Tracts']),
#                 int(row['Wards']),
#                 int(row['Boundaries - ZIP Codes']),
#                 int(row['Police Districts']),
#                 int(row['Police Beats'])
#             )
#             cursor.execute(insert_query, data_to_insert)
# 
#     connection.commit()
#     print("Data inserted into the CrimeData table.")
# 
#     # Close the cursor and connection
#     cursor.close()
#     connection.close()
# else:
#     print("Connection failed")

# In[ ]:





# #SM CREATE TABLE CODE
# 
# CREATE TABLE clean_train_data (
#     Year INT,
#     Month DATE,
#     Station_ID INT,
#     Station_Name VARCHAR(255),
#     Avg_Weekday_Rides DECIMAL(10, 2),
#     Avg_Saturday_Rides DECIMAL(10, 2),
#     Avg_Sunday_Holiday_Rides DECIMAL(10, 2),
#     Monthly_Total INT,
#     Lat_Lon POINT,
#     Community VARCHAR(255),
#     Comm_Num INT,
#     SHAPE_AREA DECIMAL(18, 2),
#     SHAPE_LEN DECIMAL(18, 5)
# );
# 
# -- Load data from CSV file into the table
# LOAD DATA INFILE '/data/Cleaned/CleanedDatasets/Train_Data.csv'
# INTO TABLE transit_data
# FIELDS TERMINATED BY ',' ENCLOSED BY '"'
# LINES TERMINATED BY '\r\n'
# IGNORE 1 LINES; -- Ignore the header row

# 
# # Replace 'your_table_name' with the actual name of the table you want to delete
# table_to_delete = 'Clean_Train_Data'
# 
# #Connect to db
# db_connection, cursor = connect_to_database()
# print(f"Connected to MySQL database: {db_connection}")
# 
# if db_connection.is_connected():
#     print(f"Connected to MySQL database: {db_connection}")
# 
#     # Create a cursor
#     cursor = db_connection.cursor()
# 
#     # Get the list of tables in the database
#     cursor.execute("SHOW TABLES")
# 
#     # Fetch and print the results
#     delete_table(cursor, {table_to_delete})
# 
#     # Close the cursor and connection
#     cursor.close()
#     db_connection.close()
#     print("closed cursor and connection to db")
# else:
#     print("Connection failed")

# In[ ]:





# #Connect to db
# db_connection, cursor = connect_to_database()
# print(f"Connected to MySQL database: {db_connection}")
# 
# if db_connection.is_connected():
#     print(f"Connected to MySQL database: {db_connection}")
# 
#     # Create a cursor
#     cursor = db_connection.cursor()
# 
#     # Get the list of tables in the database
#     cursor.execute("SHOW TABLES")
# 
#     # Fetch and print the results
#     tables = cursor.fetchall()
#     print("\nTables in the database:")
#     for table in tables:
#         print(table[0])
# 
#     # Fetch and print the results
#     tables = cursor.fetchall()
#     print("\nTables in the database:")
#     for table in tables:
#         table_name = table[0]
#         print(f"\nData in table '{table_name}':")
# 
#         # Fetch all rows from the table
#         cursor.execute(f"SELECT * FROM {table_name}")
#         rows = cursor.fetchall()
# 
#         # Fetch column names
#         cursor.execute(f"DESC {table_name}")
#         columns = [column[0] for column in cursor.fetchall()]
# 
#         # Print column names
#         print("\t".join(columns))
# 
#         # Print data
#         for row in rows:
#             print("\t".join(str(value) for value in row))
# 
#     # Close the cursor and connection
#     cursor.close()
#     db_connection.close()
#     print("closed cursor and connection to db")
# else:
#     print("Connection failed")

# In[ ]:





# # SM attempting to create table creation query for train data
# try:
#     # Connect to db
#     db_connection, cursor = connect_to_database()
#     cursor = db_connection.cursor()
#     
#     
#      """
# CREATE TABLE Clean_Train_Data (
#     ID INT AUTO_INCREMENT PRIMARY KEY,
#     Year INT,
#     Month DATE,
#     Station_ID INT,
#     Station_Name VARCHAR(255),
#     Avg_Weekday_Rides FLOAT,
#     Avg_Saturday_Rides FLOAT,
#     Avg_Sunday_Holiday_Rides FLOAT,
#     Monthly_Total INT,
#     Lat_Lon POINT,
#     Community VARCHAR(255),
#     Comm_Num INT,
#     SHAPE_AREA DOUBLE,
#     SHAPE_LEN DOUBLE
# );
# """
# 

# In[ ]:





# ### Example insert
# 
# def main():
#     # Specify the table name and columns with their data types
#     table_name = 'Cleaned_Bus_Stop_Locations'
#    
#     columns = [
#     ('id', 'INT AUTO_INCREMENT PRIMARY KEY'),
#     ('SYSTEMSTOP', 'INT'),
#     ('CROSS_ST', 'VARCHAR(255)'),
#     ('DIR', 'VARCHAR(10)'),
#     ('POS', 'VARCHAR(10)'),
#     ('ROUTESSTPG', 'VARCHAR(10)')
#          ('ROUTESSTPG', 'VARCHAR(10)')
#          ('ROUTESSTPG', 'VARCHAR(10)')
#     ]
# 
#     create_table_if_not_exists(table_name, columns)
#     #SM run once complete
# if __name__ == "__main__":
#     main()

# #CLEANRED GROCRY STORE 2 OF 2
# #SM attempting to Insert Clean_Train_DATA data into table named Clean_Train_Data
# #SM this hangs when running this cell 
# #EW: # Change Summary:
# # - Updated the data insertion process to use batch processing instead of inserting data row by row.
# # - This method groups multiple rows into batches (set up currently with 1000 rows per batch), reduces the number of separate database operations and transactions, enhancing performance.
# # - Took about insertion time to about 3 mins and 24 seconds to insert 32696 rows. I deleted the table and re-did it and it took 26 seconds
# 
# # Specify the path to your CSV file
# #EW - Had to update to point to where I had the files because it was giving me errors. Change back to the file below
# #csv_file_path = '/Users/shawnadmin/Workspace/capstone/data/Cleaned/CleanedDatasets/name.csv' 
# 
# 
# # SQL query to insert data into the table 
# #Typically values are NUll for auto incrementing, %s for commons, ST_GeomFromText(%s) for GEOMETRY
# insert_query = """
# INSERT INTO Cleaned_tablename
# (id, Community_Area_Name, Community_Area_Number, Property_Type, Property_Name, Address, Zip_Code, Phone_Number, Management_Company, Units, X_Coordinate, Y_Coordinate, Latitude, Longitude, Location)
# VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
# """
# 
# # Connect to the MySQL database
# try:
#     # Connect to db
#     db_connection, cursor = connect_to_database()
#     cursor = db_connection.cursor()
# 
#     # Open and read data from the CSV file
#     with open(csv_file_path, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)  # Skip header row
# 
# #EW - Updated code using the Batch insert operation, instead of inserting each row individually, collect a batch of rows and insert them together. This reduces the number of database operations.
#         batch_size = 1000  # Adjust this number based on your environment, currently batch size is 1000 rows
#         batch = []
# 
#         # Execute the insert query in batches
#         for row in csv_reader:
#             batch.append(tuple(row))
#             if len(batch) == batch_size:
#                 cursor.executemany(insert_query, batch)
#                 batch = []
# 
#         # Insert any remaining rows
#         if batch:
#             cursor.executemany(insert_query, batch)
# 
#     # Commit the changes
#     db_connection.commit()
#     print("Data inserted successfully!")
# 
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# 
# finally:
#     # Close the database connection
#     if db_connection.is_connected():
#         cursor.close()
#         db_connection.close()
#         print("Connection closed.")

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





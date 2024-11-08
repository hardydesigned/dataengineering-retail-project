import os
from time import time
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

user = os.environ['POSTGRES_USER'] 
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
db = os.environ['POSTGRES_DBNAME']
table_name = os.environ['POSTGRES_SCHEMA']


def ingest_data(table_name, data_path):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    order_data_iter = pd.read_csv(data_path, iterator=True, chunksize=100000)

    order_data_df = next(order_data_iter)

    order_data_df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    order_data_df.to_sql(name=table_name, con=engine, if_exists='append')


    while True: 

        try:
            t_start = time()
            
            df = next(order_data_iter)

            df.to_sql(name=table_name, con=engine, if_exists='replace')

            t_end = time()

            print('inserted another chunk, took %.3f second' % (t_end - t_start), 'for table:', table_name)

        except StopIteration:
            print("Finished ingesting data into the postgres database: ", table_name)
            break

ingest_data("order_data", "../data/order_data.csv")
ingest_data("marketing_data", "../data/marketing_data.csv")
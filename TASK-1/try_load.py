from google.cloud import bigquery
import os
import json

def write_to_bigquery(table_id, rows_to_insert):
    client = bigquery.Client()
    table = client.get_table(table_id)
    errors = client.insert_rows(table, rows_to_insert)
    if errors:
        print('Encountered errors while inserting rows: {}'.format(errors))
    else:
        print('Successfully insert data')

project_id = os.getenv('studious-works-402905')
table_id = 'studious-works-402905.my_dataset.my_table'
rows_to_insert = [{"name": "bintang", "age": 18, "hobby": "playing a guitar"},
    {"name": "sagara", "age": 19, "hobby": "playing golf"},
    {"name": "zayyan", "age": 21, "hobby": "soccer"},
    {"name": "alesha", "age": 24, "hobby": "singing"},
    {"name": "ganesha", "age": 16, "hobby": "playing DOTA"},
    {"name": "sacchio", "age": 14, "hobby": "sleeping"}
]

file_path = 'data.json'

with open(file_path, 'w') as json_file:
    json.dump(rows_to_insert, json_file, indent=2)

write_to_bigquery(table_id, rows_to_insert)
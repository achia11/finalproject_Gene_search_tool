#!/usr/bin/env python3

import mysql.connector
import os
import json

#read JSON file downloaded from human protein atlas database https://www.proteinatlas.org
atlasfile = "proteinatlas.json"
json_data = open(atlasfile).read()
json_obj = json.loads(json_data)

conn = mysql.connector.connect(user='achia2', password='JHop#120804', host='localhost', database='achia2')
cursor = conn.cursor()

#need to validate values and covert to utf-8 due to error:
#"Failed processing format-parameters; %s" % err)
#mysql.connector.errors.ProgrammingError: Failed processing format-parameters; Python 'list' cannot be converted to a MySQL type
def validate_value(item):
    if item is not None:
        return str(item).encode('utf-8')
    else:
        return item

#parse out only gene, ensembl, gene description, and protein class from human atlas database
for i, value in enumerate(json_obj):
    gene = value.get("Gene") #get for dictionary.get(keyname, value) Value is default at None, or defined value if key doesn't exist
    ensembl_ID = validate_value(value.get("Ensembl"))
    gene_des = validate_value(value.get("Gene description"))
    prot_class = validate_value(value.get("Protein class"))

    cursor.execute("INSERT INTO proteinatlas (gene, ensembl_ID, gene_description, protein_class) VALUES (%s, %s, %s, %s)", (gene, ensembl_ID, gene_des, prot_class))

conn.commit()
conn.close()
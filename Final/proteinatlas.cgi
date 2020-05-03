#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector


def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()

    #form is search with a category selected: gene or protein
    term = form.getvalue('search_term')

    if form.getvalue('searchqry'):
        searchqry = form.getvalue('searchqry')
    else:
        searchqry = "Not found"


    conn = mysql.connector.connect(user='achia2', password='JHop#120804', host='localhost', database='achia2')
    cursor = conn.cursor()

    # query is dependent on whether gene or protein is selected
    if searchqry in ['gene_term', 'protein_term']:

        if searchqry == 'gene_term':

            geneqry = """
                  SELECT gene, ensembl_ID, gene_description, protein_class
                      FROM proteinatlas
                      WHERE gene_description LIKE %s
            """

            cursor.execute(geneqry, ('%' + term + '%', ))

            #results are appended to list for terms that match within gene description
            results = { 'match_count': 0, 'matches': list() }
            for (gene, ensembl_ID, gene_description, protein_class) in cursor:
                results['matches'].append({'gene': gene, 'ensembl_ID': ensembl_ID, 'gene_description': gene_description, 'protein_class': protein_class})
                results['match_count'] += 1

        elif searchqry == 'protein_term':

            protqry = """
                  SELECT gene, ensembl_ID, gene_description, protein_class
                      FROM proteinatlas
                      WHERE protein_class LIKE %s
            """
            cursor.execute(protqry, ('%' + term + '%', ))

            #results are appended to list for terms that match within protein class
            results = { 'match_count': 0, 'matches': list() }
            for (gene, ensembl_ID, gene_description, protein_class) in cursor:
                results['matches'].append({'gene': gene, 'ensembl_ID': ensembl_ID, 'gene_description': gene_description, 'protein_class': protein_class})
                results['match_count'] += 1
         

    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()
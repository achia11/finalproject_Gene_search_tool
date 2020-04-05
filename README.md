410.712.81 Final Project

The purpose of this project is to create a simple search tool, through data mining, where user is allowed to search for a specific term, and have results returned. For this project, I’ll be using a database called the human protein atlas (https://www.proteinatlas.org), where I’ll be performing a similar search function to parse out the information related to the search term entered by user. 

The main interface would be through a simple HTML form, to enter the search term. It’ll then return results for the total count of genes related to that term, and its name (possibly including molecular function, or Ensembl gene ID). Ideally, the user will be able to search out genes with a specific term, and further research can be completed through the Ensembl ID. In the webpage, I would also include a link to Ensembl.

Files downloadable for the database are in JSON, TSV, and RDF format (https://www.proteinatlas.org/about/download), and I’ll be using JSON format to store the data into MySQL. The storing of the database on MySQL can be performed through importing of the JSON python library, with enumerating each gene, and inserting it into the database itself. 

As the database is rather large, I’ll like to attempt with only inserting values that the results would show. For example, if the user searched “TLR3”, it’ll return 3 columns with TLR3 as the gene name, the next column with its name, and a following column showing the Ensembl ID (if present). That means, I’ll only be inserting gene ID, gene name, and Ensembl ID into MySQL database.

From which, the search term will be parsed through a CGI script and queried through MySQL database, and return the results into the same website. Formatting of the webpage will be handled through CSS, and backend scripting will be through javascript. Within the Javascript, it’ll have AJAX, and likely adding autocomplete JQuery function as well. 


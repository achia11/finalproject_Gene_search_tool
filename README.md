<h1>Human gene search tool</h1>

<br><b>*ABOUT*</b></br>
Web interface for a simple data mining tool from an external source, and outputs results by searching on a term found within gene description. Created for the final project for 410.712.81 Advanced Practical Computer Concepts for Bioinformatics

<br><b>*BACKGROUND*</b></br>
The purpose of this project is to create a simple search tool, through data mining. Output is based on user's choice of search term, and term is search through the gene description of the database. Source is obtained from a database called the human protein atlas (https://www.proteinatlas.org). This database provides an extensive list of genes found within the human genome, together with additional information such as Ensembl ID, the type of protein classes each gene is associated to, the position found within the chromosome, and many more. 

For simplicity of the mining tool, the output is customized to displaying only the gene ID, Ensembl ID, and gene description, and protein classes. Database is downloaded in the JSON format, and with each gene and its associated data uploaded to MySQL. 

The search term is parsed through a CGI script to send the term back to the customized database, and javascript/JQuery is used to create the output of results through the AJAX call, and finally displayed in a table in HTML. An option to download the search results is provided to perform further filtering through Excel. 

<br><b>*DETAILED USAGE*</b></br>
1. Enter a search term (e.g receptor) into the search box. 
2. Each gene description that matches the search term is added row by row to the table. 
3. The full table is displayed on the same webpage, with each Ensembl ID hyperlinked to the Ensembl website for additional information for the gene. 
4. Optional to have the results table exported in .xls format, and Ensembl links are included with the export.

<br><b>*SOURCE OF DATABASE*</b></br>
https://www.proteinatlas.org/download/proteinatlas.json.gz

<br><b>*DEMO OF WEBSITE*</b></br>
http://bfx3.aap.jhu.edu/achia2/final/proteinatlas.html


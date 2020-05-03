// this function executes our search via an AJAX call
function runSearch( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();

    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#gene_search').serialize();
    console.log(frmStr);
    
    $.ajax({
        url: './proteinatlas.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}


// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processJSON( data ) {
    // set the span that lists the match count
    $('#match_count').text( data.match_count );
    
    // this will be used to keep track of row identifiers
    var next_row_num = 1;
    
    // iterate over each match and add a row to the result table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;
        
        // URL link to search for ensembl ID hits
        var ensemblurl = 'https://useast.ensembl.org/Multi/Search/Results?q='
    
        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('tbody');
        
        // add the gene column
        $('<td/>', { "text" : item.gene } ).appendTo('#' + this_row_id);
        
        // add the ensembl column and include url link for Ensembl ID
        // links need to be flanked by + -> e.g +var+ 
        // without flanking, the URL is redirected to the server where files are stored
        // added target"_blank" to open in a new tab
        $('<td/>', { "html" : '<a href="'+ensemblurl+''+item.ensembl_ID+'" target="_blank">' + item.ensembl_ID + '</a>'} ).appendTo('#' + this_row_id);

        // add the gene_description column
        $('<td/>', { "text" : item.gene_description } ).appendTo('#' + this_row_id);

        // add the protein_class column
        $('<td/>', { "text" : item.protein_class } ).appendTo('#' + this_row_id);

    });
    
    // now show the result section that was previously hidden
    $('#results').show();
}



// run our javascript once the page is ready
$(document).ready( function() {

    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        runSearch();
        return false;  // prevents 'normal' form submission
    });

    // Jquery plugin: table2excel export on search data
    $('#exportdata').click( function() {
        $('body').table2excel({
            exclude: ".noExl",
            name: "Worksheet Name",
            //have to include extension in filename to make it work, else file downloads as html instead
            filename: "Human_gene_search.xls",
            fileext: ".xls",
            exclude_links: false
        });
    });
});

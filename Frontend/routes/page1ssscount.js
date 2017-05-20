// Connect string to MySQL
var mysql = require('mysql');
var config = {
          host     : 'g27cis550.c7pt7c7axxui.us-east-1.rds.amazonaws.com',
          user     : 'master',
          password : 'horseman',
          database : 'G27DN',
          port     : 3306
};
/////
// Query the oracle database, and call output_actors on the results
//
// res = HTTP result object sent back to the client
// name = Name to query for
function query_db_page1ssscount(res, user_quer) {
        var connection = mysql.createConnection(config);
        connection.connect();
        connection.query('select count(distinct S.song) as ct from Songs_Tags S join Tags T on S.tag_id = T.id where T.tag in (select T1.tag from Songs_Tags ST join Tags T1 on ST.tag_id = T1.id where ST.song = ?)',[user_quer.trim().toLowerCase()], function(err, rows, fields) {
		if (err) console.log(err);
		else {
			output_page1ssscount(res, user_quer, rows);
		}
	});
        connection.end();
}

// ///
// Given a set of query results, output a table
//
// res = HTTP result object sent back to the client
// name = Name to query for
// results = List object of query results
function output_page1ssscount(res,user_quer,results) {
	res.render('page1ssscount.jade',
		   { title: "Show Count of Similar Songs to: " + user_quer,
		     results: results }
	  );
}

/////
// This is what's called by the main app 
exports.do_page1ssscount = function(req, res){
	query_db_page1ssscount(res,req.query.user_quer);
};

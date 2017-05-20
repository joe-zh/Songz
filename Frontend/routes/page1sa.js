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
function query_db_page1sa(res, user_quer) {
        var connection = mysql.createConnection(config);
        connection.connect();
        connection.query('select * from Artists_Media use index(name) where name = ?', [user_quer.trim().toLowerCase()], function(err, rows, fields) {
		if (err) console.log(err);
		else {
			output_page1sa(res, user_quer, rows);
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
function output_page1sa(res,user_quer,results) {
	res.render('page1sa.jade',
		   { title: "Show Music for Artist: " + user_quer,
		     results: results }
	  );
}

/////
// This is what's called by the main app 
exports.do_page1sa = function(req, res){
	query_db_page1sa(res,req.query.user_quer);
};

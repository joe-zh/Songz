var MongoClient = require('mongodb').MongoClient;

var sanitize = require('mongo-sanitize');


/////
// Query the oracle database, and call output_actors on the results
//
// res = HTTP result object sent back to the client
// name = Name to query for
function query_db_page2sbs(res, user_quer) {
MongoClient.connect("mongodb://master:horseman@cluster0-shard-00-00-uavue.mongodb.net:27017,cluster0-shard-00-01-uavue.mongodb.net:27017,cluster0-shard-00-02-uavue.mongodb.net:27017/test?ssl=true", function(err, db) {
    if(err) { return console.dir(err); }

    var the_sims = db.jsondata.find({'title': sanitize(user_quer).trim().toLowerCase()}, {'similars':1}).toArray();
    var rows = db.jsondata.find({track_id: {$in: the_sims[0].similars}}, {'artist':1, 'title':1});

    output_page2sbs(res,user_quer, rows);
});

}

// ///
// Given a set of query results, output a table
//
// res = HTTP result object sent back to the client
// name = Name to query for
// results = List object of query results
function output_page2sbs(res,user_quer,results) {
	res.render('page2sbs.jade',
		   { title: "Show Music Similar to Song: " + user_quer,
		     results: results }
	  );
}

/////
// This is what's called by the main app 
exports.do_page2sbs = function(req, res){
	query_db_page2sbs(res,req.query.user_quer);
};

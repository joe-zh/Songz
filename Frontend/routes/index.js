
/*
 * GET home page, which is specified in Jade.
 */

exports.do_work = function(req, res){
  res.render('index.jade', { 
	  title: 'Please search for music' 
  });
};

// Query the oracle database, and call output_actors on the results
//
// res = HTTP result object sent back to the client
// name = Name to query for
exports.do_index = function(req,res){
//  query_db_music_index(res);
};

//exports.do_yw = function(req,res){
//  res.render('yw.jade', {});
//};


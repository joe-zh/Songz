/**
 * Simple Homework 2 application for CIS 550
 */

/**
 * Module dependencies.
 */
var express = require('express')
  , routes = require('./routes')
  , index = require('./routes/index')
  , page1 = require('./routes/page1')
  , page2 = require('./routes/page2')
  , page1sa = require('./routes/page1sa')
  , page1ssa = require('./routes/page1ssa')
  , page1sfs = require('./routes/page1sfs')
  , page1salb = require('./routes/page1salb')
  , page1sss = require('./routes/page1sss')
  , page1ssscount = require('./routes/page1ssscount')
  , page2sbt = require('./routes/page2sbt')
  , page2sbs = require('./routes/page2sbs')
  , page2sba = require('./routes/page2sba')
  , page2sbti = require('./routes/page2sbti')
  , http = require('http')
  , path = require('path')
  , stylus = require("stylus")
  , nib = require("nib")
;

// Initialize express
var app = express();
// .. and our app
init_app(app);

// When we get a request for {app}/ we should call routes/index.js
app.get('/', routes.do_work);
app.get('/page1', page1.do_page1);
app.get('/page2', page2.do_page2);
app.get('/page1sa', page1sa.do_page1sa);
app.get('/page1ssa', page1ssa.do_page1ssa);
app.get('/page1sfs', page1sfs.do_page1sfs);
app.get('/page1salb', page1salb.do_page1salb);
app.get('/page1sss', page1sss.do_page1sss);
app.get('/page1ssscount', page1ssscount.do_page1ssscount);
app.get('/page2sbt', page2sbt.do_page2sbt);
app.get('/page2sbs', page2sbs.do_page2sbs);
app.get('/page2sba', page2sba.do_page2sba);
app.get('/page2sbti', page2sbti.do_page2sbti);
 
// Listen on the port we specify
http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});

///////////////////
// This function compiles the stylus CSS files, etc.
function compile(str, path) {
  return stylus(str)
    .set('filename', path)
    .use(nib());
}

//////
// This is app initialization code
function init_app() {
	// all environments
	app.set('port', process.env.PORT || 8080);
	
	// Use Jade to do views
	app.set('views', __dirname + '/views');
	app.set('view engine', 'jade');

	app.use(express.favicon());
	// Set the express logger: log to the console in dev mode
	app.use(express.logger('dev'));
	app.use(express.bodyParser());
	app.use(express.methodOverride());
	app.use(app.router);
	// Use Stylus, which compiles .styl --> CSS
	app.use(stylus.middleware(
	  { src: __dirname + '/public'
	  , compile: compile
	  }
	));
	app.use(express.static(path.join(__dirname, 'public')));

	// development only
	if ('development' == app.get('env')) {
	  app.use(express.errorHandler());
	}

}

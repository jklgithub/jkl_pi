var _express = require('express'),
    _app = _express(),
    _path = require('path'),
    _socketor = require('./routes/socketor');
_app.use(_express.bodyParser());
_app.use(_express.methodOverride());
_app.use(_app.router);
_app.use(logErrors);
_app.use(clientErrorHandler);
_app.use(errorHandler);
_app.use(_express.static(_path.join(__dirname, 'webroot')));

function logErrors(err, req, res, next) {
  console.error(err.stack);
  next(err);
}

function clientErrorHandler(err, req, res, next) {
  if (req.xhr) {
    res.send(500, { error: 'Something blew up!' });
  } else {
    next(err);
  }
}

function errorHandler(err, req, res, next) {
  res.status(500);
  res.render('error', { error: err });
}

_app.get('/feedback', routes);
_app.post('/feedback', routes);

function routes(req, res){
	res.json({head: {code : 'test!!'}});
}

var server = _app.listen(8001, function() {
    console.log('Listening on port %d', server.address().port);
});
_socketor.start(server);

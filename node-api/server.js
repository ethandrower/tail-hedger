


var express = require('express');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true}));
app.use(bodyParser.json());


var MarketData = require('./app/marketdata');


var port = 8080;

var mongoose = require('mongoose');
mongoose.connect('mongodb://writer:drower4@ds157479.mlab.com:57479/marketdata-ethandrower');

//Router


var router = express.Router();


router.get('/', function(req, res) {

	res.json({message: "test home route" });

});


//inserting marketdata

router.route('/marketdata')

  .post(function(req, res){

  	var data = new MarketData;
  	data.productName = req.body.product;
  	data.price = req.body.price;
  	//data.time = req.body.time;

  		data.save(function(err){

  			if(err)
  				res.send(err);

  			res.json({ message: 'added'});
  		});

  });





app.use('/api', router);

app.listen(port);
console.log("running on port " + port);


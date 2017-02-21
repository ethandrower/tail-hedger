

//model for market data


var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var MarketDataSchema = new Schema({
	
	product: String,
	price: Number 
});

module.exports = mongoose.model('MarketData', MarketDataSchema);
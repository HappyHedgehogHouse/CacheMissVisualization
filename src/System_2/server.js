
var express = require('express');
var sql = require('mysql');
var http=require('http');
var app= express();

//app.use(express.logger());
app.get('/a',function (req,res){
	res.send('<h1>hell world!!</h1>');
});



http.createServer(app).listen(52273,function(){
	console.log('Server running at nhttp://127.0.0.1:52273\n');
	
});

/**
 * New node file
 */
var  http = require('http');
var express = require('express');
var sql = require('mysql');
var fs = require('fs');
var app= express();
var router=express.Router();
app.use(express.static('public'));
app.use();

//라우트 합니다.
app.all('/a',function(request,response){
	response.send('<h1>Page A</h1>');
});
app.all('/b',function(request,response){
	response.send('<h1>Page B</h1>');
});
app.all('/c',function(request,response){
	response.send('<h1>Page C</h1>');
});



http.createServer(app).listen(52273, function (){
	console.log('Server Running at http://127.0.0.1:52273');
});
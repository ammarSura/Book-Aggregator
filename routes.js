const express = require('express');
const path = require('path');
const app = express();
var results = false;
const getAllResults = require("./x");
const {PythonShell} = require('python-shell');



app.use(express.static(path.join(__dirname)))


app.set('view engine', 'ejs');


app.get('/', function(req, res) {
  res.render('pages/index');
});

app.get('/home', function(req, res) {
    res.render('pages/index');
  });

app.get('/results/:term', function(req, res) {
    console.log(req.params)
    res.render('pages/results');
  });

app.get('/getResults/:term', async (req, res) => {
    const params = req.params;
    
  
    await getAllResults(params.term).then( (result) => {
        console.log('all results1', result);
        
        res.json(result);
        
    }, (error) => {
        console.log('err', error);
       
        res.json(error);
    });
    
});

const port = process.env.PORT || 3000;
app.listen(port);
console.log('Server is listening on port: ' + port);
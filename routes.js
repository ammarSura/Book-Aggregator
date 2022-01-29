const express = require('express');
const path = require('path');
const app = express();
const getAllResults = require("./x");

// console.log(getAllResults("asimov")[0])

app.use(express.static(path.join(__dirname)))


// set the view engine to ejs
app.set('view engine', 'ejs');

// use res.render to load up an ejs view file

// index page
app.get('/', function(req, res) {
  res.render('pages/index');
});

// about page
app.get('/getter/:term', async (req, res) => {
    const params = req.params;

    getAllResults(params).then( (result) => {
        console.log('res', result);
        results = result;
        res.json(result);
    }, (error) => {
        console.log('err', error);
        results = error;
        res.json(error);
    });

    res.status(202);

    // res.json([{
    //     title: 'Is Our Planet Warming Up-Isaac Asimov',
    //     price: '310',
    //     url: 'https://www.usedbooksfactory.com/buy-second-hand-old-books/detail/is-our-planet-warming-up-isaac-asimov-not-availableedition-9780431076409?book_id=54545'
    //   }])
    
    
    
});

const port = process.env.PORT || 3000;
app.listen(port);
console.log('Server is listening on port:' + port);
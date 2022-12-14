const express = require('express');
const app = express();
const cors = require('cors');
// let bodyParser = require('body-parser');
let fs = require('fs');
let dateT = require('node-datetime');

const { format } = require('path');
let dt = dateT.create();
let frmt = dt.format('Y-m-d H:M:S')

const port = 5000;
// app.use(bodyParser());
app.use(express.urlencoded({extended:true}));
app.use(express.json());

app.set('trust proxy', true);
app.use(cors());
app.set('view engine', 'ejs');

app.get('/', (req, res)=>{
    const ip = req.ip;
    res.render("index");
})
app.post('/', (req, res)=>{
    console.log(frmt+"  ->  "+req.body.ip)
    fs.appendFile('records.txt', frmt+"  ->  "+req.body.ip +"\n", (err)=>{
        if(err) throw err;
        console.log('Saved!');
    })
})

app.listen(port, ()=>{
    console.log('server running on port: '+port);
})
'use strict';

const express = require('express');
const body_parser = require('body-parser');
const path = require('path');
const fs = require('fs');

// Constants
const PORT = 3000;
const HOST = '0.0.0.0';

// App
const app = express();

// Home page
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/hello-world.html'));
});

app.get('/readiness', function(req, res) {
    res.sendStatus(200);
});

app.get('/liveness', function(req, res) {
    res.sendStatus(200);
});

app.listen(PORT, HOST);

console.log(`Running on http://${HOST}:${PORT}`);
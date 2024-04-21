#!/usr/bin/node
// script for querying star wars api
const request = require("request");

const args = process.argv
request('https://swapi-api.alx-tools.com/api/films/'+args[2],
    function (error, response, body) {
        const chars = JSON.parse(body).characters;
        chars.forEach(charUrl => {
            request(charUrl, (error, response, body) => {
                const b = JSON.parse(body);
                console.log(b.name);
            });
        });
});

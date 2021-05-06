#!/usr/bin/node

const argv = process.argv.slice(2);
const url = argv[0];
const filename = argv[1];

const fs = require('fs');
const request = require('request');
const data = {};
let users;

request(url, function (error, response, body) {
  users = JSON.parse(body);

  for (let i = 0; i < users.length; i++) {
    if (users[i].completed === true) {
      if (data[users[i].userId]) {
        data[users[i].userId] += 1;
      } else {
        data[users[i].userId] = 1;
      }
    }
  }
  console.log(data);
});

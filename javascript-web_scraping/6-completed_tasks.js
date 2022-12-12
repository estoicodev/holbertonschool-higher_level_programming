#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.error('error:', err);
  }
  const data = JSON.parse(body);
  const result = {};
  for (const task of data) {
    if (task.completed) {
      const userId = String(task.userId);
      if (Object.keys(result).includes(userId)) {
        result[userId] = result[userId] + 1;
      } else {
        result[userId] = 1;
      }
    }
  }
  console.log(result);
});

#!/usr/bin/node
const axios = require('axios');

const usersCompletedTasks = {};
axios
  .get(process.argv[2])
  .then(function (response) {
    const data = response.data;
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        if (data[i].userId in usersCompletedTasks) {
          const currentCompletedTasks = usersCompletedTasks[data[i].userId];
          usersCompletedTasks[data[i].userId] = currentCompletedTasks + 1;
        } else {
          usersCompletedTasks[data[i].userId] = 1;
        }
      }
    }
    console.log(usersCompletedTasks);
  })
  .catch(function (err) {
    if (err.response) {
      console.log(`code: ${err.response.status}`);
    }
  });

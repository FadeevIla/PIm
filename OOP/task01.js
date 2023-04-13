const _ = require('lodash');
const fs = require('fs');
const users = JSON.parse(fs.readFileSync('users.json', 'utf8'));

const resultArr = _(users)
  .filter(item => item.address.geo.lat < 0)
  .map(item => ({ username: item.username, city: item.address.city }))
  .orderBy('city', 'desc')
  .value();

_.each(resultArr, item => {
  console.log(item);
});
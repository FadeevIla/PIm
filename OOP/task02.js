const _ = require('lodash');
const fs = require('fs');
const clients = JSON.parse(fs.readFileSync('clients.json', 'utf8'));

const resultArr = _(clients.clients)
  .filter({ 'address.city': 'Кунгур' })
  .orderBy(['gender', 'age', 'name'], ['asc', 'desc', 'asc'])
  .value();

_.each(resultArr, item => {
  console.log(item);
});
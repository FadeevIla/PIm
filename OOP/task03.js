const _ = require('lodash');
const fs = require('fs');
const colors = JSON.parse(fs.readFileSync('colors.json', 'utf8'));

const resultArr = _(colors)
  .map(item => _.keys(item)[0])
  .filter(item => item.length < 6)
  .sortBy()
  .value();

_.each(resultArr, item => {
  console.log(item);
});
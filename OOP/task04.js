const _ = require('lodash');
const fs = require('fs');
const colors = JSON.parse(fs.readFileSync('colors.json', 'utf8'));

const resultArr = _(colors)
  .map(item => _.zipObject(['color', 'rgb'], [_.keys(item)[0], _.slice(_.values(item)[0], 0, 3)]))
  .orderBy('color')
  .value();

_.each(resultArr, item => {
  console.log(item);
});
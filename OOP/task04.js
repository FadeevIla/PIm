const _ = require('lodash');
const fs = require('fs');
const colors = JSON.parse(fs.readFileSync('colors.json', 'utf8'));

var resultArr = colors

resultArr = _.map(colors, function(item){
    return _.zipObject(['color', 'rgb'], [_.keys(item)[0], _.slice(_.values(item)[0], 0, 3)]);
})

resultArr = _.orderBy(resultArr, 'color')

console.log(resultArr)

_.each(resultArr, function(item){
    console.log(item)
})
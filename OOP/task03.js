const _ = require('lodash');
const fs = require('fs');
const colors = JSON.parse(fs.readFileSync('colors.json', 'utf8'));

var resultArr = _.map(colors, function(item){
    return _.keys(item)[0]
})

resultArr = _.filter(resultArr, function(item){
    return item.length < 6
})

resultArr = _.sortBy(resultArr)

console.log(resultArr)

_.each(resultArr, function(item){
    console.log(item)
})
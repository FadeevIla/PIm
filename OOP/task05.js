const _ = require('lodash');
const data = require("./data.js");
const colors = data.colors
const argb = data.argb

function rgbToHex(item) {
    const r = item[0]
    const g = item[1]
    const b = item[2]
    return "#" + (1 << 24 | r << 16 | g << 8 | b).toString(16).slice(1);
  }

resultArr = _.zip(colors, argb)

resultArr = _.map(resultArr, function(item){
    return {color: item[0], hex_name: rgbToHex(item[1])}
})

resultArr = _.orderBy(resultArr, 'color')

console.log(resultArr)

_.each(resultArr, function(item){
    console.log(item)
})


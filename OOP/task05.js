const _ = require('lodash');
const data = require("./data.js");
const colors = data.colors;
const argb = data.argb;

function rgbToHex(item) {
  const [r, g, b] = item;
  return "#" + (1 << 24 | r << 16 | g << 8 | b).toString(16).slice(1);
}

const resultArr = _(colors)
  .zip(argb)
  .map(item => ({ color: item[0], hex_name: rgbToHex(item[1]) }))
  .orderBy('color')
  .value();

_.each(resultArr, item => {
  console.log(item);
});
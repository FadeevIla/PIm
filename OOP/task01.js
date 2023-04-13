const _ = require('lodash');
const fs = require('fs');
const users = JSON.parse(fs.readFileSync('users.json', 'utf8'));

var resultArr = _.filter(users, function(item){
    return item.address.geo.lat < 0
})

resultArr = _.map(resultArr, function(item){
    return {username: item.username, city: item.address.city}
})
 
resultArr = _.orderBy(resultArr, 'city', 'desc')

console.log(resultArr)

_.each(resultArr, function(item){
    console.log(item)
})
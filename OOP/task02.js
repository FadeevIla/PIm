const _ = require('lodash');
const fs = require('fs');
const clients = JSON.parse(fs.readFileSync('clients.json', 'utf8'));

var resultArr = clients.clients

resultArr = _.filter(resultArr, function(item){
    return item.address.city === 'Кунгур'
})

resultArr = _.orderBy(resultArr, ['gender', 'age', 'name'], ['asc', 'desc', 'asc'])

console.log(resultArr)

_.each(resultArr, function(item){
    console.log(item)
})
// let map = new Map

// map.set(10,20)
// map.set('key1',20)

// for(let i of map){
//     console.log(i)
// }

// console.log(map.get(10))
// console.log(map.has(10))
// console.log(map.size)












// let set = new Set()

// set.add(10)
// set.add(10)
// set.add('duvindu')
// console.log(set)


// console.log(set.size)
// console.log(set.has(10))


// for(let i of set){
//     console.log(i)
// }


fetch('https://fakestoreapi.com/products')
.then(result => result.json())
.then(data => f1(data))


function f1(values){
    for(let i=0; i<values.length; i++){
        console.log(values[i])
    }
}
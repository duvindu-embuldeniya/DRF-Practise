let arr1 = [10,20,30,40,50]
let obj1 = {val1:10, val2:20, val3:30, val4:40, val5:50}


//destructuring
let arr2 = [...arr1]

//rest parameter
let [a,,c,...rest] = arr1
console.log(rest)



//destructuring
let obj2 ={...obj1}

//can use alias
//if not alias key should same
//can't use commas to skip values 
let {val1:aa,val2,...restt} = obj1
console.log(val2)
// promises are solution for callback hell.........../////////////////////////////////////////


//meth1.........................................../////////////////////////////////////////////
// const myPromsie = new Promise((resolve,reject)=>{
//     setTimeout(()=>{
//         const state = true
//         if(state){
//             resolve("Done")
//         }
//         else{
//             reject("Didn't")
//         }
//     },1000)
// })


// myPromsie.then((accept)=>{
//     console.log("Done")
// }).catch((exception)=>{
//     console.log(exception)
// }).finally(()=>{
//     console.log("End..!")
// })



//method2...........................................////////////////////////////////////////////
// function eat(){
//     return new Promise((resolve,reject)=>{
//         setTimeout(() => {
//             const state = true
//             if(state){
//                 resolve("Ate")
//             }
//             else{
//                 reject("Didn't eat")
//             }
//         }, 1000);
//     })
// }


// function wash(){
//     return new Promise((resolve,reject)=>{
//         setTimeout(()=>{
//             const state = true
//             if(state){
//                 resolve("Washed")
//             }
//             else{
//                 reject("Didn't wash")
//             }
//         },1500)
//     })
// }


// function sleep(){
//     return new Promise((resolve,reject)=>{
//         setTimeout(()=>{
//             const state = false
//             if(state){
//                 resolve("Slept")
//             }
//             else{
//                 reject("Didn't sleep")
//             }
//         },2000)
//     })
// }


// eat().then((accept)=>{
//     console.log(accept)
//     return wash()
// }).then((accept)=>{
//     console.log(accept)
//     return sleep()
// }).then((accept)=>{
//     console.log(accept)
//     console.log("All correct..!")
// }).catch((exception)=>{
//     console.log(exception)
//     console.log("Some error..!")
// }).finally(()=>{
//     console.log("End..!")
// })



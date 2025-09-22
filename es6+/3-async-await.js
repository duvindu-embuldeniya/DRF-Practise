
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



// async function run(){
//     try{
//         console.log(await eat())
//         console.log(await wash())
//         console.log(await sleep())
//         console.log("All Done")
//     }
//     catch(exception){
//         console.log(exception)
//         console.log("Some error..!")
//     }
// }


// run()
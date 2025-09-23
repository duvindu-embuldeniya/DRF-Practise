// let projects = ()=>{
//     fetch('http://localhost:8000/api/blogs/')
//     .then(data => data.json())
//     .then(response => {
//         // console.log(response)
//         build_projects(response)
//     })
// }


// let wrapper = document.getElementById('blogs-wrapper')


// let build_projects = (data)=>{
//     for(let blog of data){
//         wrapper.innerHTML += `
//             <div>
//                 <p>Title :- ${blog.title}</p>
//             <div>
//         `
//     }
// }


// projects()

let wrapper = document.getElementById('blogs-wrapper')


let blogs = ()=>{
    fetch('http://localhost:8000/api/blogs/')
    .then(result => result.json())
    .then(data => display_blogs(data))
}


let display_blogs = (data)=>{
    for(let blog of data){
        // console.log(blog)
        wrapper.innerHTML += `
            <p> Title :- ${blog.title} </p>
            <p> Description :- ${blog.description} </p>
            <p> Total Votes :- ${blog.vote_total} </p>
            <p> Vote percentage :- ${blog.vote_percentage} </p>
            <button type='submit' id='up'> Up </button>
            <button type='submit' id='down'> Down </button>
            <hr>
        `
    }
}


blogs()
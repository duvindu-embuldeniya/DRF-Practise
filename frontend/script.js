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
            <button type='submit' class='btn' data-vote='up' data-blog='${blog.id}'> Up </button>
            <button type='submit' class='btn' data-vote='down' data-blog='${blog.id}'> Down </button>
            <hr>
        `
    }
    addVoteCount()

}


blogs()




let addVoteCount = ()=>{
    let buttons = document.getElementsByClassName('btn')
    // console.log(buttons)
    for(let i = 0; i < buttons.length; i++){
        buttons[i].addEventListener('click', (e)=>{
            // console.log("Button Was Clicked:", i)
            let value = e.currentTarget.dataset.vote
            let blog = e.currentTarget.dataset.blog
            console.log(blog,value)
        })
    }
}

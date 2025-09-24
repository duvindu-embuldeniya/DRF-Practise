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
blogs()



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



let addVoteCount = ()=>{
    let buttons = document.getElementsByClassName('btn')
    // console.log(buttons)
    for(let i = 0; i < buttons.length; i++){
        buttons[i].addEventListener('click', (e)=>{
            let value = e.currentTarget.dataset.vote
            let blog = e.currentTarget.dataset.blog

            // console.log(value,blog)

            fetch(`http://localhost:8000/api/blog/${blog}/`,{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4NzY4OTI4LCJpYXQiOjE3NTg2ODI1MjgsImp0aSI6IjBlZDkyZDAyNDQyNzRhYjBhNjQ4ZmNlNzI2YzkwMmMyIiwidXNlcl9pZCI6IjEifQ.I16IJuIcSoAhDuUopPBE-tBovaFm21sro8xB9ohDdiM'
                },
                body:JSON.stringify({"type": `${value}`})
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
            })
        })
    }
}

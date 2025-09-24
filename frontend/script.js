let wrapper = document.getElementById('blogs-wrapper')


let blogs = ()=>{
    fetch('http://localhost:8000/api/blogs/')
    .then(result => result.json())
    .then(data => display_blogs(data))
}



let display_blogs = (data)=>{
    wrapper.innerHTML = ''
    for(let blog of data){
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




let addVoteCount = () => {
    let btns = document.getElementsByClassName('btn')
    for(let i=0; i<btns.length; i++){
        btns[i].addEventListener('click', (e)=>{
            let vote = e.currentTarget.dataset.vote
            let blog = e.currentTarget.dataset.blog
            // console.log(vote,blog)
            
            // let token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4NzY4OTI4LCJpYXQiOjE3NTg2ODI1MjgsImp0aSI6IjBlZDkyZDAyNDQyNzRhYjBhNjQ4ZmNlNzI2YzkwMmMyIiwidXNlcl9pZCI6IjEifQ.I16IJuIcSoAhDuUopPBE-tBovaFm21sro8xB9ohDdiM'
            let token = localStorage.getItem('token')
            console.log(token)
            fetch(`http://localhost:8000/api/blog/${blog}/`,{
                method:'POST',
                headers:{
                    'Content-Type': 'application/json',
                    'Authorization':`Bearer ${token}`
                },
                body:JSON.stringify({"type": `${vote}`})
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                blogs()
            })
            // blogs()
        })
    }
}

blogs()

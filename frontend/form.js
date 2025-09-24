let form = document.getElementById('form')

form.addEventListener('submit', (e)=>{
    e.preventDefault()
    // console.log(999)

    let formData = {
        'username':form.username.value,
        'password':form.password.value
    }

    // console.log(formData)
    fetch('http://localhost:8000/api/users/token/', {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(formData)
    })
    .then(result => result.json())
    .then(data => {
        if(data.access){
            localStorage.setItem('token',data.access)
            window.location = 'file:///c%3A/Users/duvin/Desktop/drf/frontend/index.html'
        }
        else{
            alert("Credentials doesn't match..!")
        }
    })
})
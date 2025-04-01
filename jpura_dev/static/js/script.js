let alertt = document.querySelector('.alert')
let alert_btn = document.querySelector('.alert__close')

setTimeout(function(){
    alertt.style.display = 'none';
},4000)


// alert_btn.addEventListner('click', func)

// function func(){
//     alertt.style.display = 'none'
// } 

let form = document.querySelector('.form')
let pages = document.getElementsByClassName('page')

for(let i=0; i < pages.length; i++){
    pages[i].addEventListener('click', func)

    function func(e){
        e.preventDefault()
        console.log('xxx')

        let page = this.dataset.page

        form.innerHTML += `<input value=${page} name='page' hidden>`

        form.submit()
    }
}






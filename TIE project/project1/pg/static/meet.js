
var username = document.getElementById('username')
var password = document.getElementById('password')
var form = document.getElementById('form')
var errorElement = document.getElementById('error')

form.addEventListener('submit',(e)=>{
    let messages = []
    if(username.value === ''||username.value==null){
        messages.push('Please enter the name')
    }
    if(password.value.length <= 6){
        messages.push('password must be longer than 6 characters')
    }
    if(password.value === ''||password.value==null){
        messages.push('Please enter the password')
    }
    if(messages.length>0){
        e.preventDefault()
        errorElement.innerText = messages.join(',')
        
    }
})
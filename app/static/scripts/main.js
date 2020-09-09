function registerSubmit(){
    var email = document.getElementById('form-email').value;
    var pw = document.getElementById('form-password').value
    var emailError = document.getElementById('email-error')
    var passwordError = document.getElementById('password-error')
    var form = document.getElementById('register-form')
    
    if(validateEmail(email)){
        emailError.style.display = 'none';
    }
    else{
        console.log('email error')
        emailError.style.display = 'block';
        return false;
    }
    if(pw.length < 8){
        passwordError.style.display = 'block';
        return false;
    }
    else{
        form.submit()
    }
}

function validateEmail(email) 
    {
        var re = /\S+@\S+\.\S+/;
        return re.test(email);
    }

function inputElement(){
    document.getElementsByClassName('add-item')[0].innerHTML = "<form method=\"POST\" action=\"\/add\/item\">            <ul>                <li>                    <input id=\"form-input\" type=\"text\" placeholder=\"Place my phone on charge...\" required>                <\/li>                <li>                    <svg onclick=\"addItem()\" id=\"svg-tick\" width=\"20px\" height=\"20px\" class=\"w-6 h-6\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\" xmlns=\"http:\/\/www.w3.org\/2000\/svg\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 13l4 4L19 7\"><\/path><\/svg>                <\/li>            <\/ul>                        <\/form>"
    document.getElementById('svg-plus').style.display = 'none';
    document.getElementById('svg-close').style.display = 'block';
}

function closeInput(){
    document.getElementsByClassName('add-item')[0].innerHTML = ''
    document.getElementById('svg-plus').style.display = 'block';
    document.getElementById('svg-close').style.display = 'none';

}

function addItem(){
    
    var input = document.getElementById('form-input').value
    fetch(`/add/${input}`)
    .then(response => response.text())
    .then((response) => {
        var x =  `<input type=\"hidden\" value=\"${response}\">`;
        document.getElementsByClassName('item-desc')[0].innerHTML += `<ul id=\"item-${response}\"> <li> <p>${input}<\/p> <\/li> <li> <div class=\"list-icons\"> <svg onclick=\"deleteItem(${response})\" id=\"svg-trash\" width=\"20px\" height=\"20px\" class=\"w-6 h-6\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\" xmlns=\"http:\/\/www.w3.org\/2000\/svg\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16\"><\/path><\/svg> <\/div> <\/li> <\/ul>`
    })
    
    document.getElementsByClassName('add-item')[0].innerHTML = '';
    document.getElementById('svg-plus').style.display = 'block';
    document.getElementById('svg-close').style.display = 'none';
}

function deleteItem(item){
    fetch(`/delete/${item}`);
    document.getElementById(`item-${item}`).remove();

}
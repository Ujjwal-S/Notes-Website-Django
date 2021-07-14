let container = document.getElementsByClassName("my-hero-container")[0];

    let register_palat = document.getElementById("register-palat");
    let login_palat = document.getElementById("login-palat");

    register_palat.addEventListener("click", ()=>{
        container.style.transform = "rotateY(180deg)";
    })

    login_palat.addEventListener("click", ()=>{
        container.style.transform = "rotateY(0deg)";
    })

// PASSWORD

let passwordValid = false;

let p1 = document.getElementsByName("password1")[0]
let p1Error = document.getElementsByClassName("my-error")[1]
let p2 = document.getElementsByName("password2")[0]
let p2Error = document.getElementsByClassName("my-error")[2]


p1.addEventListener("input", ()=>{
    if (p1.value.length < 8){
        p1Error.classList.remove("invisible")
        passwordValid = false;
    }
    else{
        p1Error.classList.add("invisible")
        passwordValid = true;
    }
    checkOther();
})
p2.addEventListener("input", ()=>{
    
    if (p1.value === p2.value){
        p2Error.classList.add("invisible")
        passwordValid = true;
    }
    else{
        p2Error.classList.remove("invisible")
        passwordValid = false;
    }
    checkOther();
})

function checkOther(){
    if (p1.value === p2.value){
        p2Error.classList.add("invisible")
        passwordValid = true;
    }
    else{
        p2Error.classList.remove("invisible")
        passwordValid = false;
    }
}

// Check Email

let emailError = document.getElementsByClassName("my-error")[0]
let emailInput = document.getElementById("Remail")

function isEmailValid(E_Mail){
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(E_Mail);
}

async function checkEmail(){
    let response = await fetch(`/checkemail/${emailInput.value}`)
    let json = await response.json()
    return json.emailExists
}

emailInput.addEventListener("input", ()=>{
    emailError.classList.add("invisible")
})

// Form 

async function isValid(){
    form = document.getElementsByTagName("form")[1];

    if (!isEmailValid(emailInput.value)){
        emailError.innerHTML = "**Enter valid email.";
        emailError.classList.remove("invisible")
    }
    else{

        let emailExists = await checkEmail().then(data => data);
        
        let cl1 = document.getElementById("inp-pass-e1").classList
        let cl2 = document.getElementById("inp-pass-e2").classList
        let has_invisible1 = false
        let has_invisible2 = false

        for (let i of cl1){
            if (i == 'invisible'){
                has_invisible1 = true
            }
        }

        for (let i of cl2){
            if (i == 'invisible'){
                has_invisible2 = true
            }
        }

        if (has_invisible1 && has_invisible2){ passwordValid = true } else{ passwordValid = false}


        if (!emailExists && isEmailValid(emailInput.value) && passwordValid){
            form.submit()
        }
        else if(emailExists){
            emailError.innerHTML = "**Account already exist.";
            emailError.classList.remove("invisible")
        }
    }
}



// LOGIN

let peeche_form = document.getElementsByTagName("form")[2];
let login_error = document.getElementById("login_error");


peeche_form.addEventListener('input', ()=>{
    login_error.classList.add("d-none")
}) 

if (document.referrer === `${domain_url}accounts/login/`){
    login_error.classList.remove("d-none")
}

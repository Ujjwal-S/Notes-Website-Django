let passwordValid = false;

let p1 = document.getElementsByName("password1")[0]
let p1Error = document.getElementsByClassName("my-error")[0]
let p2 = document.getElementsByName("password2")[0]
let p2Error = document.getElementsByClassName("my-error")[1]
let prf = document.getElementById("prf")


document.getElementById("inp-pass").addEventListener("input", ()=>{
    if (p1.value.length < 8){

        passwordValid = false
        p1Error.classList.remove("invisible")
    }
    else{
        passwordValid = true
        p1Error.classList.add("invisible")
    }

    if (p1.value !== p2.value){
        passwordValid = false
        p2Error.classList.remove("invisible")
    }
    else{
        p2Error.classList.add("invisible")
        if (p1.value.length < 8){
            passwordValid = false
            p1Error.classList.remove("invisible")
        }
        else{
            passwordValid = true
            p1Error.classList.add("invisible")
        }
    }

})



prf.addEventListener("submit", (event)=>{
    event.preventDefault()
    if (passwordValid){
        console.log(" mai aaya")
        prf.submit()
    }
})

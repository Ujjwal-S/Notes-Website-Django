(function () {
    'use strict'

    document.querySelector('#navbarSideCollapse').addEventListener('click', function () {
        document.querySelector('.offcanvas-collapse').classList.toggle('open')
    })
})()


if (is_auth === "False"){
    let navbar_nav = document.getElementsByClassName("navbar-nav")[0];
    let navbar_nav_children = Array(...navbar_nav.children)
    navbar_nav_children.pop()
    for (let child of navbar_nav_children){
        child.children[0].classList.add("disabled");
        child.addEventListener("click", (element)=>{
            alert("Login To Continue.");
        })
    }

    let signup_login_btn = document.getElementById("signup-login-btn")

    if (window.location.href === domain_url){  // TODO isko sahi kar dena
        signup_login_btn.onclick = "document.getElementById('hero').scrollIntoView(true)"
    }
    else{
        signup_login_btn.href=home_page_url
    }
}


const search_form = document.getElementById("search_form")
const search_input = document.getElementById("search_input")
const search_input_btn = document.getElementById("search_input_btn")

search_input_btn.addEventListener("click", ()=>{
    search_input.value = search_input.value.trim()
    if (search_input.value){
        search_form.submit()
    }
})


let nav_link_notes = document.getElementById("nav-link-notes")
let nav_link_kmu = document.getElementById("nav-link-kmu")

function handelNavbarLinks(ele){
    if (window.location.href == domain_url){  // TODO isko sahi kar dena
        if (ele == 'Notes'){
            document.getElementById('Notes').scrollIntoView(true);
        }
        else if (ele == 'keepMeUpdated'){
            document.getElementById('keepMeUpdated').scrollIntoView(true);
        }
    }
    else{
        sessionStorage.setItem("moveToEl", `${ele}`);
        window.location.href="/"
    }
}


if (sessionStorage.getItem("moveToEl")){
    document.getElementById(`${sessionStorage.getItem("moveToEl")}`).scrollIntoView(true);
    sessionStorage.removeItem("moveToEl")
}
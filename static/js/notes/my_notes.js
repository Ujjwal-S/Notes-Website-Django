make_btn_small()

window.addEventListener('resize', make_btn_small);

function make_btn_small(){

    let view_btns = Array(...document.getElementsByClassName("btn-info"))

    if (document.body.clientWidth <= 600){
        view_btns.forEach(element => {
            element.classList.add("btn-sm")
        });
    }
    else{
        view_btns.forEach(element => {
            element.classList.remove("btn-sm")
        });
    }
}
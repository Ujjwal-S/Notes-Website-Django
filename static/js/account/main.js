
function kashti(){
    document.getElementById('kashti').innerHTML = ''
    let message_width = document.getElementsByClassName("message")[0].clientWidth;

    for(let i=0; i<Math.floor(message_width/22); ++i){
        document.getElementById('kashti').append("⛵")
    }
}
kashti()
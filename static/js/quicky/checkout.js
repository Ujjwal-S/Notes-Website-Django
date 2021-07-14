let points_checker = document.getElementById("flexSwitchCheckDefault");

let user_points = document.getElementById("user_points");
let original_user_points = parseInt(user_points.innerText);

let payable_amount = document.getElementById("payable-amount");
let original_payable_amount = parseInt(payable_amount.innerText.slice(2));

let payBtn = document.getElementById("payBtn")

points_checker.addEventListener("click", ()=>{

    if(points_checker.checked){

        if(parseInt(user_points.innerText) <= parseInt(payable_amount.innerText.slice(2))){
            payable_amount.innerHTML = `&#x20b9;&nbsp;${parseInt(payable_amount.innerText.slice(2)) - parseInt(user_points.innerText)}`
            user_points.innerText = "0";

            if (payable_amount.innerText.slice(2) == 0) changePayToMyNotes()
            else changeMyNotesToPay()
        }
        else{
            user_points.innerHTML = `${parseInt(user_points.innerText) - parseInt(payable_amount.innerText.slice(2))}`
            payable_amount.innerHTML = `&#x20b9;&nbsp;0`

            if (payable_amount.innerText.slice(2) == 0) changePayToMyNotes()
            else changeMyNotesToPay()
        }
    }

    else{
        user_points.innerHTML = original_user_points
        payable_amount.innerHTML = `&#x20b9;&nbsp;${original_payable_amount}`

        if (payable_amount.innerText.slice(2) == 0) changePayToMyNotes()
        else changeMyNotesToPay()
    }

})

function changePayToMyNotes(){
    payBtn.innerText = 'Add to My Notes'
}
function changeMyNotesToPay(){
    payBtn.innerText = 'Pay Amount'
}


if (orderItemsCount == 0){
    points_checker.disabled = true
    payBtn.disabled = true
}


let q_icon = document.getElementById("more-info-question-icon");

q_icon.addEventListener("click", ()=> {
    sendToast("https://emojiguide.com/wp-content/uploads/platform/google/44074.png", "<a href='#' class='text-dark'><b>Click here</b></a><span class='text-secondary'> to know more</span>")
})


    // TOAST
    let count_of_toast = 0;

    function sendToast(emojiUrl, message){

      let toast_container = document.getElementById("toast-container")


      toast_container.insertAdjacentHTML("beforeend", 
      `<div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-${count_of_toast}">
            <div class="toast-header">
              <img src="${domain_url}static/images/favicon2.png" class="rounded me-2" width="16px" height="16px" alt="The Quicky Science Icon"> 
              <strong class="me-auto">The Quicky Science</strong>
              <small style="margin-right: 15px;" class="text-muted"><img src="${emojiUrl}" class="rounded me-2" alt="" width="25px" height="25px"></small>
              <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body" style="background: white;">
              ${message}
            </div>
        </div>`
      )
      toastu(count_of_toast)
      ++ count_of_toast
    }

    function toastu(count_of_toast){

      var toastHTMLElement = document.getElementById(`toast-${count_of_toast}`)

      var toastElement = new bootstrap.Toast(toastHTMLElement, {
        delay : 5000
      })

      toastElement.show()
      
}

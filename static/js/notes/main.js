let accordions = document.getElementsByClassName("accordion-button");

for (let accordion of accordions) {
  accordion.style.backgroundColor = "white";
}


if (is_auth === "True") {
  let cart_btns = Array(...document.getElementsByClassName("cart-btn"))      // for firefox  https://bugzilla.mozilla.org/show_bug.cgi?id=654072
    cart_btns.forEach(element => {
      element.disabled = true
    })

  // get my notes

  fetch(`/notes/get_my_notes/`)

    .then(data => data.json())

    .then((data) => {

      // first set all the btns to cart svg

      cart_btns.forEach(element =>{
        element.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cart2" viewBox="0 0 16 16">
                            <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l1.25 5h8.22l1.25-5H3.14zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"/>
                            </svg>`

      })

      // change cart svg of notes which are bought

      let notes_id_list = data.my_notes_ids;
      for (let note_id of notes_id_list) {

        if (document.getElementById(note_id)) {

          let c_btn = document.getElementById(`button-${note_id}`);

          c_btn.dataset.bought = 'true';

          c_btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye" viewBox="0 0 16 16">
              <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"/>
              <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>
              </svg>`

          let c_btn_link_id = c_btn.parentElement.id;
          c_btn.parentElement.href = `/notes/view_notes/${c_btn_link_id}`;

        }
      }


      // once this data is arrived ,,,, then
      // enable all btns
        let add_to_cart_btn = Array(...document.getElementsByClassName("add-to-cart"))
            add_to_cart_btn.forEach(element =>{
              element.disabled = false
        })

    })


    .catch((e) => console.log("Erorr", e))



  // add to cart


      let add_to_cart_btns = Array(...document.getElementsByClassName("add-to-cart"))

      add_to_cart_btns.forEach(element => {
        element.addEventListener("click", () => {

          if (!(element.dataset.bought == 'true')) {
            let id_s = element.dataset.id_s

            send_data_to_cart(id_s)

          }
        })
      });


      function send_data_to_cart(id_s){
          fetch('/my_cart_info/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                'notes-id': `${id_s}`
              })
          })
          .then(response => response.json())
          .then(data => {
            if (data.added == true){
              sendToast("https://emojiguide.com/wp-content/uploads/platform/google/44074.png", "Item was Succesfully added to Cart.")
              document.getElementById("latest_cart_items_count").innerHTML = data.latest_count
            }
            else{
              sendToast("https://emojiguide.com/wp-content/uploads/2020/11/Smiling-Face-With-Sunglasses.png", "Item is already in Cart.")
              document.getElementById("latest_cart_items_count").innerHTML = data.latest_count
            }
          })
      }
    }


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

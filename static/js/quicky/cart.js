

make_btn_small()

window.addEventListener('resize', make_btn_small);

function make_btn_small(){

    let remove_btns = Array(...document.getElementsByClassName("btn-danger"))

    if (document.body.clientWidth <= 600){
        remove_btns.forEach(element => {
            element.classList.add("btn-sm")
        });
    }
    else{
        remove_btns.forEach(element => {
            element.classList.remove("btn-sm")
        });
    }
}

let my_remove_btns = Array(...document.getElementsByClassName("my-remove-btn"))

my_remove_btns.forEach(element => {
    element.addEventListener("click", removeThisItem)
})

function removeThisItem(){

    fetch('/remove_item/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'remove_order_item_id': `${this.dataset.table_cell_id}`
        })
    })
    
    .then(response => response.json())

    .then((data) => {
        if(data.removed == true){
            document.getElementById(`table_cell_${this.dataset.table_cell_id}`).remove()
            if(document.getElementsByClassName("my-remove-btn").length == 0){
                document.getElementsByClassName("container")[0].innerHTML = `<h1 style="text-align: center;">Cart is Empty</h1>`
            }
            document.getElementById("latest_cart_items_count").innerHTML = data.latest_count
        }
        else(() => alert("Try Again"))    
    }
    )

}

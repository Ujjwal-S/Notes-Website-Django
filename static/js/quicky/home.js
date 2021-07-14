// PCB TEXT

const pcb = document.getElementById("animated_text");

observer = new IntersectionObserver((entry) => {
    console.log(entry);
    if (entry[0].isIntersecting){
        pcb.classList.add("animation");
        observer.unobserve(entry[0].target);
    }
})

observer.observe(pcb)

// Subsbcribe

let updates_email = document.getElementById("updates-email")
let updates_status = document.getElementById("update-status")

updates_email.addEventListener("input", ()=>{
    updates_status.classList.add("d-none");
})

let updates_form = document.getElementById("updates-form")

updates_form.addEventListener("submit", (e)=>
    {
        e.preventDefault()

        let update_status_message = document.getElementById("update-status-message")
        fetch(`addsubscriber/${updates_email.value}`)
        .then(response => response.json())
            .then((response)=>{
                if (response.added === true){
                    updates_status.classList.remove("d-none");
                    update_status_message.innerHTML = "Successfully added as a subscriber."
                }else{
                    updates_status.classList.remove("d-none");
                    update_status_message.innerHTML = "Already added as a subscriber."
                }
            })
        .catch((e)=>{
            console.log(e)
        })
        updates_form.reset()
    }
)
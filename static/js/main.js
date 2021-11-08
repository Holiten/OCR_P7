function getValue(evt){
    let user_text = document.getElementById("user_text").value;
    console.log(user_text)
    evt.preventDefault()
    let options = {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({
            question:user_text
        })
    }
    fetch('/user_text', options).then(result => result.json()).then(result => {
        let htmlelem = document.createElement('p')
        htmlelem.textContent = result['wiki_results'][2]
        document.getElementsByTagName('body')[0].appendChild(htmlelem)
    })
}

let user_button = document.getElementById("form")
user_button.addEventListener("submit", getValue)
let user_send = document.getElementById("user_send")
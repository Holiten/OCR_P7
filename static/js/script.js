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
    fetch('/user_text', options).then(results => results.json()).then(results => {
        let htmlelem = document.createElement('p')
        htmlelem.textContent = results['wiki_results'][2]
        document.getElementsByTagName('body')[0].appendChild(htmlelem)
    })
}

let user_button = document.getElementById("form")
user_button.addEventListener("submit", getValue)
let user_send = document.getElementById("user_send")

let lat =



let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}
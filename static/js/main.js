function getValue(evenement){
    let user_text = document.getElementById("user_text").value; //Récupération du texte entré par l'utilisateur
    console.log(user_text) //Print pour test
    evenement.preventDefault() //Arret de l'evenement attendu (ne pas aller sur /user_text)

    let options = {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({
            question:user_text
        })
    }


    fetch('/user_text', options)
        .then(results => results.json())
        .then(results => {document.getElementById('api_container').style.display = 'flex'

        let g_lat = results['g_lat']
        let g_long = results['g_long']

        let g_map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: g_lat, lng: g_long},
            zoom: 14
        })

        new google.maps.Marker({
            position: { lat: g_lat, lng: g_long},
            map: g_map,
        })

        document.querySelector('#user_text_bubble p').textContent = "Voici ce que j'ai trouvé sur " + results['google_args']
        document.querySelector('#format_adress_bubble p').textContent = "L'adresse est la suivante : " + results['g_form_adress']
        document.querySelector('#bubble p').textContent = "Je connais d'ailleurs cet endroit et voici ce que je peux dire de cette adresse : " + results['wiki_results'][2]
    })
}

let user_button = document.getElementById("form")
user_button.addEventListener(
    "submit",
     getValue)
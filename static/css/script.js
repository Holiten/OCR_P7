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
        .then(results => {
        // let html_elem_create = document.createElement('p')
        // html_elem_create.textContent = results['wiki_results'][2]
        document.getElementById('api_container').style.display = 'flex'

        let g_lat = results['g_lat']
        let g_long = results['g_long']



        // let divMap = document.createElement("div");
        // divMap.className = "map";
        // divMap.id = "map"


        g_map.setCenter({lat: g_lat , lng: g_long})


        // document.getElementById('bubble').appendChild(html_elem_create)
        document.querySelector('#bubble p').textContent = results['wiki_results'][2]
    })
}
function calculerKms(element){
    var valeur = document.getElementById("inputkms").value;
    fetch(window.origin+'/calculerkms/'+valeur, {
        method: 'POST'
    })
    // Sens Flask vers Javascript
    .then(function (response) {
        if (response.status !== 200){
            console.log("La réponse du serveur n'est pas 200: " + response.status)
            return 
        }
        response.json().then(function (data) {
            // Ce que je reçois de Flask
            console.log(data)
            location.reload()
        })
    }).catch((error) => {
        alert("Erreur de communication avec le serveur.")
    });
}
function initMap() {
    let myLatLng = {lat: -25.363, lng: 131.044};

    let map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: myLatLng
    });


    for (let i = 0; i < locList.length; i++) {
        
        let myLatLng = locList[i];
        let marker = new google.maps.Marker({
            position: myLatLng,
            map: map,
            title: 'Hello World!'
        });
    }
}


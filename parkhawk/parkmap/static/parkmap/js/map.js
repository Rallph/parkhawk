function initMap() {
    let myLatLng = {lat: 41.661129, lng: -91.530167};

    let map = new google.maps.Map(document.getElementById('map'), {
      zoom: 14,
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


$(function(){
  // alert('ok');
  if(navigator.geolocation)
  {
    navigator.geolocation.getCurrentPosition(getCoords, getError);
  }else {
    initialize(5.066121, -75.503331);
  }
  function getCoords(position)
  {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;

    initialize(lat,lng);
  }

  function getError(err)
  {
    initialize(5.066121, -75.503331);
  }
  function initialize(Lat, Lng)
  {
    var latlng = new google.maps.LatLng(lat, lng);
    var mapSettings = {
      center : latlng,
      zoom: 15,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    map = new google.maps.Map($('#mapa').get(0), mapSettings);

    var marker = new google.maps.Marker({
      position: latlng,
      map: map,
      draggable:true,
      title: 'Arrastrar'
    });

    google.maps.event.addListener(marker, 'position_changed', function(){
      getMarkerCoords(marker);
    });


    function getMarkerCoords(marker)
    {
        var getMarkerCoords = marker.getposition();
        $('#id_lat').val(getMarkerCoords.lat() );
        $('#id_lng').val(getMarkerCoords.lng() );
      }
});

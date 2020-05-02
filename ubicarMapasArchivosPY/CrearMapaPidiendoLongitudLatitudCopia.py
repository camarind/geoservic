def MapasNbC():
    # Con esta funcion podemos ubicar cualqier lugar en el mapa
    geo = Nominatim(user_agent="MyApp")
    lugar = input("Dime un lugar: ")
    loc = geo.geocode(lugar)
    print(loc)
    print(loc.latitude, loc.longitude)

    ### voy a pasar los datos a la funcion con Folium para pintar los mapas
    latitud = loc.latitude
    longitud = loc.longitude
    resp = input ("Por favor digite 1 para Mapa a Color ||| 2 Para mapa a blanco y negro ")
    eXten = '.html'
    if resp == "1":
        #pinto el mapa a color
        print(" Usted Eligio la opcion 1 mapa a color ")
        mapa = folium.Map(location=[latitud, longitud], zoom_start=12, control_scale=True)
        nombreMapaColor = input(" Ponle un nombre al mapa ---->  ")
        ruta = 'C:\\Users\\cesar\\Desktop\\MapasFolium\\'
        rutaColor = ruta+nombreMapaColor+eXten
        mapa.save(rutaColor)
    elif resp == "2":
        #pinto el mapa a blanco y negro
        print(" Usted Eligio la opcion 2 mapa a Blancon y Negro ")
        mapa= folium.Map(location=[latitud, longitud], zoom_start=12, control_scale=True, tiles='Stamen Toner')
        nombreMapaBlancoNegro = input(" Ponle un nombre al mapa ---->  ")
        ruta ='C:\\Users\\cesar\\Desktop\\MapasFolium\\'
        rutaNegro = ruta+nombreMapaBlancoNegro+eXten
        mapa.save(rutaNegro)
    else:
        print("la opcion es incorrecta")

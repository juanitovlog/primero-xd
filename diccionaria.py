meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "MEME": "Imagen, video o texto, por lo general distorsionado con fines caricaturescos, que se difunde principalmente a través de internet,"
            "XD": " carita feliz"
            }
            
word = input("escribe una palabra en mayuscula")

if word in meme_dict.keys():
    print("el significado es",meme_dict[word] )
    
else:
    print(" no esta vuelva a seleccionar")
    
    

# Python_Pro
## Este repositorio pertenece a Nomar Noel Aquino Terrero

meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "JEVI": "Chévere, cool, bueno. Ej: Eso ta’ jevi.",
    "TIGUERE": "Persona astuta, viva a veces con connotación de buscavida",
}

for i in range(5):
    palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if palabra in meme_dict.keys():
        # Si se encuentra la palabra, imprimimos su definición
        print(meme_dict[palabra])
    else:
        # Si no se encuentra, lo avisamos
        print("No encuentro esa palabra")

print("No encuentro más palabras :c") 

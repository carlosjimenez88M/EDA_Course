def convert_units(personajes,alturas,pesos):
    new_hts = [altura / 10 for altura in alturas]
    new_wts = [peso * 2.20 for peso in pesos]

    personaje_data = {}

    for i, personaje in enumerate(personajes):
        personaje_data[personaje] = (new_hts[i],new_wts[i])
    return personaje_data 
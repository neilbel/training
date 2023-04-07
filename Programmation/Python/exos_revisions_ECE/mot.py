def nombre_de_mots(phrase):
    nbr = 0
    for c in phrase:
        if c == '.' or c == ' ':
            nbr += 1
    return nbr
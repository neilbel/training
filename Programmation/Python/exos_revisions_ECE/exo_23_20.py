from random import randint
def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nbre_cases
        if not (case_en_cours in cases_vues):
            cases_vues.append(case_en_cours)
        n += 1
    return n

#Exercice 1 
def ajoute_dictionnaires(d1,d2):
    d = d1.copy()
    for item in d2.items():
        if item[0] in d:
            d[item[0]] += item[1]
        else:
            d[item[0]] = item[1]
      
    return d

print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
## Exercice 1

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]

def rangement_valeurs(notes_eval):
    effectifs = [0,0,0,0,0,0,0,0,0,0,0]
    for note in notes_eval:
        effectifs [note] +=1
    return effectifs

def notes_triees(effectifs):
    l = []
    note = 0
    for n in effectifs:
        for _ in range (n):
            l.append (note)
        note +=1
    return l







                                                
## Exercice 2

def dec_to_bin (nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == ...:
        return str(r)
    else:
        return dec_to_bin(...) + ...

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif ...:
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = ...
        return ... * bin_to_dec(nb_bin[:-1]) + ...

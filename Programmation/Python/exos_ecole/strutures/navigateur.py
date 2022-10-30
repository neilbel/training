# exercices école sur les pile : réaliser un gestionnaire d'historique de
# navigateur à l'aide de dictionnaire.
#
# Auteur : Neil Bel Hadj
# Date : 30/10/2022

from collections import deque

historique = {
    "back":deque(['url_D3','url_C1','url_A8','url_A5']),
    "current":'url_F',
    "forward":deque(['url_Z','url_alpha1'])
}

historique2 = {
    "back":deque(['url_D1','url_C4','url_A2','url_A1']),
    "current":'url_G',
    "forward":deque(['url_E','url_F'])
}

def reculer(hist):
    if(len(hist["back"]) == 0):
        return hist
    else:
        hist["forward"].appendleft(hist["current"])
        hist["current"] = hist["back"].popleft()
        return hist

def avancer(g):
    if(len(g["forward"]) == 0):
        return g
    else:
        g["back"].appendleft(g["current"])
        g["current"] = g["forward"].popleft()
        return g

def nouvelle_url(g, url):
    g["back"].appendleft(g["current"])
    g["current"] = url
    g["forward"].clear()
    

print(historique)
#reculer, reculer, nouvelle_url, reculer, reculer, avancer
reculer(historique)
reculer(historique)
nouvelle_url(historique, "url_n")
reculer(historique)
reculer(historique)
avancer(historique)
print(historique)

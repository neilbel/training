# exercices école sur les pile : réaliser un gestionnaire d'historique de
# navigateur à l'aide d'une classe (version objet de navigateur.py)
#
# Auteur : Neil Bel Hadj
# Date : 30/10/2022

from collections import deque

class Historique:
    def __init__(self, back = deque(), current = "", forward = deque()):
        self.back = back
        self.current = current
        self.forward = forward

    def reculer(self):
        if(len(self.back) == 0):
            return self
        else:
            self.forward.appendleft(self.current)
            self.current = self.back.popleft()
            return self

    def avancer(self):
        if(len(self.forward) == 0):
            return self
        else:
            self.back.appendleft(self.current)
            self.current = self.forward.popleft()
            return self

    def nouvelle_url(self, url):
        self.back.appendleft(self.current)
        self.current = url
        self.forward.clear()

    def __repr__(self):
        return f"Back: {self.back}\nCurrent: {self.current}\nForward: {self.forward}"

h = Historique( deque(['url_D3','url_C1','url_A8','url_A5']),
                'url_F',
                deque(['url_Z','url_alpha1']) )

hv = Historique()

print(h)
print(hv)
#reculer, reculer, nouvelle_url, reculer, reculer, avancer
h.reculer()
h.reculer()
h.nouvelle_url("url_n")
h.reculer()
h.reculer()
h.avancer()
print(h)

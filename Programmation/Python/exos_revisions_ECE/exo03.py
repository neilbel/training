def moyenne(liste):
    numerateur = 0
    denominateur = 0

    for couple in liste:
        numerateur += couple[0] * couple[1] 
        denominateur += couple[1] 
    if denominateur == 0:
        return None
    else:
        return numerateur/denominateur

print(moyenne ([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne ([(3, 0), (5, 0)]))

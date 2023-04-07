def indices_maxi (tab):
    couple=(tab[0],[0])
    for i in range(1, len(tab)):
        if tab[i] > couple[0]:
            couple = (tab[i], [i])
        elif tab[i] == couple[0]:
            couple[1].append(i)
    return couple
print (indices_maxi ([1,5,6,9,1,2,3,7,9,8]))
print (indices_maxi ([7]))

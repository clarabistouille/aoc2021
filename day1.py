file = open('day1key.txt', 'r')
liste = file.read().split('\n')
liste.pop()

#ONE STAR

#searches for increases
def nb_increases(liste):
    sum = 0
    for i in range(1, len(liste)):
        if liste[i] > liste[i - 1]:
            sum += 1
    return sum

#TWO STARS
listesum = []
dico = {"A" : 0, "B" : 0, "C" : 0}
#cases for the 2 first lines
dico["A"] = int(liste[0]) + int(liste[1])
dico["B"] = int(liste[1])
#sum of 3
for i in range(2, len(liste)):
    if i % 3 == 0:
        dico["A"] += int(liste[i]) #1st elem
        dico["B"] += int(liste[i]) #3rd elem (last)
        dico["C"] += int(liste[i]) #2nd elem
        new_sum = dico["B"]
        dico["B"] = 0
    elif i % 3 == 1:
        dico["B"] += int(liste[i]) #1st elem
        dico["C"] += int(liste[i]) #3rd elem (last)
        dico["A"] += int(liste[i]) #2nd elem
        new_sum = dico["C"]
        dico["C"] = 0
    elif i % 3 == 2:
        dico["C"] += int(liste[i]) #1st elem
        dico["A"] += int(liste[i]) #3rd elem (last)
        dico["B"] += int(liste[i]) #2nd elem
        new_sum = dico["A"]
        dico["A"] = 0
    listesum.append(new_sum)
print(nb_increases(liste)+1)
print(nb_increases(listesum))

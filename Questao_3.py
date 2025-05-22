nota_1 = 7.5
nota_2 = 8.0
nota_3 = 6.5

notas = [nota_1, nota_2, nota_3]

for nota in notas:
    media_notas = sum(notas) / len(notas)
    print(round(media_notas,2))


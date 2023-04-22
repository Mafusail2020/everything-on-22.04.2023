weights = sorted([e for e in enumerate(list(map(int, input().split())))], key=lambda x: -x[1])
# print(weights)
m1, m2 = map(int, input().split())

sum_of_weights = sum([num[1] for num in weights])

if m1 + m2 < sum_of_weights:
    print("They can not do it!")

elif m1 >= sum_of_weights and m2 >= sum_of_weights:
    print("They both can do it!")

elif m1 >= sum_of_weights and m2 < sum_of_weights:
    print("Vasyl can do it!")

elif m2 >= sum_of_weights and m1 < sum_of_weights:
    print("Petro can do it!")

else:
    vasyl = []
    vasyl_i = []
    petro = []
    petro_i = []

    for index, mass in weights:
        if sum(vasyl) + mass <= m1:
            vasyl.append(mass)
            vasyl_i.append(index+1)
            continue

    for i in range(len(vasyl)):
        weights.remove((vasyl_i[i]-1, vasyl[i]))

    for index, mass in weights:
        if sum(petro) + mass <= m1:
            petro.append(mass)
            petro_i.append(index+1)
            continue

    for i in range(len(petro)):
        weights.remove((petro_i[i]-1, petro[i]))

    if len(weights) != 0:
        print("They can not do it!")
    else:
        petro_i = [str(i) for i in petro_i]
        vasyl_i = [str(i) for i in vasyl_i]

        print(f"""They need to work together!
Vasyl: {' '.join(vasyl_i)}
Petro: {' '.join(petro_i)}""")


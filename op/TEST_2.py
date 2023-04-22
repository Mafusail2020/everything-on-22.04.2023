n = int(input())

prev = list(map(int, input().split()))
cur = []

vasyl = []
petro = []

for i in range(n-1):
    cur = list(map(int, input().split()))
    for n in cur:
        prev.remove(n)
    missing = sum(prev)

    if i % 2 == 0:
        vasyl.append(str(missing))
    else:
        petro.append(str(missing))

    prev = cur
    if len(prev) == 1:
        if i % 2 != 0:
            vasyl.append(str(prev[0]))
        else:
            petro.append(str(prev[0]))

print(' '.join(sorted(vasyl, key=lambda x: int(x))))
print(' '.join(sorted(petro, key=lambda x: int(x))))

# DO NOT TOUCH

observed = [(0.5, 1.4), (2.3, 1.9), (2.9, 3.2)]

slope = 2 # correct (0.445)
interception = 1 # basic stat (0.9)


SSR = 0
N = 10000
learning_rate = 0.01

for i in range(N):
    # dSSR / dB
    for x, y in observed:
        e = -2*(y - (slope * x + interception))

        SSR += 2*e

    step = learning_rate * SSR
    interception -= step
    ssrb = SSR
    SSR = 0

    for x, y in observed:
        e = -2 * x * (y - (slope * x + interception))

        SSR += 2*e

    step = learning_rate * SSR
    slope -= step
    ssrk = SSR
    SSR = 0
    print(f"k = {round(slope, 2)}\t\tb = {round(interception, 2)}\t\tssrb = {round(ssrb, 2)}\t\tssrk = {round(ssrk, 2)}")

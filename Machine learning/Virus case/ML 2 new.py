from math import *
from colorama import *


w1, b1 = 2.74, 0.0
w2, b2 = -1.13, 0.0

w3 = 0.36
w4 = 0.63
b3 = 0.0


def act(x):
    return log(1 + e**x)


def predict(inp):
    y1 = inp * w1 + b1
    y2 = inp * w2 + b2

    bl = act(y1) * w3
    orang = act(y2) * w4

    out = bl + orang + b3
    return [out, act(y1), act(y2)]


N = 10000
learning_rate = 0.01
dSSR = 0

data_set = [(0, 0),
            (0.5, 1),
            (1, 0)]


graph = [[f'{Fore.BLACK}.' for _ in range(105)] for _ in range(155)]

for i in range(101):
    graph[round(predict(i / 100)[0]/4.5*100)+100][i] = f'{Fore.GREEN}#'
    # print(f"{round(predict(i/100)[0], 2)}", end=' ')

graph.reverse()
for row in graph:
    print(''.join(row))
print(Fore.RESET + "#"*150)
print(Fore.RESET + "#"*150)

for i in range(N):

    # B3 ============================================ B3
    dSSR = 0
    for inpt, outp in data_set:
        predicted_out, y1, y2 = predict(inpt)

        dSSR += -2*(outp - predicted_out)
    step_size = dSSR * learning_rate
    b3 -= step_size
    # B3 ============================================ B3

    # W3 ============================================ W3
    dSSR = 0
    for inpt, outp in data_set:
        predicted_out, y1, y2 = predict(inpt)

        dSSR += -2 * y1 * (outp - predicted_out)
    step_size = dSSR * learning_rate
    w3 -= step_size
    # W3 ============================================ W3

    # W4 ============================================ W4
    dSSR = 0
    for inpt, outp in data_set:
        predicted_out, y1, y2 = predict(inpt)

        dSSR += -2 * y2 * (outp - predicted_out)

    step_size = dSSR * learning_rate
    w4 -= step_size
    # W4 ============================================ W4

    # ------------------------------------------------------------------------

    # W1 ============================================ W1
    dSSR = 0
    for inpt, outp in data_set:
        predicted_out, y1, y2 = predict(inpt)

        dSSR += -2 * inpt * w3 * (outp - predicted_out) * ((e**(inpt * w1 + b1)) / (e ** (inpt * w1 + b1)+1))

    step_size = dSSR * learning_rate
    w1 -= step_size
    # W1 ============================================ W1

    # W2 ============================================ W2
    dSSR = 0
    for inpt, outp in data_set:
        predicted_out, y1, y2 = predict(inpt)

        dSSR += -2 * inpt * w4 * (outp - predicted_out) * ((e ** (inpt * w2 + b2)) / (e ** (inpt * w2 + b2) + 1))

    step_size = dSSR * learning_rate
    w2 -= step_size
    # W2 ============================================ W2

    # B1 ============================================ B1
    dSSR = 0
    for inpt, outp in data_set:
        predicted_out, y1, y2 = predict(inpt)

        dSSR += -2 * w3 * (outp - predicted_out) * ((e**(inpt * w1 + b1)) / (e ** (inpt * w1 + b1)+1))

    step_size = dSSR * learning_rate
    b1 -= step_size
    # B1 ============================================ B1

    # B2 ============================================ B2
    dSSR = 0
    for inpt, outp in data_set:
        predicted_out, y1, y2 = predict(inpt)

        dSSR += -2 * w4 * (outp - predicted_out) * ((e ** (inpt * w2 + b2)) / (e ** (inpt * w2 + b2) + 1))

    step_size = dSSR * learning_rate
    b2 -= step_size
    # B2 ============================================ B2


print("=========================================")
for inpt, outp in data_set:
    pred = round(predict(inpt)[0], 2)

    print(f"Input: {inpt}\nObserved output: {outp}\nPredicted output: {pred}")
    print("=========================================")

print(f"{Fore.BLUE}w3 = {round(w3, 2)}\t{Fore.YELLOW}w4 = {round(w4, 2)}")
print(f"{Fore.RESET}b3 = {round(b3, 2)}\n")
print(f"{Fore.LIGHTBLUE_EX}w1 = {round(w1, 2)}\t{Fore.LIGHTYELLOW_EX}w2 = {round(w2, 2)}")
print(f"{Fore.RESET}b1 = {round(b1, 2)}\tb2 = {round(b2, 2)}")

print("=========================================")


graph = [[f'{Fore.BLACK}.' for _ in range(105)] for _ in range(155)]

for i in range(101):
    graph[round(predict(i / 100)[0]/4.5*100)+100][i] = f'{Fore.GREEN}#'
    # print(f"{round(predict(i/100)[0], 2)}", end=' ')

graph.reverse()
for row in graph:
    print(''.join(row))

import numpy as np


def calc(weight):
    return 2/(1+np.exp(-weight)) - 1


def df(x):
    return 0.5*(1+x)*(1-x)


w11 = np.array([0.12, -0.2, 0.5])
w12 = np.array([-0.12, 0.2, 0.5])
w1 = np.array([w11, w12])
w2 = np.array([-0.6, 0.5])


def net(inps):
    sums = np.dot(w1, inps)
    output_w1 = np.array([calc(s) for s in sums])

    sums = np.dot(w2, output_w1)
    y = calc(sums)

    return (y, output_w1)


def train(input_to_result):
    global w1, w2
    lmbd = 0.001
    N = 100000
    len_of_inp = len(input_to_result)

    for _ in range(N):
        random_inputs = input_to_result[np.random.randint(0, len_of_inp)]

        y, w1_output = net(random_inputs[0:3])

        e = y - random_inputs[-1]
        gradient = e * df(y)

        w2[0] = w2[0] - w1_output[0] * lmbd * gradient
        w2[1] = w2[1] - w1_output[1] * lmbd * gradient

        second_grad = gradient * df(w1_output) * w2

        w1[0, :] = w1[0, :] - np.array(random_inputs[0:3]) * second_grad[0] * lmbd
        w1[1, :] = w1[1, :] - np.array(random_inputs[0:3]) * second_grad[1] * lmbd


epoch = [(-1, -1, -1, -1),
         (-1, -1, 1, 1),
         (-1, 1, -1, -1),
         (-1, 1, 1, 1),
         (1, -1, -1, -1),
         (1, -1, 1, 1),
         (1, -1, -1, -1),
         (1, 1, -1, -1),
         (1, 1, 1, -1)
         ]

train(epoch)

for x in epoch:
    y, out = net(x[0:3])
    print(f"Output is: {round(y, 2)} = {x[-1]}")

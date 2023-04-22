import numpy as np


def calc(weight):
    return 2/(1+np.exp(-weight)) - 1


def df(x):
    return 0.5*(1+x)*(1-x)


nw11 = np.array([-0.3, 1, -0.5])
nw12 = np.array([1, -0.1, 0])
wl1 = np.array([nw11, nw12])
wl2 = np.array([0.15, -1])


def forward(inp):
    sum = np.dot(wl1, inp)
    out = np.array([calc(x) for x in sum])

    sum = np.dot(wl2, out) # y1 * w1 + y2 * w2
    output = calc(sum)
    return (output, out)


def train(epoch):
    global wl1, wl2
    lmbd = 0.01             # Шаг (точность обучения)
    trainings = 10000       # Число итераций
    count = len(epoch)

    for k in range(trainings):
        x = epoch[np.random.randint(0, count)]      # Случайный выбор входного сигнала из выборки для обучения
        y, out = forward(x[0:3])                    # Вывод сети и вывод предыдущих 2-х нейронов
        er = y - x[-1]                              # То насколько сильно сеть ошиблась
        delta = er*df(y)                            # Локальный градиент
        wl2[0] = wl2[0] - lmbd * out[0] * delta     # Корректировка веса первой связи
        wl2[1] = wl2[1] - lmbd * out[1] * delta     # Второй

        delta2 = wl2*delta*df(out)

        wl1[0, :] = wl1[0, :] - np.array(x[0:3]) * delta2[0] * lmbd
        wl1[1, :] = wl1[0, :] - np.array(x[0:3]) * delta2[1] * lmbd


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
    y, out = forward(x[0:3])
    print(f"Output is: {round(y, 2)} = {x[-1]}")

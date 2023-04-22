from math import *
import colorama
import numpy as np


def output_with_bias(weight_out: np.array, bias):
    result_array = np.array([])

    for j in range(len(bias)):
        result_array = np.append(result_array, weight_out[j] + bias[j])
    return result_array


def act(x):
    return np.logaddexp(0, x)


def predict_with_direct_info(inp):
    start = np.array([inp])
    print(f"Start: {start}")

    out_wl_1 = np.dot(wl1, start)
    print(f"Layer 1 weights: {out_wl_1}")
    out_wl_1 = output_with_bias(out_wl_1, bl1)
    print(f"Layer 1 with biases: {out_wl_1}")
    out_wl_1 = np.array([act(x) for x in out_wl_1])
    print(f"Layer 1 output: {out_wl_1}")

    print()

    out_wl_2 = np.array([np.dot(wl2, out_wl_1)])
    print(f"Layer 2 weights: {out_wl_2}")
    out_wl_2 = output_with_bias(out_wl_2, bl2)
    print(f"Layer 2 with biases: {out_wl_2}")
    print()
    return abs(round(out_wl_2[0], 2))

    # print(out_wl_2)


def predict(inp):
    start = np.array([inp])

    out_wl_1 = np.dot(wl1, start)
    out_wl_1 = output_with_bias(out_wl_1, bl1)
    x_1 = out_wl_1[0]
    x_2 = out_wl_1[1]
    out_wl_1 = np.array([act(x) for x in out_wl_1])

    out_wl_2 = np.array([np.dot(wl2, out_wl_1)])
    out_wl_2 = output_with_bias(out_wl_2, bl2)
    return [round(out_wl_2[0], 5), out_wl_1[0], out_wl_1[1], x_1, x_2]

    # print(out_wl_2)


# <><><><><><><><><><><><><><><><><> BACKPROPAGATION START <><><><><><><><><><><><><><><><><><><><><><><><><>

dSSR = 0
learning_rate = 0.001
N = 10000
data_set = [(0, 0),
            (0.5, 1),
            (1, 0)]
c = 0


# ===============================================================================

wl1 = np.array([[2.74], [-1.13]])
bl1 = np.array([[0.0], [0.0]])

wl2 = np.array([0.36, 0.63])
bl2 = np.array([0.0])

# ===============================================================================

for i in range(N):
    inpt, observed_out = data_set[c % 3][0], data_set[c % 3][1]
    predicted_out, green, blue, x_1_i, x_2_i = predict(inpt)

    # For b3
    dSSR = -2*(observed_out - predicted_out)
    step_size = dSSR * learning_rate
    bl2[0] -= step_size
    print(step_size)
    # For b3

    # For w3
    dSSR = -2 * green * (observed_out - predicted_out)
    step_size = dSSR * learning_rate
    wl2[0] -= step_size
    print(dSSR)
    # For w3

    # For w4
    dSSR = -2 * blue * (observed_out - predicted_out)
    step_size = dSSR * learning_rate
    wl2[1] -= step_size
    print(step_size)
    # For w4

    # ============================================

    # For w1
    dSSR = -2 * wl2[0] * inpt * (observed_out - predicted_out) * ((e**x_1_i) / (e ** x_1_i+1))
    step_size = dSSR * learning_rate
    wl1[0][0] -= step_size
    print(step_size)
    # For w1

    # For w2
    dSSR = -2 * wl2[1] * inpt * (observed_out - predicted_out) * ((e**x_2_i) / (e ** x_2_i+1))
    step_size = dSSR * learning_rate
    wl1[1][0] -= step_size
    print(step_size)
    # For w2

    # For b1
    dSSR = -2 * wl2[0] * (observed_out - predicted_out) * ((e ** x_1_i) / (e ** x_1_i + 1))
    step_size = dSSR * learning_rate
    bl1[0][0] -= step_size
    print(step_size)
    # For b1

    # For b2
    dSSR = -2 * wl2[1] * (observed_out - predicted_out) * ((e ** x_2_i) / (e ** x_2_i + 1))
    step_size = dSSR * learning_rate
    bl1[1][0] -= step_size
    print(step_size)
    # For b2
    # print(f"w2 = {wl1[1][0]}\tw1 = {wl1[0][0]}")

    c += 1


# <><><><><><><><><><><><><><><><><> BACKPROPAGATION END <><><><><><><><><><><><><><><><><><><><><><><><><><>

print()
print(f"OUTPUT: {predict_with_direct_info(0.5)}")
print(f"b3 = {round(bl2[0], 2)}")

print(colorama.Fore.BLUE + f"w3 = {round(wl2[0], 2)}\t{colorama.Fore.YELLOW}w4 = {round(wl2[1], 2)}")
print(f"{colorama.Fore.LIGHTBLUE_EX}w1 = {round(wl1[0][0], 2)}\t\
{colorama.Fore.LIGHTYELLOW_EX}w2 = {round(wl1[1][0], 2)}")
print(f"{colorama.Fore.RESET}b1 = {round(bl1[0][0], 2)}\tb2 = {round(bl1[1][0], 2)}")

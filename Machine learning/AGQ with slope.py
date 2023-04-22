import colorama


observed = [(1, 1), (2, 3)]

slope = 2 # correct (0.445)
interception = 2 # basic stat (0.9)
aqquired_inter = 1

def func(x):
    global slope, interception
    y = slope*x + interception
    return y


def dto_intercept(x):
    global slope, interception



SSR = 0
learning_rate = 0.001
N = 1000

for i in range(N):
    # dSSR/dB e = (observed_y - func(x)) -----------------------------
    for x, observed_y in observed:
        der = -2 * (observed_y - slope * x - interception)

        SSR += der

    step_size = SSR * learning_rate
    ssr_b = SSR
    SSR = 0
    interception -= step_size

    # ----------------------------------------------------------------
    # dSSR/dK --------------------------------------------------------
    for x, observed_y in observed:
        der = -2*x * (observed_y - slope * x - interception)
        SSR += der
    step_size = SSR * learning_rate
    slope -= step_size
    ssr_k = SSR
    SSR = 0

    # ----------------------------------------------------------------

    print(f"b = {round(interception, 2)}\t\tk = {round(slope, 2)}\t\tSSR b = {round(ssr_b, 3)}\t\tSSR k = {round(ssr_k, 3)}")

percentage_of_accuracy = 90
print(colorama.Fore.GREEN + f"\n{interception}\t\t{percentage_of_accuracy}%" \
      if 90 < percentage_of_accuracy < 110 \
      else colorama.Fore.RED + f"\n{interception}\t\t{percentage_of_accuracy}%")

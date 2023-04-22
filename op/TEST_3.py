import sys


def query(x: int, y: int) -> bool:
    if x <= 0 or x > 100 or y <= 0 or y > 100:
        return False
    print('?', x, y)
    sys.stdout.flush()
    return input() == 'inside'


def check_square(cor_x, cor_y):
    t_x, t_y = cor_x + 20, cor_y + 20

    previous_x_y = t_x
    while True:
        resp = query(t_x, t_y)
        if not resp:
            b = 19
            while True:
                responce = query(previous_x_y+b, previous_x_y+b)
                if responce:
                    while True:
                        if query(previous_x_y+b+1, previous_x_y+b+1):
                            b += 1
                        else:
                            t_x, t_y = previous_x_y+b, previous_x_y+b

                            # Final check
                            if query(t_x+1, t_y):
                                return False
                            return True

                else:
                    b //= 2

        else:
            previous_x_y = t_x
            t_x += 20
            t_y += 20
            if t_x > 80:
                return False


# Struggling to find corner
def find_corner(x_t, y_t):
    # for the start finding top with binary search
    y_corner = None
    x_corner = None

    b = 19
    while True:
        resp = query(x_t, y_t - b)
        if resp:
            while True:
                if query(x_t, y_t - b - 1):
                    b -= 1
                else:
                    break

            y_corner = y_t - b
            break
        else:
            b //= 2
    b = 19
    # now the left side
    while True:
        resp = query(x_t - b, y_corner)
        if resp:
            while True:
                if query(x_t - b - 1, y_corner):
                    b -= 1
                else:
                    break

            x_corner = x_t - b
            break
        else:
            b //= 2

    return (x_corner, y_corner)


def answer(result: bool):
    if result:
        print('! square')
    else:
        print('! rectangle')
    sys.stdout.flush()


# Searching for any cell
step = 20
x, y = step, step
i = 0

while True:
    for x in range(20, 81, 20):
        answ = query(x, y)
        if answ is True:
            top_x, top_y = find_corner(x, y)
            is_square = check_square(top_x, top_y)
            if is_square:
                answer(True)
            else:
                answer(False)
    y = y+step
    if y > 80:
        y = step
    i += 1
    if i > 11:
        print('! rectangle')
        sys.stdout.flush()

import sys

def query(x: int, y: int) -> bool:
    if x <= 0 or x > 100 or y <= 0 or y > 100:
        return False
    print('?', x, y)
    sys.stdout.flush()
    return input() == 'inside'


def answer(result: bool):
    if result:
        print('! square')
    else:
        print('! rectangle')
    sys.stdout.flush()


is_over = False
for cy in range(1, 101):
    for cx in range(1, 101):
        resp = query(cx, cy)
        if resp:
            width = 0
            height = 0

            for x in range(cx, 100):
                res = query(x+1, cy)
                if not res:
                    width = x - cx
                    break
            print(width)
            for y in range(cy, 101):
                res = query(cy, y+1)
                if not res:
                    height = y - cy
                    break
            print(height)
            if width == height:
                answer(True)
                is_over = True
            else:
                answer(False)
                is_over = True
            break
    if is_over:
        break

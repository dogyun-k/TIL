import numpy as np


def print_arr(arr):
    # 윗 라인
    print('===', end='')
    for _ in range(len(arr[0])):
        print('=====', end='')
    print('=====')

    print('R\C', end='')
    for i in range(len(arr[0])):
        print('{:5}'.format(i), end='')
    print('  sum')

    for r, a in enumerate(arr):
        print('{:3}'.format(r), end='')
        for j in a:
            print('{:5}'.format(j), end='')
        print('{:5}'.format(sum(a)))

    arr = arr.transpose()

    print('sum', end='')
    for i in arr:
        print('{:5}'.format(sum(i)), end='')
    print('{:5}'.format(arr.sum()))

    # 아래 라인
    print('===', end='')
    for _ in range(len(arr)):
        print('=====', end='')
    print('=====')

origin = np.array(range(100, 0, -1)).reshape(10, 10).transpose()
print('original array')
print_arr(origin)

print('slicing')
print_arr(origin[1::2, 1::3])

print('reshaping')
print_arr(origin[1::2, 0:9].reshape(3, 15)[:, 1::3])
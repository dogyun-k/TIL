import numpy as np

arr = 5*np.random.randn(3, 5) + 10

print('randomly generated array mean 10 std 5')
print('----------------------------------------')
for i in arr:
    for j in i:
        print("{:7.2f}".format(j), end=' ')
    print()
print('----------------------------------------')
arr = arr.reshape(15)
arr.sort()
print('3rd = {:5.2f}, 12th = {:5.2f}'.format(arr[2], arr[11]))

print('sorted 2d array')
print('----------------------------------------')
arr = arr.reshape(3, 5)
for i in arr:
    for j in i:
        print("{:7.2f}".format(j), end=' ')
    print()
print('----------------------------------------')

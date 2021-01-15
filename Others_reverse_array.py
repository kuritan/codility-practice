def reverse_array(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
    return a

if __name__ == '__main__':
    print(reverse_array([1,2,3,4,5,6]))
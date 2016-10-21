def count_down(n):
    print(n)
    if n != 0:
        count_down(n-1)

count_down(5)

def count_up(n):
    for i in range(0, n+1, 1):
        print(i)

count_up(5)
def print_rect(n, m):
    for _ in range(n):
        for _ in range(m):
            print("1", end="")
        print()

n,m = map(int, input().split())
print_rect(n,m)
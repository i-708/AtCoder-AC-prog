def main():
    import sys
    
    readline = sys.stdin.readline
    # ε₯ε
    N,K = map(int,readline().rstrip().split())

    for i in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            n = int(str(N) + '200')
            N = int(n)
    # εΊε
    print(N)


main()

def main():
    import sys
    
    readline = sys.stdin.readline
    # ε₯ε
    N = int(readline().rstrip())
    cnt = 1
    while True:
        N -= 100
        if N <= 0:
            break
        else:
            cnt += 1
    # εΊε
    print(cnt)


main()

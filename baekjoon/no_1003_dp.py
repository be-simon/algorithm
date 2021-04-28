if __name__ == '__main__':
    T = input()
    for _ in range(int(T)):
        N = int(input())
        fibo_0 = [0 for _ in range(N + 1)]
        fibo_1 = [0 for _ in range(N + 1)]
        for i in range(N + 1):
            if i == 0:
                fibo_0[i] = 1
                fibo_1[i] = 0
            elif i == 1:
                fibo_0[i] = 0
                fibo_1[i] = 1
            else:
                fibo_0[i] = fibo_0[i - 1] + fibo_0[i - 2]
                fibo_1[i] = fibo_1[i - 1] + fibo_1[i - 2]
        
        print(fibo_0[N], fibo_1[N])

n = int(input())
mod = 1000000
p = 15 * mod // 10

fibo = [0] * p

fibo[0] = 0
fibo[1] = 1

for i in range(2, p):
  fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000


print(fibo[n % p])
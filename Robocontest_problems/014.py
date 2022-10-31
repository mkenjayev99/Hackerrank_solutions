MOD_NUM = int(1e9 + 7)

def binpow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        x = binpow(a, n/2)
        return x * x % MOD_NUM
    return a * binpow(a, n-1) % MOD_NUM

def func():
    n, k = map(int, input().split())
    print(binpow(k+1, n))
func()
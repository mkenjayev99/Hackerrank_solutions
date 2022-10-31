# The answer is equal to "N"th term of Fibonacci

def flagCombinations(n):
    fibonacci = [0, 1]
    for i in range(2, n+1):
        i = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(i)
    answer = fibonacci[n]*2
    return answer


n = int(input())
print(flagCombinations(n))

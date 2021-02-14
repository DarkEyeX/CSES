def weird(n):
    print(n, end=' ')
    if n == 1:
        return(n)
    elif n % 2 == 0 :
        return(weird(n//2))
    else:
        return(weird((n*3)+1))
n = int(input())
weird(n)

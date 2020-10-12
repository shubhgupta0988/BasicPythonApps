def prime(p):
    if p == 1:
        return (False)
    for i in range (2,p) :
        if p % i == 0:
            return (False)
            break
    else:
        return (True)

n = int(input("Enter the number whose prime factorisation is to be found out:"))

if n == 1 :
    print ("Prime factorisation of 1 is not possible as it is neither prime nor composite")

else:
    factors = []
    for i in range(2, n+1):
        x = i
        if prime(x):
            while n % x == 0:
                factors.append(i)
                x = x*i
    for i in range (len(factors) - 1):
        print(factors[i], "*", end = "")
    print (factors.pop())




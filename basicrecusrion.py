#printing n nums reverse order
'''def printnos(n):
    if n<= 0:
        return 0 
    print(n) 
    printnos(n-1)
n = int(input())
print(printnos(n))'''
#printing n nums ascending order
'''def sumofn(n, sum=0):
    if n< 0 :
        print(sum)
        return 
    sumofn(n-1, sum+n)'''
'''def sumofn(n):
    if n == 0:
        return 0
    return n + sumofn(n-1)

n = int(input())
print(sumofn(n))'''

#factorial of n
def fact(n):
    if n <=0:
        return 1
    return n*fact(n-1)

n = int(input())
print(fact(n))
    

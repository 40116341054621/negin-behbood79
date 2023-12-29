def findthebiggest(a,b,c):
    max=a
    if(b>max):
     max=b
    if(c>max):
     max=c
    else:
      print("They are equal")
    
    print("max={0}".format(max))
    
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
c=int(input("enter your third number:"))
findthebiggest(a,b,c)

print()


def rec(a,b):
    c=a*b
    return c

a=float(input("Enter length="))
b=float(input("Enter width="))
print("area={0}".format(rec(a,b)))


print()


def isprime(x):
    flag=True
    for i in range(2,x):
        if(x%i==0):
            flag=False
    if(flag==True):
        return 1
    else:
        return 0
    
a=int(input("Enter your number="))
print("The result is={0}".format(isprime(a)))


print()


def iscomplete(a):
    s=0
    for i in range(1,a):
        if(a%i==0):
            s+=i
    if(s==a):
        return 1
    else:
        return 0
x=int(input("Enter number="))
print("checking if complete or not ={0}".format(iscomplete(x)))


print()


lst=[]
def maxlist(lst):
    return max(lst)


for i in range(1,101):
    x=int(input("Enter elements="))
    lst.append(x)
print("The biggest element is={0}".format(maxlist(lst)))


    


print()


def isprime(i):
    flag=True
    for j in range(2,i):
        if(i%j==0):
            flag=False
            break
    if(flag==True):
        return 1
    else:
        return 0
    
for i in range(1,1000000):
    if(isprime(i) and i!=1 ):
        print(i)



print()


def plus(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s

n=int(input("Enter n="))
print("The final answer is={0}".format(plus(n)))


print()


def sort_lst(lst):
    lst.sort(reverse=True)
    print(lst)
    

lst=[int(x) for x in input("Enter list elements=").split()]
sort_lst(lst)


print()


def search_list(lst,x):
    if x in lst:
        return lst.index(x)
    else:
        return -1
    
lst=[i for i in range(1,101)]
print("The index of targeted number is={0}".format(search_list(lst,4)))


print()


def num_digit(x):
    s=0
    while (x>0):
        b=x%10
        s+=b
        x//=10
    return s


x=int(input("Enter num="))
print("The sum of digits={0}".format(num_digit(x)))


print()


def digit_count(x):
    count=0
    while (x>0):
        x%10
        x//=10
        count+=1
    return count

n=int(input("Enter x="))
print("The count of digit={0}".format(digit_count(x)))

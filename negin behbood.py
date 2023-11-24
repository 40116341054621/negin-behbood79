a=int(input("Enter a="))
b=int(input("Enter b="))
s=a+b
print("s={0}".format(s))

print()

a=int(input("Enter a="))
b=int(input("Enter b="))
if(a>b):
    print("a is bigger than b")
elif(a>b):
    print("b is bigger than a")
else:
    print(" they are equal")

print()

a=int(input("Enter a="))
b=int(input("Enter b="))
c=int(input("Enter c="))
max=5
if(b>c):
    max=b
if(a>c):
   max=a
print("max{0}".format(max))


print()

a=int(input("Enter your first number="))
count=1
while count<100:
    number=int(input("Enter another number="))
    count+=1
    if(number>a):
       max=number
print(max)

print()

a=int(input("Enter your first number="))
max=a
min=a
count=1
while count<100:
    number=int(input("Enter your next number="))
    if(number>max):
        max=number

    elif(number<min):
        min=number
    count+=1

print(max)
print(min)

print()


a=[]
for i in range(1,11):
    a.append(int(input("Enter number:")))

a.sort(reverse=True)
print(a)


print()

b=[]
for i in range(1,101):
    b.append(int(input("Enter value:")))

b.sort()
print(b)


print()


a=int(input("Enter a="))
if(a%2==0):
    print("even")
else:
    print("odd")


print()

num=int(input("Enter your number="))
max=num
for i in range(1,10):
    a=int(input("Enter another number="))
    if(a>max):
        max=a

print(max)


print()


a=int(input("Enter a="))
b=int(input("Enter b="))
for i in range(a+1,b):
    if(i%2==0):
        print(i)


print()


a=int(input("Enter a="))
flag=True
for i in range(2,a):
    if(a%i==0):
        flag=False
        break

if(flag):
    print("F")

else:
    print("H")


print()


a=int(input("Enter a="))
b=int(input("Enter b="))
count=0
if a>b:
    (a,b)=(b,a)

for i in range(a+1,b):
    for j in range(2,i):
        if(i%j==0):
            count+=1
            break
        if(count!=0):
           print(i)
           break


print()


a=int(input("Enter a="))
b=int(input("Enter b="))
if(a>b):
    (a,b)=(b,a)

for i in range(a+1,b):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum+=i
        if(sum==2*i):
            print(i)


print()


n=int(input("Enter your number="))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==n):
   print('True')

else:
   print("False")


print()


a=[]
for i in range(1,101):
    a.append(int(input("Enter value=")))
print(max(a))


print()


lst=[]
for i in range(1,11):
    lst.append(int(input("Enter value=")))
x=int(input("Enter x="))
if x in lst:
    print("found")
else:
    print("not found")



print()



lst1=[]
lst2=[]
for i in range(1,101):
    lst1.append(int(input('enter value=')))
for j in range(1,101):
    lst2.append(int(input('Enter more values=')))
c=lst1+lst2
print(c)



print()


a=int(input("Enter a="))
sum=0
while a>=0:
    a=int(input('Enter a='))
    sum+=a

print(sum-a)



print()



b=int(input("Enter b="))
f=1
i=1
while i<=x:
    f*=i
    i+=1
print("factorial=",f)


print()


m=int(input("Enter m="))
n=int(input("Enter n="))
fact=1
while m>n:
    f=m-n
    for i in range(1,f):
        fact*=i

print("factorial=",fact)


            




























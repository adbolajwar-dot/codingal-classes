a=3
b=6
c=4

avg=(a+b+c)/3
print(avg)

if avg>5 and avg>b and avg>c:
    print("Average is greater than all.")

elif avg>a and avg>b :
    print("Average is greater than a and b.")

elif avg>a :
    print("Average is greater than a.")

else:
    print("Average is not greater than a, b and c.")
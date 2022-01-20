#Wap to check a given number prime or not

num=int(input("Enter n values"))
if num>1:
    for i in range(2,num):
      if(num,i==0):
        print("Given number is not prime")
        break
    else:
       print("Given number is prime")

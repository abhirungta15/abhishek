def div(num):
     lst=[]
     for i in range(1,num+1):
          if num%i==0:
               lst.append(i)
     return lst

num=int(input("Enter the number:"))
lst=[]
lst=div(num)
print("The divisor of the",num,"are as follows:") 
print(lst)

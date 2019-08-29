def find(ordered_list, element_to_find):
    
    for element_to_find in ordered_list:
      return (1)
    else:
        return (0)
  
lst2 = []
size = int(input("Enter the size:"))
print("Enter the elements:")
for i in range(0, size):
    a=int (input())
    lst2.append(a)
ele=input("Enter the element to find:")

result=(find(lst2,ele))
if result==True:
    print("found",(ele))
else :
    print("Not found",(ele))


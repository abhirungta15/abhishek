string = input("Enter the string: ")

new_string = string.split(" ")
new_string1 = new_string[-1::-1]
rev_string = " ".join(new_string1)
print("Original String: ", string)
print("Output 1: ",rev_string)

converted = []

for i in new_string:
     converted.append(i[::-1])

another_rev_string = " ".join(converted)

print("Output 2: ",another_rev_string)

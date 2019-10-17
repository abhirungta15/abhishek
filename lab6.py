class validity:
    def __init__(self,string):
        self.sequence_string=string

    def validate(self):
        strlist=list(self.sequence_string)
        stack1=[]
        stack2=[]
        stack3=[]
        for char in strlist:
            if char=='(':
                stack1.append(char)
            if char==')':
                if not stack1:
                    return 0
                else:
                    stack1.pop()

            if char=='{':
                stack2.append(char)
            if char=='}':
                if not stack2:
                    return 0
                else:
                    stack2.pop()

            if char=='[':
                stack3.append(char)
            if char==']':
                if not stack3:
                    return 0
                else:
                    stack3.pop()
        if  stack1 or  stack2 or  stack3:
            return 0
        else:
            return 1

seq=input("Enter the string\n")
obj=validity(seq)
if obj.validate()==0:
    print("Invalid String")
else:
    print("Valid String")

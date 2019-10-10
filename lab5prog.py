class callDetails:
    def __init__(self,c,r,d,t):
        self.cal = c
        self.rec = r
        self.dur = d
        self.typ = t

    def disp(self):
        print("\nCaller: ",self.cal)
        print("Reciever: ",self.rec)
        print("Duration: ",self.dur)
        print("Type: ",self.typ)

class Util:
    def __init__(self):
        self.list_of_call_objects = []  
        self.count = 0
        self.count1 = 0
        self.count2 = 0
    def parse_customer(self,list_of_call_string):
        
        for i in list_of_call_string:
            x = i.split(",")
            for j in x:
                if j == "STD":
                    self.count+= 1
                elif j == "ISD":
                    self.count1+= 1
                elif j == "Local":
                    self.count2+= 1
                
            o = callDetails(*x)
            self.list_of_call_objects.append(o)
        

    def disp(self):
        for i in self.list_of_call_objects:
            i.disp()
        print("\nSTD: ",self.count)
        print("ISD: ",self.count1)
        print("Local: ",self.count2)


call = '9123848912,12385612934,23,STD'
call2 = '2395713534,29435812359,12,Local'
call3 = '123854295,105949324,18,ISD'
call4 = '134845,34953460,19,ISD'
list_of_call_string = [call, call2, call3, call4]
util = Util()
util.parse_customer(list_of_call_string)
util.disp()

class CallDetail:
    def __init__(self, call_from, call_to,duration,call_type):
        self.call_from=call_from
        self.call_to=call_to
        self.duration=duration
        self.call_type=call_type
        
    def print_details(self):
        print(self.call_from," ",self.call_to," ",self.duration," ",self.call_type)
        
class Util:
    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self,list_of_call_string):
        
        for i in list_of_call_string:
            li=i.split(',')
            self.list_of_call_objects.append(CallDetail(li[0],li[1],li[2],li[3]))
            
    def show_list(self):
        for i in self.list_of_call_objects:
                i.print_details()


call1='9999999999,8888888888,98,STD'
call2='7777777777,6666666666,67,ISD'
call3='1011010101,8855875748,2,Local'

list_of_call_string=[call1,call2,call3]

Obj1=Util()
Obj1.parse_customer(list_of_call_string)
Obj1.show_list()
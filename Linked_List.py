class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        temp1=Node(data)
        if(self.__head==None):
            self.__head=temp1
            self.__tail=temp1
        else:
            self.__tail.set_next(temp1)
            self.__tail=temp1
        #Remove pass and copy the code you had written to add an element.
    
    def display(self):
        temp2=LinkedList()
        temp2=self.__head
        while(temp2 is not None):
            print(temp2.get_data())
            temp2=temp2.get_next()
        #Remove pass and copy the code you had written to display the element(s).
    
    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return(temp.get_data()+"found")
            temp=temp.get_next()
        return None
        #Remove pass and copy the code you had written to find the node containing the element.

    
    def insert(self,data,data_before):
        tem=Node(data)
        if(data_before==None):
            tem.set_next(self.__head)
            self.__head=tem
            if(self.__head.get_next()==None):
                self.__tail=tem
        else:
            temp1=self.__head
            while(temp1 is not None):
                if(data_before==temp1.get_data()):
                    tem.set_next(temp1.get_next())
                    temp1.set_next(tem)
                    if(tem.get_next()==None):
                        self.__tail=tem
                temp1=temp1.get_next()
            return("error")
                    
        #Remove pass and copy the code you had written to insert an element.
    
    def delete(self,data):
        temp=self.__head
        if(temp.get_data()==data):
            head=temp.get_next()
            del(temp)
            return
        while(temp is not None):
            if(temp.get_data()==data):
                temp1=temp
                temp=temp.get_next()
                del(temp1)
                return
            else:
                temp=temp.get_next()
        print("error")
        #Remove pass and write the logic to delete an element.
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


list1=LinkedList()
#Add all the required element(s)
#Delete the required element.
list1.add("salt")
list1.add("sugar")
print(list1.find_node("milk"))
list1.insert("milk","salt")
list1.insert("teabags","sugar")
list1.display()
#list1.delete("Sugar")
list1.display()
'''
Created on Jan 22, 2020

@author: Admin
'''

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size
                                       
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg    

def remove():
    global clipboard,undo_stack
    data=clipboard[len(clipboard)-1]
    clipboard.remove(data)
    undo_stack.push(data)
    print("Remove:",clipboard)

def undo():
    global clipboard,undo_stack,redo_stack
    if(undo_stack.is_empty()):
        print("There is no data to undo")
    else:
        data=undo_stack.pop()
        clipboard.append(data)
        redo_stack.push(data)
    print("Undo:",clipboard)


def redo():
    global clipboard, undo_stack,redo_stack
    if(redo_stack.is_empty()):
        print("There is no data to redo")
    else:
        data=redo_stack.pop()
        if(data not in clipboard):
                print("There is no data to redo")
                redo_stack.push(data)
        else:
            clipboard.remove(data)
            undo_stack.push(data)
    print("Redo:",clipboard)



clipboard=["A","B","C","D","E","F"]
undo_stack=Stack(len(clipboard))
redo_stack=Stack(len(clipboard))
remove()
undo()
redo()
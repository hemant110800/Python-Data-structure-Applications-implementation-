class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size
                                        
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

def send_for_print(doc):
    global print_queue
    if(print_queue.is_full()):
        print("Queue is full")
    else:
        print_queue.enqueue(doc)
        print(doc,"sent for printing")


def start_printing():
    global print_queue
    while(not print_queue.is_empty()):
        doc=print_queue.dequeue()
        global pages_in_printer
        for i in range(0,len(doc)):
            if(doc[i]=="-"):
                no_of_pages=int(doc[i+1:])
                break
        if(no_of_pages<=pages_in_printer):
            print(doc,"printed")
            pages_in_printer-=no_of_pages
            print("Remaining no. of pages in printer:", pages_in_printer)
        else:
            print("Couldn't print",doc[:i],". Not enough pages in the printer.")

     

pages_in_printer=12
print_queue=Queue(10)
send_for_print("doc1-5")
send_for_print("doc2-3")
send_for_print("doc3-6")
start_printing()


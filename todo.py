class Todo:
   
    def __init__(self) -> None:
        self.todo_list = [] 
    def add(self,task): 
        self.todo_list.append(task)
    def print_list(self):
        j =0 
        for i in self.todo_list: 

            print("[", j ,"].",i)
            j=j+1

    def remove(self,i): 
        self.todo_list.pop(i)

t = Todo()
op = 1; 
while op!=5: 
    print("\n[1] add \n [2] print_list\n[3].remove")
    print("\n")
    op = int(input("enter your option : "))
    if op ==1 : 
        t.add(input("enter the task: "))
    elif op ==2: 
        t.print_list()
    else: 
        t.remove(int(input("enter the Sl No of task to remove: ")))
t.add("lunch")
t.print_list();

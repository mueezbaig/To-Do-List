tasks = []

completed_task = []

def add(description, due_date, priority):
    task = {
        "description":description, 
        "due_date": due_date,
        "priority": priority,
        "Complete": False
    }
    tasks.append(task)
    print("Task Added Successfully. ")

def Display():
    if len(tasks)>0:
        print("To-do List:\n")
        i = 1 
        for j in tasks:
            s = "Completed" if j["Complete"] else "Pending"
            print(f"{i}.Description: {j['description']}\n  Due_Date: {j['due_date']}\n  Priority: {j['priority']}\n  Status: {s}\n ")
            i=i+1

    else:
        print("No Tasks in to-do List. ")

def Complete_task(t_index):
    if len(tasks) == 0:
        print("No tasks in the to-do list. Please add tasks before updating.")
        return
    
    if 0 <= t_index < len(tasks):
        tasks[t_index]["Complete"] = True
        completed_task.append(tasks.pop(t_index))
        print("Task Marked as completed. ")

    else:
        print("Invalid Task Index.")

def Update(t_index, description, due_date, priority):
    if len(tasks) == 0:
        print("No tasks in the to-do list. Please add tasks before updating.")
        return
    
    if 0<=t_index < len(tasks):
        task = tasks[t_index]

        if description and description!=task["description"]:
            task["description"] = description

        if due_date and due_date!=task["due_date"]:
            task["due_date"] = due_date

        if priority and priority != task["priority"]:
                task["priority"] = priority

        if description or due_date or priority:
            print("Task updated Successfully. ")

        else:
            print("No changes made to the task.")

    else:
        print("Invalid task index.")

def Remove(t_index):
    if len(tasks) == 0:
        print("No tasks in the to-do list. Please add tasks before updating.")
        return
    
    if 0<=t_index<len(tasks):
        tasks.pop(t_index)
        print("Task removed from the list. ")

    else:
        print("Invalid task index.")


while True:
    print("\nTo-do List Application ")
    print('1. Add Tasks ')
    print('2. Display Tasks ')
    print('3. Mark as Completed ')
    print('4. Update Task ')
    print('5. Remove Task')
    print('6. Exit\n')

    ch = input("Enter Your Choice (1-6): ")

    if ch == '1':
        description = input("Enter Your Description: ")
        due_date = input("Enter Due_Date: ")
        priority = input("Enter Priority: ")
        add(description, due_date, priority)

    elif ch == '2':
        Display()

    elif ch == '3':
        if len(tasks) == 0:
            print("No tasks in the to-do list. Please add tasks before updating.")
            continue
        t_index = int(input("Enter the task_index to mark as completed: "))
        Complete_task(t_index - 1)

    elif ch == '4':
        if len(tasks) == 0:
            print("No tasks in the to-do list. Please add tasks before updating.")
            continue

        t_index = int(input("Enter task index to update: "))
        description = input("Enter Your Description: ")
        due_date = input("Enter Due_Date: ")
        priority = input("Enter Priority: ")

        Update(t_index-1, description, due_date, priority)

    elif ch == "5":
        if len(tasks) == 0:
            print("No tasks in the to-do list. Please add tasks before updating.")
            continue

        task_index = int(input("Enter task index to remove: "))
        Remove(task_index - 1)

    elif ch == '6':
        break

    else:
        print("Invalid choice. Please try again.")
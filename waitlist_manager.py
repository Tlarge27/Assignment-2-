# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None
    
# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None
#This is to add a customer to the front of the waitlist. 
    def add_front(self, name): 
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} added to the front of the waitlist") 

#This is to add a customer to the END of the waitlist. 
    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head + new_node
        else: 
            current = self.head
            while current.next: 
                current = current.next
            current.next = new_node
        print(f"{name} added to the end of the waitlist")
    
#This is to remove a name from the waitlist. 

    def remove(self, name): 
        current = self.head
        prev = None
        while current:
            if current.name == name: 
                if prev:
                    prev.next = current.next
                else: 
                    self.head = current.next
                print(f"Removed {name} from the waitlist")
                return
            prev = current
            current = current.next 
        print(f"{name} not found in the waitlist")  

#This is to print the current waitlist 
    def print_list(self):
        if not self.head:
            print("The waitlist is empty")
            return
        current = self.head
        while current:
            print(f"- {current.name}")
            current = current.next 

def waitlist_generator():
    waitlist = LinkedList()
    
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)
            
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()
            
            
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()
'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
# The waitlist program that I created uses a linked list. It's a way of storing a list of infomation where every node links onto the next node. 
# Every node will hold a customer name and link it to the next node in the line. All of this is under the linkedlist class. The class itslef works to let you add
# Customers to the back or front of the list, aswell as removing them from the list or to print the list to see the full list of names. 

# The head is the first node in a list, essentially it's the starting point for the list. Without the head there is no list because no other items can be accessed. 
# When I add, remove, or use any of the functions of the class the head needs to update so it will always indentify the first person in line. 
# Without this names may not remove, or the list would show out of order, defeating the purpose of the list in the first place. 

# A real engineer would use a list like this if they needed to keep track of a queue of tasks or of things that need to be correctly ordered.
# The first thing that came to mind for real world application is the waitlist at a restaurant. For whatever reason I thought of Olive Garden
# Because every time I go, there is a line. But using the linked lists makes it easy to add and remove names or tasks from a list.
# It makes it easier to control and edit the data thats being stored. I believe it also can make programs run faster. 
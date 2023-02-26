"""
Q1: Create a class called BankAccount that has four attributes: bankname,
firstname,lastname, and balance.
"""


#Class for Bank Account
class BankAccount:
    def __init__(self, bankname, firstname, lastname, balance=0):
        #Initialize the bank account
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def deposit(self, amount):
        #Add deposit amount to balance
        self.balance = self.balance + amount
        print(f"Deposit complete.  Current balance: {self.balance}")

    def withdrawal(self, amount):
        #Withraw amount from balance
        if amount > self.balance:
            print("Withdrawal is greater than current balance. Transaction cancelled.")
        else:
            self.balance = self.balance - amount
            print(f"Withdrawal complete. Remaining balance: {self.balance}")

    def __str__(self):
        #Return a string with the bank account information
        return f"Bank Name: {self.bankname}\nOwner Name: {self.firstname} {self.lastname}\nCurrent Balance: {self.balance}"


#Instantiate a bank account and examples
myaccount = BankAccount("Chase Bank", "Johny", "Rodriguez", 1000)

#Print the bank account information
print(myaccount)

#Deposit money
myaccount.deposit(500)

#Withdraw money
myaccount.withdrawal(250)

#Withdraw more money than the current balance
myaccount.withdrawal(5000)


"""
Q2: Create a class Box that has attributes length and width that takes values 
for length and width upon construction (instantiation via the constructor).
"""

#Class for Box
class Box:
    #Initialize the box
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def render(self):
        #Prints out to the screen a box made with asterisks
        for i in range(self.width):
            print('*' * self.length)

    def invert(self):
        #Switches the length and width of the box
        self.length, self.width = self.width, self.length

    def get_area(self):
        #Returns the area of the box
        return self.length * self.width

    def get_perimeter(self):
        #Returns the perimeter of the box
        return 2 * (self.length + self.width)

    def double(self):
        #Returns a new box with dimensions twice the original
        new_box = Box(self.length * 2, self.width * 2)
        return new_box

    def __eq__(self, other):
        #Returns true if the length and width of the boxes are equal
        return self.length == other.length and self.width == other.width

    def print_dim(self):
        #Prints the length and width of the box
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")

    def get_dim(self):
        #Returns the length and width of the box
        return (self.length, self.width)

    def combine(self, other):
        #Combines two boxes
        self.length = self.length + other.length
        self.width = self.width + other.width

    def get_hypot(self):
        #Returns the hypotenuse of the box
        return (self.length ** 2 + self.width ** 2) ** 0.5


# Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1, box2 and box3 respectively
box1 = Box(5, 10)
box2 = Box(3, 4)
box3 = Box(5, 10)

# Print dimensions
box1.print_dim()
box2.print_dim()
box3.print_dim()

# Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False
print(box1 == box2)
print(box1 == box3)

# Combine box3 into box1
box1.combine(box3)

# Double the size of box2
box2 = box2.double()

# Combine box2 into box1
box1.combine(box2)

# Print the final dimensions of box1
box1.print_dim()


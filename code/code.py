import sys 
def initial_contactbook(): 
    rows, cols = int(input("Please enter initial number of contacts: "))
    contact_book = [] 
    print(contact_book) 
    for i in range(rows): 
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1)) 
        print("NOTE: * indicates mandatory fields") 
        print("....................................................................") 
        t = [] 
        for j in range(cols):
          if t[j] == '' or t[j] == ' ': 
                    sys.exit( 
                        "Name is a needed") 
          if j == 1: 
                t.append(int(input("Enter number*: "))) 
          if j == 2: 
                t.append(str(input("Enter e-mail address: "))) 
                if t[j] == '' or t[j] == ' ': 
                    t[j] = None
                      
          if j == 3: 
                t.append(str(input("Enter date of birth(dd/mm/yy): "))) 
                if t[j] == '' or t[j] == ' ': 
                  t[j] = None
          if j == 4: 
                t.append( 
                str(input("Enter category(Family/Friends/Work/Others): "))) 
                if t[j] == "" or t[j] == ' ': 
                    t[j] = None
        contact_book.append(t)
        print(contact_book) 
    return contact_book 
  
def menu(): 
   print("********************************************************************") 
   print("SMARTPHONE DIRECTORY", flush=False) 
   print("********************************************************************") 
   print("You can now perform the following operations on this contactbook\n") 
   print("1. Add a new contact") 
   print("2. Remove an existing contact") 
   print("3. Delete all contacts") 
   print("4. Search for a contact") 
   print("5. Display all contacts") 
   print("6. Exit contactbook") 
   choice = int(input("Please enter your choice: ")) 
      
   return choice 
  
def add_contact(cb): 
    dip = [] 
    for i in range(len(cb[0])): 
        if i == 0: 
            dip.append(str(input("Enter name: "))) 
        if i == 1: 
            dip.append(int(input("Enter number: "))) 
        if i == 2: 
            dip.append(str(input("Enter e-mail address: "))) 
        if i == 3: 
            dip.append(str(input("Enter date of birth(dd/mm/yy): "))) 
        if i == 4: 
            dip.append( 
                str(input("Enter category(Family/Friends/Work/Others): "))) 
    cb.append(dip) 
    return cb 
  
def remove_existing(cb): 
  query = str( 
        input("Please enter the name of the contact you wish to remove: ")) 
  t = 0
  for i in range(len(cb)): 
        if query == cb[i][0]: 
          t += 1
          print(cb.pop(i)) 
          print("This query has now been removed") 
          return cb 
        if t == 0: 
           print("Sorry, you have entered an invalid query.\  Please recheck and try again later.") 
          
        return cb 
  
def delete_all(cb):
  return cb.clear() 
  
def search_existing(cb): 
    choice = int(input("Enter search criteria \n\n1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\nPlease enter: ")) 
    t = [] 
    check = -1
   
      
    if choice == 1: 
      query = str( 
      input("Please enter the name of the contact you wish to search: ")) 
      for i in range(len(cb)): 
            if query == cb[i][0]: 
                check = i 
                t.append(cb[i]) 
                  
    elif choice == 2: 
      query = int( 
      input("Please enter the number of the contact you wish to search: ")) 
      for i in range(len(cb)): 
            if query == cb[i][1]: 
                check = i 
                t.append(cb[i]) 
                  
    elif choice == 3: 
        query = str(input("Please enter the e-mail ID of the contact you wish to search: ")) 
        for i in range(len(cb)): 
            if query == cb[i][2]: 
                check = i 
                t.append(cb[i]) 
    elif choice == 4: 
        query = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY) of the contact you wish to search: ")) 
        for i in range(len(cb)): 
            if query == cb[i][3]: 
                check = i 
                t.append(cb[i]) 
                  
    elif choice == 5: 
      query = str( 
      input("Please enter the category of the contact you wish to search: ")) 
      for i in range(len(cb)): 
            if query == cb[i][4]: 
                check = i 
                t.append(cb[i]) 
            else: 
                    print("Invalid search criteria") 
            return -1
            if check == -1: 
                return -1
            else: 
                display_all(t) 
                return check 
def display_all(cb): 
    if not cb: 
      print("List is empty: []") 
    else: 
        for i in range(len(cb)): 
            print(cb[i]) 
def thanks():
    print("********************************************************************") 
    print("Thank you for using our Smartphone directory system.") 
    print("Please visit again!") 
    print("********************************************************************") 
    sys.exit("Goodbye, have a nice day ") 
    print("....................................................................") 
print("Hello dear user, welcome to our smartphone directory system") 
print("You may now proceed ") 
print("....................................................................") 
ch = 1
cb = initial_contactbook() 
while ch in (1, 2, 3, 4, 5): 
    ch = menu() 
    if ch == 1: 
        cb = add_contact(cb) 
    elif ch == 2: 
        cb = remove_existing(cb) 
    elif ch == 3: 
        cb = delete_all(cb) 
    elif ch == 4: 
        d = search_existing(cb) 
        if d == -1: 
            print("The contact does not exist. Please try again") 
    elif ch == 5: 
        display_all(cb)
    else: 
        thanks() 

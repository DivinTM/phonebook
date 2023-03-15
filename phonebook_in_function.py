def insertion():
    name=input("Enter the name: ")
    if name in phonebook:
        print("Already exist")
    else:
        phoneno=int(input("Enter the phone no.: "))
        phonebook[name]=phoneno
        print("*Save*")

def updation():
    print("1.Name upadate")
    print("2.Phone no. update")
    ch=int(input("Enter your choice: "))
    print("******************")
    if ch==1:
        oldname=input("Enter the old name: ")
        if oldname in phonebook:
            phonenumber=phonebook[oldname]
            phonebook.pop(oldname)
            newname=input("Enter the new name: ")
            phonebook[newname]=phonenumber
            print("*Save*")
        else:
            print("Name not in list")
    if ch==2:
        oldphone=int(input("Enter the old number: "))
        
        for i,j in phonebook.items():
            if oldphone==j:
                newphone=int(input("Enter the new number: "))
                phonebook[i]=newphone
                print("*Save*")
        
def delection():
    deletename=input("Enter the name: ")
    if deletename in phonebook:
        phonebook.pop(deletename)
        print("*Deleted*")
    else:
        print("Name not in contact")

def display():
    if len(phonebook)==0:
        print("*"*20,"","*"*12)
        print("Name"," "*16,"Phone Number")
        print("*"*20,"","*"*12)
        print(" "*8,"*No condacts*")
    else:
        print("*"*20,"","*"*12)
        print("Name"," "*16,"Phone Number")
        print("*"*20,"","*"*12)
        for i,j in phonebook.items():
            print(i," "*(20-len(i)),j)


def exitt():
    exit()
    


phonebook={}
while True:
    print("----------------------------------")
    print("1.Insertion")
    print("2.Updation")
    print("3.Deletion")
    print("4.Display")
    print("5.Exit")
    print("----------------------------------")
    ch=int(input("Enter your choice: "))
    print("----------------------------------")
    


    if ch==1:
        insertion()
        
    elif ch==2:
        updation()

    elif ch==3:
        delection()
        
    elif ch==4:
        display()

    elif ch==5:
        exitt()

    else:
        print("Entered value not matching")
class contact:
    def __init__(self, f_name, l_name, phone_no):
        self.f_name=f_name
        self.l_name=l_name
        self.phone_no=phone_no
    def put_data(self):
        f=open("phonebook1.txt","a")
        f.write(self.f_name+"  |  "+self.l_name+"  |  "+self.phone_no+"\n")
        f.close()
        print("Data entered successfully! ")
          
def get_data():
    f=open("phonebook1.txt","r")
    print("\nThe contents of the file are : ")
    print(f.read())
    f.close()
          

f_name=input("Enter the first name : ")
l_name=input("Enter the last name : ")
phone_no=input("Enter the phone number : ")
c1=contact(f_name,l_name,phone_no)
c1.put_data()
get_data()

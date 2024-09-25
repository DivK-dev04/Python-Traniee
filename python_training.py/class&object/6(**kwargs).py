def student_data(Stud_id, stud_name, stud_class):                                             #normal function 
    print(f"The name of the student is {stud_name} with ID {Stud_id} in class of {stud_class}.")

# student_data(1892563, "NHZ" , "Development")

def stud(stud_id, **kwargs):                                                                  #function using **kwargs arguments
    print(f"Student ID : {stud_id}")                                                          #stud_id is constant , it will print stud_id everytime 
    
    if 'stud_name' in kwargs:                                              #**kwargs when we dont know how many time a key:value arguments are going to come
        print(f"Student Name : {kwargs['stud_name']}")                                        #syntax to use **kwargs in proper way
    
    if 'stud_class' in kwargs:
        print(f"Student Class : {kwargs['stud_class']}")

stud(1234)
print()
stud(123456 , stud_name = "NHZ")                                                               # in key:value format that's why **kwargs
print()
stud(123 , stud_name = "NHZ INDIA" , stud_class = "MCA")
print()
stud(123 , stud_name = "NHZ INDIA Pvt Ltd." , stud_class = "MCA")
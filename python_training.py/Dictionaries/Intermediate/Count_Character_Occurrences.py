# Count Character Occurrences
# Write a function that takes a string and returns a dictionary with each character as a key and its count as the value. For example, for the string "hello", the output should be {'h': 1, 'e': 1, 'l': 2, 'o': 1}.


def occur():
    try:
        a = str(input("Enter Any word : ")).lower()

        if not a.isalpha():                                              #it will only take alphbet not even the space in between
            raise ValueError("Input must be string only.")
        
        if len(a) < 2:
            print("Enter the word more than Two Letters.")

        count = {}
        print(f"Inputted Word by You : {a}")

        for x in a:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        print(count)

    except:
        print("Enter the valid String.")

occur()
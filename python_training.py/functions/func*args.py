def args(*kids):                      #Using *args in Pyhton 
    print("Using *args")
    print("The tallest kids is : ",kids[3])

args("robert","Downey","Jr.","Iron","Man")


def kys(tree1,tree2,tree3):                    #Using keyword Arguments
    print("Tree under plantation : ", tree1)
    print("Tree in Kashmir : ", tree2)
    print("Tree in Nagpur : ",tree3)
kys(tree1 = "Mango" , tree2 = "Apple" , tree3 ="Grapes")
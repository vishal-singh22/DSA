x = eval(input("enter the number: "))  # eval used any types of data types excpect string 

match x:
    # case 1.45:
    #     print("decimal")            #in match case you can used any type of data types 
        
    # case [1,4,7,3]:
    #     print("list")
        
    # case 3+4j:                     # match and case are the soft keywords  and allow to be used to declared
    #     print("complex")
    
    # case True:
    #     print("four")
        
    # case 5:
    #     print("five")
        
    # case _:                       #used default for using '_'
    #     print("invalid")
    
    
    # conditional used by match
    case x if type(x) == int:
        print(f"{x} is integer")
    case x if type(x) == float:
        print(f"{x} is float")
    case x if type(x) == bool:
        print(f"{x} is bool")
    case _:
        print("string")
        
print('we are out now')
        
# This code runs only in python 3.10 or above versions
def number_to_string(arguments):
    match arguments:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"
        case 6:
            return "six"
        case 7:
            return "seven"
        case 8:
            return "eight"
        case 9:
            return "nine"
        case default:
            return "Only Integer Value is allowed"
n=input("enter the value you want: ")
Num_words = ""
rev=n[::-1]
rev=int(rev)
while(rev!=0):
    r=rev%10
    head = number_to_string(r)
    rev=rev//10
    Num_words += head + " "
print(Num_words)   
 
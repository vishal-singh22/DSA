""" 
in this you have only three types of input '(' , ')' and '*' 
write a program string is valid or not 
"""
def check_valid_string(str):
    left_c = 0
    right_c = 0
    
    for c in str:
        if c== "(":
            left_c +=1
            right_c +=1
        
        elif c==")":
            left_c -=1
            right_c -=1
        
        else :
            left_c -=1
            right_c +=1
            
        if right_c < 0:
            return False
        if left_c <0:
            left_c =0
            
    return left_c == 0

test_string = "(*))"
print(check_valid_string(test_string))
            
            
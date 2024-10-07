#s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by 
# inserting "my name is" between "Hello" and "Jane" in s1.

def similarity_check(s1,s2):
    
    words1 = s1.split()
    words2 = s2.split()
    
    if len(words1) > len(words2):
        words1 , words2 = words2, words1
        
    i = 0 
    while i < len(words1) and  words1[i]  == words2[i]:
        i +=1
    
    j = 0  
    while j < len(words2) and words1[-i-j] == words2[-i-j]:
        j +=1
        
    return i+j == len(words1)
    
        
s1 = "Hello Jane" 
s2 = "Hello my name is Jane"

print(similarity_check(s1,s2))

    
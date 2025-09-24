true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]

def calculate_love_score(name1, name2):
    count1 = 0
    count2 = 0
    n1count = 0
    n2count = 0
    
    
    
    for char in name1.lower(): 
        if char in true:
            n1count+= 1
           
    for char in name2.lower():
        if char in true:
            n2count+=1
           
    count1 = n1count + n2count        
    print(count1)  
    n1count = 0
    n2count = 0
    #print(n1count)
    #print(n2count)
    
    for char in name1.lower(): 
        if char in love:
            n1count+=1
          
    for char in name2.lower():
        if char in love:
            n2count+=1
        
    count2 = n1count + n2count        
    print(count2)        
    
    
    print(str(count1) + str(count2))

calculate_love_score("Jay Prakash ", "Nisha Rathod")
   
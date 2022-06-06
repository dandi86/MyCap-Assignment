list1 = [12, -7, 5, 64, -14,] 
  
pos_nos = list(filter(lambda x: (x >= 0), list1))
  
print("Positive numbers in the list: ", *pos_nos) 


list2 = [12, 14, -95, 3] 
  
pos_nos = list(filter(lambda x: (x >= 0), list2))
  
print("Positive numbers in the list: ", *pos_nos) 


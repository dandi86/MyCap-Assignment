def printChar(arr, Len):
 
    # To store the
    occ = {}
    for i in range(Len):
         
        if(arr[i] in occ):
            occ[arr[i]] = occ[arr[i]] + 1
         
        else:
            occ[arr[i]] = 1
  
    # Map's size
    size = len(occ)
  
    # While there are elements in the map
    while (size > 0):
  
        # Finding the maximum value
        # from the map
        currentMax = 0
        arg_max = 0
        for key, value in occ.items():
 
            if (value > currentMax or (value == currentMax and key > arg_max)):
                arg_max = key
                currentMax = value
  
        # Print the character
        # alongwith its frequency
        print(f"{arg_max} - {currentMax}")
  
        # Delete the maximum value
        occ.pop(arg_max)
        size -= 1
 
# Driver code
Str = "Mississippi"
Len = len(Str)
 
 
printChar(list(Str), Len)
 

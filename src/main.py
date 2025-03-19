def add(a, b, c=0):
   try:
     return int(a + b) + int(c)
   except:
     return print("error")
   
add(2, 2) 

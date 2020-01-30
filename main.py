def Vacuume(x):
  return x[::-1]
katz = Vacuume("Sam")
print(katz)
#https://www.w3schools.com/python/python_howto_reverse_string.asp
  
def reverse(y):
    if len(y) == 1: 
        return y 
    else: 
        return reverse(y[1:]) + y[0] 
  
y = "kite"
print (y) 
print (reverse(y)) 
#https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
def greet(name="utilisateur"):
    print(f"bonjour{name}")
##fonction lambda 

sqr=lambda x:x**2
print(sqr(5))

#fonction imbrique et closure
def makemultiplier(n):
   def multiplier(x):
       return x*n
   return multiplier 
times3=makemultiplier(3)
print(times3(10))
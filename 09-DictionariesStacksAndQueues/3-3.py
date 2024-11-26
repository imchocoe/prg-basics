import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   exp=queue.LifoQueue()
   wynik=True
   i=0
   while i<len(expression):
      if expression[i]=="(" or expression[i]=="[" or expression[i]=="{":
         exp.put(expression[i])
      if exp.empty():
         break
      elif  expression[i]==")":
         if exp.get(0)!="(":
            wynik=False
      elif expression[i]=="]":
         if exp.get(0)!="[":
            wynik=False
      elif expression[i]=="}":
         if exp.get(0)!="{":
            wynik=False
      
      i+=1
   return wynik

if brackets_ok(expression1):
   print("Correct")
else:
   print('Incorrect')

if brackets_ok(expression2):
   print("Correct")
else:
   print('Incorrect')

if brackets_ok(expression3):
   print("Correct")
else:
   print('Incorrect')
   


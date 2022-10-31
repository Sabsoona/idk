#For a given string S, write a function to check if it is a palindrome. Taking a single string as its parameter, your function should return True if the given string is a palindrome, else return False 
#(A string is said to be a palindrome if it is the same when read backward).
#idea isaa ro -1 it waviyvano sityva da palidromi tu ra wiricaa gamova anu magalitad ro davwer lo daweros lol
text = input("enter your texst: ")
if text == text[::-1]:
   print('true')
else:
   print('false')
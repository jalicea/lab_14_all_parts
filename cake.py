"""
cake.py
=====
Write a program that asks for cake and handles a yes, no, or anything other than 
yes or no. 
 It will say different things depending on the user's answer.  Here's an example:

Do you want cake?
> yes
Here, have some cake.

Do you want cake?
> no
No cake for you.

Do you want cake?
> blearghhh
I do not understand.
"""

print("Do you want cake?")
res = raw_input(">");
if res == 'yes':
	print ("Have some cake.")
elif res == 'no':
	print("No cake for you.")
elif res != 'yes' and res != 'no':
	print ("Wut?")
"""
name_that_roll.py
=====
Write a program that names the rolls of two dice in a dice game called craps...

* ask the user for the values of two dice rolls.  
* output the name of the roll using Wikipedia's article on Craps
	* http://en.wikipedia.org/wiki/Craps#Rolling
* only check for the following rolls:
	* _Snake Eyes_
	* _Hard Four_ 
	* _Easy Four_  
* print out "I don't know yet" for any other rolls.  Example output:
* example interaction:

What roll did you get for the first die?
> 1
What roll did you get for the second die?
> 1
Snake Eyes!

Press ENTER or type command to continue
What roll did you get for the first die?
> 1
What roll did you get for the second die?
> 3
Easy Four
"""
d1 = raw_input("What roll did you get for the first die?");
d2 = raw_input("What roll did you get for the second die?");

if int(d1) == 1:
	if int(d2) == 1:
		print ("snake eyes")
	if int(d2) == 3:
		print ("Easy four")
elif int(d1) == 3:
		if int(d2) == 1:
			print ("Easy four")
elif int(d1) == 2:
	if int(d2) == 2:
		print ("Hard Four")
else:
	print ("I AM not a smart program")

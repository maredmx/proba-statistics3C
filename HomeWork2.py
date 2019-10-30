#!/usr/bin/env python
# coding: utf-8

# # Excercise 5, More Variables and Printing

# In[5]:


a=24
b='New York'
c='cat'
d='Joseph'
e=13
f=14


# # •Variables inside a string 
# You embed variables inside a string by using a special {} sequence and then put the variable you want inside the {} characters. You also must start the string with the letter f for ”format”,as in f"Hello{somevar}".
# 

# In[6]:


print(f"Let's talk about {d} ")
print(f"He's from {b} ")
print(f"He has a {c} ")
print("his pet is so cute")
print(f"his pet weighs {f} kg")
print(f"They have lived {e} years whit him")
total = a + e + f
print(f"If I add {a}, {e}, and {f} I get {total}.")


# # Excercise 6, More Variables and Printing
# 

# # •f-string
# it is used when we want to save into a string varibe in another varible

# In[10]:


r = 200
f= f"There are {r} pillows in my room" 

t = "Fighting"
e="Sleeping"
y = f"I use part of this for {e} and others for {t}."

print(f)
print(y)
print(f"I said: {r}")
print(f"I also said: '{y}'")

g = True



# # •.format()
# It is used when we want want to apply a format to an already created string

# In[11]:


fut = "Isn't that videogame violence?! {}"
print(fut.format(g))
w = "It isn't a bad videogame..."
que = "actually it is a good one."
print(w + que)


# # Excercise 7, More Printing

# In this exercise, we only declared variables to finally get together and form a simple sentence

# In[15]:


print("Cristian has to go home.")
print("His house is big like a {}.".format('truck'))
print("." * 10) 

abc1 = "h"
abc2 = "e"
abc3 = "l"
abc4 = "l"
abc5 = "o"

abc7 = "f"
abc8 = "r"
abc9 = "i"
abc10 = "e"
abc11 = "n"
abc12 = "d"
abc13 = "s"

print(abc1 + abc2 + abc3 + abc4 + abc5, end=' ')
print(abc7 + abc8 + abc9 + abc10 + abc11 + abc12 + abc13 )


# # Excercise 8, Printing, Printing 

# # •formatter
# Formatters work by putting in one or more replacement fields and placeholders defined by a pair of curly braces {} into a string and calling the .format ()

# In[16]:


formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("Grapes", "Orange", "Banana", "Watermelon"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
   "Let's listen a beautiful song:",
   "My mom loves me a lot, ",
   "But just when I obey her, ",
   "I really want to eat right now"
))


# # Excercise 9, Printing, Printing, Printing 

# # •\n
# The \n is used like the "enter" in our keyboards, is for give us a jump in the text

# In[25]:


firstnumbers = "1 2 3 4 5 6 7 8 9"
firstletters = "\nA \nB \nC \nD \nE \nF"
print("Here are the first numbers: \n", firstnumbers)
print("Here are the first letters : ", firstletters)
print("")


# # Excercise 10, What Was That?

# # •\t
# it is used to simulate indentations

# In[31]:


asx = "\t Hi friends."
bsx = "We're a Rock Band."


# # •\ (backslash)
# It is used to create spaces in a text with a slash, very similar to the comma

# In[27]:


csx = "I \\ don't \\ want to see her."


# # •\t*
# It is used to create the points of a list

# In[33]:



ssx = """
 I make a list for the market:
 \t* Pencil
 \t* Rule
 \t* Sharpener
 \t* Notebooks
 """

print(asx)
print(bsx)
print(csx)
print(ssx)


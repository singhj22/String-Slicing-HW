'''
Created on Oct 22, 2018

@author: Jugat Singh
Python Period 5 even
String Slicing HW
'''

#input from user
string= input("Please enter a String: ")

start = int(input("Please enter the index where you would like to start slicing: "))

stop = int(input("Please enter the index where you would like to stop slicing: "))

access = int(input("Please enter the index of the character you would like to access: "))

#variable
character= string[access]

#display output

print("\nOriginal String: ", string)

print("Length of the String: ",len(string))

print("Substring from index ", start, "to index ", stop, ": ", string[start:stop])

print("Character at index ", access, ": ", character)
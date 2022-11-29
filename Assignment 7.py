#------------------------------------#
# Title: Assignment 7
# Desc: Error Handling and Pickling Demonstration
# Dev: Stephanie Miller
# Date: November 26, 2022
# Change Log: (Who, When, What)
#------------------------------------#

#---------Error Handling-------------#
try:
    y = 100/int(x)
    print(y)
except NameError as e:
    print("X must be defined!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

#---------Pickiling---------------#
import pickle

Task = input("Enter a Task: ")
Priority = input("Enter the Priority: ")
ToDoList = [Task, Priority]

objFile = open("PickleData.dat", "ab")
pickle.dump(ToDoList, objFile)
objFile.close()

objFile = open("PickleData.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()

print(objFileData)


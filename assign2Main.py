# -*- coding: utf-8 -*-

"""

Imported material:
    indexing and searching python files
    os lib

Input:
    Printed the menu using printMenu function
    user selects option from the menu 
    options are  indexing, retrival or exit
    
    if user chose indexing, the name of folder of text files is taken as input
        
Computions:
    using try and except blocks only numbers are taken as input
    
    
    if user chose 1st option that is indexing
    the progarm further import the indexing function run indexing for generating index dic
    and prints index dic
    
    
    if user chose 2nd option that is retrieval
    it takes input as query from user 
    and then pass it as arguement to search function and prints docscore dic for the query
    
    
    if user chose 3rd option
    program ends
    
    while loop breaks when user input option 3
    
    
Output:
    option 1 given index dictionary
    option 2 gives docScores dic for query
"""


# main module
import indexing, searching
import os

def printMenu(): 
    print('-'*4)
    print('Menu')
    print('-'*4)
    print('1. indexing')
    print('2. Retrival')
    print('3. exit')
# the menu for user    


def main():
    """display the menu as follows
    1. indexing 
    2. retrieval 
    """
    printMenu()
    valid = 0
    while(valid == 0):
         try:
             #prompting user for selecting option and checking whether it is a number
            selected_Num = input("Select one option from menu :")
            selected_Num = int(selected_Num)
            # selected_Num is option chose by user here 
            valid = 1
         except ValueError:
                print("Error, Please enter numbers only!")
                
    
                
    while True: # using while loop to give the output untill option selected is 3 and checking if number is in Menu or not.
         
          if selected_Num == 1:
             
              #prompting user for name of folder of text files(subdir)
             print('please put your folder of text files in current working directory')
             subdir = str(input("Enter the name of folder that contains text files:"))
             #getting current working dir (path) and creating a list of files and directories(lyst)  in path
             path = os.getcwd()
             lyst = os.listdir(path)
             #checking if the name of folder given by user is correct or not.
             if subdir in lyst:
                newdir = os.chdir(os.path.join(path,subdir))
                indexing.runIndexing(newdir)
                numDoc = indexing.getNumberofDocument(newdir)
             else:
                 print('Please print correct name of folder')
                 subdir = str(input("Enter the name of folder that contains text files:"))
                    
          elif selected_Num ==2:
              #prompting user for query text
               query = str(input("Enter the query text:"))
               #printing scores for that query in document
               print('-'*28)
               print('Scores for query in documents')
               print('-'*28)
               print(searching.search(query,numDoc))
          
          elif selected_Num ==3:
              # ending program and breaking while loop
               print('-'*12)
               print('program ended')
               print('-'*12)
               break
           
          else:
              print("Please enter only the number given in Menu")#message for entering wrong num
          printMenu()
          valid = 0
          while(valid == 0):
                try:
                   selected_Num= int(input("Select one optiion :"))
                   selected_Num = int(selected_Num)
                   valid =1
                except ValueError:
                    print("Error, Please enter numbers only!")
            
      
main()




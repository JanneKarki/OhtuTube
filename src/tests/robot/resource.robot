*** Settings ***
Library  ../../AppLibrary.py

*** Keywords ***
Input Add Command 
    Input Command  1

Input Exit Command
    Input Command  0
    
Output Text 
    
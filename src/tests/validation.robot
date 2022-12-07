*** Settings ***
Resource  resource.robot
Test Timeout  5


*** Test Cases ***


Add Book Reference With Incorrect Year
    [Documentation]    UI returning error and instructions for correct form 
    Select Add New Book Reference
    Input Valid Author
    Input Valid Title
    Input Year    fff
    Input Valid Year
    Input Valid Publisher
    Input Valid Address
    Reject Manual Id
    Confirm Summary  
    Execute
    Output Should Contain    Error, enter the year like this: 2014

Add Book Reference with Incorrect Author
    Select Add New Book Reference
    Input Author  Metz Cade
    Input Valid Author
    Input Valid Title
    Input Valid Year
    Input Valid Publisher
    Input Valid Address
    Reject Manual Id
    Confirm Summary  
    Execute
    Output Should Contain    Error, enter the author like this: Bond, James

Add Book Reference with Empty Title
    Select Add New Book Reference
    Input Valid Author
    Input Empty Title
    Input Valid Title
    Input Valid Year
    Input Valid Publisher
    Input Valid Address
    Reject Manual Id 
    Confirm Summary  
    Execute
    Output Should Contain    Error, field is empty!

Add Book Reference with Empty Publisher
    Select Add New Book Reference
    Input Valid Author
    Input Valid Title
    Input Valid Year
    Input Empty Publisher
    Input Valid Publisher
    Input Valid Address
    Reject Manual Id
    Confirm Summary  
    Execute
    Output Should Contain    Error, field is empty!

Add Book Reference with Empty Address
    Select Add New Book Reference
    Input Valid Author
    Input Valid Title
    Input Valid Year
    Input Valid Publisher
    Input Empty Address
    Input Valid Address
    Reject Manual Id
    Confirm Summary  
    Execute
    Output Should Contain    Error, field is empty!


*** Keywords ***

Input Valid Author
    Input Author    Metz, Cade

Input Valid Year
    Input Year    2021

Input Valid Title
    Input    Genius makers

Input Empty Title
    Input Title  ${SPACE}

Input Valid Publisher
    Input Publisher    Penguin

Input Empty Publisher
    Input Publisher  ${SPACE}

Input Valid Address
    Input Address    London

Input Empty Address
    Input Address  ${SPACE}
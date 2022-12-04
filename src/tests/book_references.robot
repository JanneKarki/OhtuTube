*** Settings ***
Resource  resource.robot


*** Test Cases ***

Add Book Reference With Correct Inputs
    [Documentation]    UI returning confirmation when reference added succesfully
    Select Add New Book Reference
    Input Correct Book Reference Values 
    Confirm Summary    
    Execute
    Output Should Contain    Added successfully!


Add Book Reference With Incorrect Year
    [Documentation]    UI returning error and instructions for correct form 
    Select Add New Book Reference
    Input Author    Metz, Cade
    Input Title    Genius makers    
    Input Year    fff
    Input Year    2021    
    Input Publisher    Penguin
    Input Address    London     
    Confirm Summary  
    Execute
    Output Should Contain    Error, enter the year like this: 2014

Search Book References With Parameter
    [Documentation]    Search book reference from database with Author
    Save Two Book References
    Select Search
    Input Query   Genius
    Execute
    Entry Should Succeed With Summary
    
See Summary Of The Entry
    [Documentation]    UI displaying summary of the reference entry
    Select Add New Book Reference
    Input Correct Book Reference Values
    Confirm Summary 
    Execute
    Entry Should Succeed With Summary


*** Keywords ***

Input Correct Book Reference Values
    Input Author    Metz, Cade
    Input Title    Genius makers    
    Input Year    2021    
    Input Publisher    Penguin
    Input Address    London    


Save Two Book References
    Select Add New Book Reference
    Input Author    Metz, Cade
    Input Title    Genius makers    
    Input Year    2021    
    Input Publisher    Penguin
    Input Address    London    
    Confirm Summary  
    Select Add New Book Reference
    Input Author    Evans, Claire L.
    Input Title    Broad band
    Input Year    2018
    Input Publisher    Portfolio/Penguin
    Input Address    New York
    Confirm Summary 


Entry Should Succeed With Summary
    Output Should Contain    ${SUMMARY}  


    
    
    
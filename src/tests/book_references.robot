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
    Reject Manual Id
    Confirm Summary  
    Execute
    Output Should Contain    Error, enter the year like this: 2014

Search Book References List Of One Book With Parameter
    [Documentation]    Search book reference from database with Author
    Select Add New Book Reference
    Input Correct Book Reference Values 
    Confirm Summary   
    Select Search
    Input Query   Genius
    Execute
    Output Should Contain    ${SUMMARY1}


Search Book References List Of Several Books With Parameter
    [Documentation]    Search book reference from database with Author
    Save Two Book References
    Select Search
    Input Query   Claire
    Execute
    Output Should Contain    ${SUMMARY1} 
    Output Should Contain    ${SUMMARY2} 
    
See Summary Of The Entry
    [Documentation]    UI displaying summary of the reference entry
    Select Add New Book Reference
    Input Correct Book Reference Values
    Confirm Summary 
    Execute
    Entry Should Succeed With Summary

Add Book Reference With Manually Written Id
    [Documentation]    Test sets reference id manually
    Select Add New Book Reference
    Input Author    Metz, Cade
    Input Title    Genius makers    
    Input Year    2021    
    Input Publisher    Penguin
    Input Address    London
    Accept Manual Id
    Input ReferenceID    mcg21
    Confirm Summary
    Execute
    Output Should Contain    Added successfully!


*** Keywords ***

Input Correct Book Reference Values
    Input Author    Metz, Cade
    Input Title    Genius makers    
    Input Year    2021    
    Input Publisher    Penguin
    Input Address    London
    Reject Manual Id 


Save Two Book References
    Select Add New Book Reference
    Input Author    Metz, Cade
    Input Title    Genius makers    
    Input Year    2021    
    Input Publisher    Penguin
    Input Address    London
    Reject Manual Id
    Confirm Summary  
    Select Add New Book Reference
    Input Author    Evans, Claire L.
    Input Title    Broad band
    Input Year    2018
    Input Publisher    Portfolio/Penguin
    Input Address    New York
    Reject Manual Id
    Confirm Summary 

    
    
    
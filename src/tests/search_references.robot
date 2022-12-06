*** Settings ***
Resource  resource.robot

*** Variables ***
${Lastname}    Metz
${Author}    Evans, Claire L.
*** Test Cases ***

Search Book References List Of One Book With Parameter
     [Documentation]    Search book reference from database with Lastname
    Save Two Book References
    Select Add New Book Reference
    Input Correct Book Reference Values 
    Confirm Summary   
    Execute
    Search Output Should Contain Value With Parameter   Metz, Cade    ${Lastname}

Search Book References List Of Several Books With Parameter
    [Documentation]    Search book reference from database with Author
    Save Two Book References
    Select Search
    Input Query   Evans
    Execute
    Search Output Should Contain Value With Parameter    ${author}    ${author}


*** Keywords ***

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

Input Correct Book Reference Values
    Input Author  Metz, Cade
    Input Title  Genous makers
    Input Year  2021
    Input Publisher  Penguin
    Input Address  London
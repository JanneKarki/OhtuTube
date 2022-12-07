*** Settings ***
Resource  resource.robot

*** Test Cases ***

Bibtex File Is Created
    Select Add New Book Reference
    Input Book Reference
    Confirm Summary
    Select Create Bibtex
    Execute
    Output Should Contain  Bibtex-file created!

*** Keywords ***

Input Book Reference
    Input Author    Metz, Cade
    Input Title    Genius makers    
    Input Year    2021    
    Input Publisher    Penguin
    Input Address    London    

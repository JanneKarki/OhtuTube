*** Settings ***
Resource  resource.robot

*** Variables ***
${AuthorMetz}    Metz, Cade
${ColumnAuthor}    author

*** Test Cases ***
Import References From Bibtex File
    Create Bibtex File
    Select Empty Database
    Confirm
    Database Should Be Empty
    Select Import References
    Search Output Should Contain Value With Parameter    ${AuthorMetz}    ${AuthorMetz}    ${ColumnAuthor}
    Execute

*** Keywords ***

Create Bibtex File
    Select Add New Book Reference
    Input Book Reference
    Confirm Summary
    Select Create Bibtex

Input Book Reference
    Input Author    Metz, Cade
    Input Title    Genius makers    
    Input Year    2021    
    Input Publisher    Penguin
    Input Address    London
    Reject Manual Id
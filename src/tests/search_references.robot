*** Settings ***
Resource  resource.robot

*** Variables ***
${LastnameMetz}    Metz
${AuthorEvans}    Evans, Claire L.
${AuthorMetz}    Metz, Cade
${Year2021}    str(2021)
${Title}
${ColumnAuthor}    author
${ColumnTitle}    title
${ColumnYear}    year
${ColumnPublisher}    publisher
${ColumnAddress}    address



*** Test Cases ***


Search Book References List Of Several Books With Author
    [Documentation]    Search book reference from the database with Author
    Save Four Book References
    Execute
    Search Output Should Contain Value With Parameter    ${AuthorEvans}    ${AuthorEvans}    ${ColumnAuthor}
     Search Output Should Not Contain Unmatching Results    ${AuthorEvans}    ${AuthorEvans}    ${ColumnAuthor}

Search Book References with Lastname
    [Documentation]    Search book reference from the database with Lastname
    Save Four Book References 
    Execute
    Search Output Should Contain Value With Parameter   ${AuthorMetz}    ${LastnameMetz}    ${ColumnAuthor}
    Search Output Should Not Contain Unmatching Results    ${AuthorMetz}    ${LastnameMetz}    ${ColumnAuthor}

Search Book References with Year
    [Documentation]    Search book reference from the database with Year
    Save Four Book References 
    Execute
    Search Output Should Contain Value With Parameter   ${Year2021}    ${Year2021}     ${ColumnYear}
    Search Output Should Not Contain Unmatching Results    ${Year2021}     ${Year2021}     ${ColumnYear}


*** Keywords ***

Save Four Book References
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
    Select Add New Book Reference
    Input Author    Sipser, Michael
    Input Title    Introduction To The Theory Of Computation
    Input Year    1997
    Input Publisher    PWS
    Input Address     Massachusetts
    Confirm Summary
    Select Add New Book Reference
    Input Author    Laaksonen, Antti
    Input Title    Tirakirja
    Input Year    2021
    Input Publisher    Self-publishing
    Input Address    Helsinki
    Confirm Summary

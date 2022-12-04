*** Settings ***
Library  ../ReferencesLibrary.py

*** Variables ***
# tämä ei ole nyt toimiva saati oikein 
#${SUMMARY} =metz2021${SPACE*6}| Metz, Cade${SPACE*10}| Genius makers${SPACE*10}| 2021${SPACE*3}| Penguin${SPACE*12}| London${SPACE*12}


*** Keywords ***
Input Exit Command
    Input    0

Execute
    Input Exit Command
    Start App

Select Add New Book Reference
    Input    1

Select Search
    Input    3
    


Confirm Summary
    Input    y

Input Author
    [Arguments]  ${author} 
    Input  ${author}

Input Title
    [Arguments]  ${title} 
    Input  ${title}

Input Year
    [Arguments]  ${year} 
    Input  ${year}

Input Publisher
    [Arguments]  ${publisher} 
    Input  ${publisher}

Input Address
    [Arguments]  ${address} 
    Input  ${address}

Input ReferenceID
    [Arguments]  ${id} 
    Input    ${id}

Input Book Reference
    Input Author
    Input Title
    Input Year
    Input Publisher
    Input Address
    Input ReferenceID

Input Query
    [Arguments]  ${query} 
    Input    ${query}

# Entry Should Succeed With Summary
#     Output Should Contain    metz2021      | Metz, Cade          | Genius makers                | 2021   | Penguin            | London
            
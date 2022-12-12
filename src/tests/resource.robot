*** Settings ***
Library  ../ReferencesLibrary.py

*** Variables ***
${SUMMARY1}     ${SPACE}${SPACE}${SPACE} NO ${SPACE}${SPACE}| metz2021geni ${SPACE}| Metz, Cade ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE}| Genius makers ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE}| 2021 ${SPACE} | Penguin ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE}| London ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE}
${SUMMARY2}     ${SPACE}${SPACE}${SPACE} NO ${SPACE}${SPACE}| evan2018broa ${SPACE}| Evans, Claire L. ${SPACE} ${SPACE}| Broad band ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE} | 2018 ${SPACE} | Portfolio/Penguin ${SPACE}| New York ${SPACE} ${SPACE} ${SPACE} ${SPACE} ${SPACE}


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
    
Select Create Bibtex
    Input    5

Select Empty Database
    Input    8

Select Import References
    Input    6

Confirm
    Input    y

Confirm Summary
    Input    y

Accept Manual Id
    Input    y

Reject Manual Id
    Input    n

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

Entry Should Succeed With Summary
    Output Should Contain    ${SUMMARY1}  
*** Settings ***
Resource  resource.robot
Test Setup  Run Application

*** Test Cases ***

# As a user, I can add book-reference to the app
Add New Book Reference
    Input Add Command
    Set Author  Metz, Cade
    Set Title  Genius makers
    Set Year  2021
    Set Publisher  Penguin
    Set Address  London
    Set ReferenceID  metz2021
    # Entry Should Succeed With Summary  
    # Should Ask For Confirmation
    Input Command  y
    Entry Should Succeed With Message  Added successfully!



Exit Application
    Input Exit Command



*** Keywords ***

Set Author
    [Arguments]  ${author}
    Input Text  > Author (Last name, First name):  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  > Title:  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  > Year:  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  > Publisher:  ${publisher}

Set Address
    [Arguments]  ${address}
    Input Text  > Address:  ${address}

Set ReferenceID
    [Arguments]  ${referenceID}
    Input Text  > Create a unique reference id:  ${referenceID}


Entry Should Succeed With Summary
    [Arguments]  ${referenceID} ${author} ${title} ${year} ${publisher} ${address}
    Output Should Contain   # what

Entry Should Succeed With Message
    [Arguments]  ${message}
    Output Should Contain  ${message}


    


    
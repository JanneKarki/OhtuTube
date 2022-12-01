*** Settings ***
Library  ../ReferencesLibrary.py


*** Keywords ***
Add Book Reference
    [Arguments]  ${menu}  ${author}  ${title}  ${year}  ${publisher}  ${address}  ${id}  ${yes}  ${exit}
    Input  ${menu}
    Input  ${author}
    Input  ${title}
    Input  ${year}
    Input  ${publisher}
    Input  ${address}
    Input  ${id}
    Input  ${yes}
    Input  ${exit}
    Start App


Collect Book Inputs
    [Arguments]  ${menu}  ${author}  ${title}  ${year}  ${publisher}  ${address}  ${id}  ${yes}  ${exit}
    Input  ${menu}
    Input  ${author}
    Input  ${title}
    Input  ${year}
    Input  ${publisher}
    Input  ${address}
    Input  ${id}
    Input  ${yes}
    Input  ${exit}
    Start App
    
##


# Add Book Reference
#     [Arguments]  ${menu}  ${author}  ${title}  ${year}  ${publisher}  ${address}  ${id}  ${yes}  ${exit}
#     Book Inputs  ${menu}  ${author}  ${title}  ${year}  ${publisher}  ${address}  ${id}  ${yes}  ${exit}







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

Book Reference Inputs
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}  ${address}  ${id}
    Input Author
    Input Title
    Input Year
    Input Publisher
    Input Address
    Input ReferenceID

Entry Should Succeed With Summary
    Output Should Contain    Reference ID  | Author              | Title                        | Year   | Publisher          | Address 
    # Output Should Contain    ${id}    ${author}    ${title}    ${year}    ${publisher}    ${address}
    # Output Should Contain    ${id:13} | ${author:19} | ${title:28} | ${year:6} | ${publisher:18} | ${address:18}                
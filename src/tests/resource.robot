*** Settings ***
Library  ../ReferencesLibrary.py


*** Keywords  ***
Book Inputs
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
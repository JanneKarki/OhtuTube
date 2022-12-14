*** Settings ***
Resource  resource.robot
Test Timeout  5


*** Test Cases ***

Change Language
    Select Change Language
    Execute
    Output Should Contain    Changing language to finnish

Change Language Changes Ui Language
    Select Change Language
    Execute
    Output Should Contain     \n Sovellus sulkeutuu
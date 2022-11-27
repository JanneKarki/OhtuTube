*** Settings ***
Resource  resource.robot
Test Setup  Run Application

*** Test Cases ***
Exit Application
    Input Exit Command
    
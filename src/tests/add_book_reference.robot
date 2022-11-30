*** Settings ***
Resource  resource.robot



*** Test Cases ***
Add Book Reference
    Book Inputs  1  Seppo, Taalasmaa  Salattu  1212  WSOY  AA  9232  y  0
	Output Should Contain  Added successfully!
	



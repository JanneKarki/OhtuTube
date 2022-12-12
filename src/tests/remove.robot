*** Settings ***
Resource  resource.robot

*** Variables ***


${Idecm18}    ecm18
${AuthorEvans}    Evans, Claire L.
${Year2018}    str(2018)
${TitleBroadBand}    Broad band
${PublisherPenguin}    Penguin
${AddressNewYork}    NewYork
${SelectedFalse}    False

${Idmcg21}    mcg21
${AuthorMetz}    Metz, Cade
${Year2021}    str(2021)
${TitleGeniusMakers}    Genius makers
${PublisherPenguin}    Penguin
${AddressLondon}    London
${SelectedTrue}    True

${columnId}    id
${ColumnAuthor}    author


*** Test Cases ***

Remove Selected Reference From The Database
    Select Empty Database
    Confirm
    Database Should Be Empty
    Add Book Reference    ${Idecm18}    ${AuthorEvans}    ${TitleBroadBand}    ${Year2018}   ${PublisherPenguin}    ${AddressNewYork}    ${SelectedFalse}
    Add Book Reference    ${Idmcg21}    ${AuthorMetz}     ${TitleGeniusMakers}    ${Year2021}     ${PublisherPenguin}    ${AddressLondon}     ${SelectedTrue}
    Search Output Should Contain Value With Parameter    ${AuthorMetz}    ${AuthorMetz}    ${ColumnAuthor}
    Select Remove Reference
    Confirm
    Execute
    Reference Not In Database    ${AuthorMetz}    ${ColumnAuthor}

*** Keywords ***

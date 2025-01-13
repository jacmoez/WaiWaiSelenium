*** Settings ***
Library                         SeleniumLibrary


*** Variables ***
${url}                          https://testautomationpractice.blogspot.com/
${newtab}                       //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[4]/div[1]/button

${mobile}                       //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[6]/div[1]/div/div/a[1]

${double_click}                 //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[7]/div[1]/button

*** Keywords ***
Search Text
    Input Text                  id:Wikipedia1_wikipedia-search-input            Myanmar
    Sleep                       3
    Click Button                class:wikipedia-search-button
    Sleep                       2
    ${elemnets}=                Get Web Elements                        xpath:/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/div[2]/div[2]/a
    Sleep                       2
    #Click Element               ${elemnets}[0]


    Click Button               name:start
    Sleep                      2
    Click Button               id:alertBtn
    Sleep                      2
    Handle Alert
    Click Button               id:confirmBtn
    Handle Alert               accept
    ${ok}                      Get Text                     id:demo
    Log                        ${ok}
    Click Button               id:confirmBtn
    Handle Alert               dismiss
    ${cancel}                  Get Text                     id:demo
    Log                        ${cancel}

New Tab
    Click Button              ${newtab}
    Sleep                       2
    ${handles}=                Get Window Handles
    Switch Window              ${handles}[1]
    Sleep                      2
    Close Window
    Switch Window              ${handles}[0]
    Sleep                      2
    #Click Button               id:PopUp
    Sleep                      2
    Click Button               class:dropbtn
    Sleep                      2

    Scroll Element Into View               ${mobile}
    Sleep                       2
    Click Element               ${mobile}
    Scroll Element Into View               ${double_click}
    Sleep                       2
    Double Click Element                     ${double_click}



*** Test Cases ***
Main
    Open Browser                ${url}                 browser=Chrome
    Maximize Browser Window
    Search Text
    New Tab
    Sleep                       5


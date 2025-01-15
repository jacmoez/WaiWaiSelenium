*** Settings ***
Library                 SeleniumLibrary


*** Variables ***

${url}              https://testautomationpractice.blogspot.com/
${home}             //html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div/ul/li[1]/a

${hidden}           //html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div/ul/li[2]/a

${download}         //html/body/div[3]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div/ul/li[3]/a

${download_pdf}    //html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div[1]/div[2]/button[3]

${youtube}         //html/body/div[3]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[2]/div/div/div[1]/a


*** Keywords ***
Form Test
#     Input Text             id:input1               Wai Wai
#     Sleep                  3
#     Click Button           id:btn1
#     Sleep                  3
#     Input Text            name:input2              Swe Swe
#     Sleep                  3
#     Click Button           btn2

     ${elements}         Create List            Wai Wai     Swe Swe       San San

     FOR     ${i}          IN RANGE             0       3
            ${count}=       Evaluate            ${i} + 1
            Input Text      id:input${count}       ${elements}[${i}]
            Sleep           3
            Click Button    id:btn${count}
    END
    Sleep                   3
    Click Element           ${home}
    Sleep                   3
    Click Element           ${hidden}
    Sleep                   3


Download Files
    Click Element          ${download}
    Sleep                   3
    Input Text             id:inputText             QA Wai Wai
    Sleep                   3
    Click Button            id:generateTxt
    Sleep                   3
    Click Element          id:txtDownloadLink
    Sleep                   3
    Click Button            id:generatePdf
    Sleep                   3
    Click Element           id:pdfDownloadLink
    Sleep                   3
    Click Button            ${download_pdf}
    Sleep                   3

    Input Text              //input[1]           Wai Wai
    Click Element           ${youtube}

*** Test Cases ***
Main
    Open Browser            ${url}              browser=Chrome
    Maximize Browser Window
    Form Test
    Download Files
    Sleep                   5

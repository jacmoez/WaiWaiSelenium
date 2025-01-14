*** Settings ***
Library                 SeleniumLibrary


*** Variables ***

${url}              https://testautomationpractice.blogspot.com/
${silder1}          //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[9]/div[1]/div/span[1]

${silder2}          //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[9]/div[1]/div/span[2]

${drop_down}        //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[11]/div[1]/div/div[5]

${erro_code1}       //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[12]/div[1]/div/div[3]/a[1]

${hidden}          //html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div[2]/div/ul/li[2]/a


*** Keywords ***
Drag Drop Item
        Sleep               3
       Drag And Drop        id:draggable                id:droppable
       Sleep                5

Slider
      Drag and Drop By offset       ${silder1}          -75     0
#      Drag and Drop By offset       ${silder1}           70     0
      Drag and Drop By offset       ${silder2}          -175   0
      Drag and Drop By offset       ${silder2}          100    0

      Sleep                 5


Drop Down Items
       Input Text                   id:comboBox             Item 5
        Sleep                       5
       Click Element                ${drop_down}
       Sleep                        3
       Click Element                id:apple
       Sleep                        5
       Execute JavaScript           window.history.back()
       Sleep                        3
#       Click Element                id:dell
#       Sleep                        5
#       Execute JavaScript           window.histrory.back()
#       Sleep                        5



Broken List
       FOR   ${i}      IN RANGE    1        8
                    Click Element          //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[12]/div[1]/div/div[3]/a[${i}]
                    Sleep              2
                    ${title}=         Get Title
                    Log               ${title}
                    Execute JavaScript          window.history.back()
       END

Hidden Element And Ajax
       Click Element               ${hidden}
       Sleep                        5

*** Test Cases ***
Main
    Open Browser            ${url}              browser=Chrome
    Maximize Browser Window
    Drag Drop Item
    #Slider
    Drop Down Items
    Broken List
    Hidden Element And Ajax




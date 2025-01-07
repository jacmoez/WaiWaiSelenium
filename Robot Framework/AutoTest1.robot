*** Settings ***
Library                         SeleniumLibrary



*** Variables ***
${url}                          https://testautomationpractice.blogspot.com/
${img1}                         C:\\Users\\DELL\\Pictures\\backgound.jpeg
${img2}                         C:\\Users\\DELL\\Pictures\\Screenshots\\Screenshot 2024-12-28 003144.png
${img3}                         C:\\Users\\DELL\\Pictures\\Screenshots\\Screenshot 2024-12-20 224403.png

${multifile}                    xpath:/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[2]/div[1]/form[2]/button


*** Keywords ***
Input Field Test
        Open Browser            ${url}               browser=Chrome
        Maximize Browser Window
        Sleep                   2s
        Input Text              id=name              QA
        Sleep                   2s
        Clear Element Text      id=name
        Sleep                   2s
#       Input Text              css:input[placeholder='Enter Name']     QA Wai Wai

        ${elements}=            Get WebElements       css:input[placeholder^='Enter']

        ${user_data}=           Create List           QA        qa@ams.com.mm   09778656503

        FOR    ${i}             IN RANGE               0        3
                                Input Text            ${elements}[${i}]        ${user_data}[${i}]
                                Sleep                 2s
        END
        Input Text              id=textarea           Yangon, Myanmar.
        Sleep                   2s


Radio Test
       Click Element            css:input[value='female']
       Sleep                    2s

Checkbox Test
#       Click Element            id=monday
#       Sleep                    2s
#       Click Element            xpath=//*[@id="tuesday"]
#       Sleep                    2s
#       Click Element            css:input[value='friday']
#       Sleep                    2s
        ${days}=                 Create List        monday      tuesday      thursday       friday      saturday
        FOR                     ${i}                IN RANGE    0   5
                                Click Element       id=${days}[${i}]
                                Sleep               2s
        END

Select Text
#        Select From List By Index                  id=country           1
         Select From List By Value                  id=country         japan
         Sleep                                      2s
         Select From List By Value                  id=colors          green
         Sleep                                      2s
         Select From List By Value                  id=animals         dog      cat
         Sleep                                      2s

Date Picker Test
        Input Text                                  id=datepicker      11/04/1998
        Sleep                                       2s
        Press Keys                                  id=datepicker       RETURN
        Sleep                                       2s
        Click Element                               id:txtDate
        Sleep                                       2s
        Select From List By Value                   xpath:/html/body/div[5]/div/div/select[2]           2019
        Sleep                                       2s
        Select From List By Value                   xpath:/html/body/div[5]/div/div/select[1]           2
        Sleep                                       2s
        Click Element                               xpath:/html/body/div[5]/table/tbody/tr[3]/td[5]/a
        Sleep                                       2s
        Input Text                                  id:start-date        11/04/1998
        Sleep                                       2s
        Input Text                                  id:end-date           01/07/2025
        Sleep                                       2s
        Click Element                               class:submit-btn
        Sleep                                       2s
        ${result}=                                  Get Text               id:result
        Log                                         ${result}
        Click Element                               class:home-link
        Sleep                                       2s

File Upload
       Choose File                                  id:singleFileInput      C:\\Users\\DELL\\Pictures\\backgound.jpeg
       Sleep                                        2s
       Click Element                                xpath:/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[2]/div[1]/form[1]/button

       Sleep                                        2s
       Choose File                                  id:multipleFilesInput       ${img1}\n ${img2}\n ${img3}
       Sleep                                        2s
       Click Element                                ${multifile}
       Sleep                                        5s

Table Data
       Table Data By Name                           BookTable
       #Table Data By ID                             taskTable

Table Data By Name
       [Arguments]                                  ${table_name}
       @{cells}=                                    Get WebElements             xpath://table[@name='${table_name}']//td
       FOR             ${cell}    IN                @{cells}
                       ${text}=   Get Text          ${cell}
       END

       @{rows}=                                     Get WebElements              xpath://table[@name='${table_name}']//td
       FOR             ${row}    IN                 @{rows}
                       ${row_elements}=             Get WebElements              ${row}
                       ${text}=                     Get Text                     ${row_elements}
                       Log                          ${text}
       END


*** Test Cases ***
Main
   Input Field Test
#    Radio Test
#    Checkbox Test
#    Select Text
#    Date Picker Test
#    File Upload
    Table Data
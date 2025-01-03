*** Settings ***
Library                         SeleniumLibrary



*** Variables ***
${url}                          https://testautomationpractice.blogspot.com/


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


*** Test Cases ***
Main
    Input Field Test
    Radio Test
    Checkbox Test
    Select Text

*** Settings ***
Library                         SeleniumLibrary





*** Variables ***
${url}                          https://testautomationpractice.blogspot.com/


*** Keywords ***
Table Data
      Table Data By Name                       BookTable
      Table Data By ID                         taskTable



Table Data By Name

  [Arguments]                                  ${table_name}
#First Way
       @{cells}=                                    Get WebElements             xpath://table[@name='${table_name}']//td
       FOR             ${cell}    IN                @{cells}
                       ${text}=   Get Text          ${cell}
                       Log                          ${text}
       END

#Second Way
  @{rows}=                                    Get WebElements               xpath://table[@name='${table_name}']//tr
        FOR           ${row}      IN                @{rows}
                      ${row_elements}=              Get WebElements         ${row}
                      ${text}=                      Get Text                ${row_elements}
                      Log                           ${text}
        END

Table Data By ID
       [Arguments]                              ${table_id}
       @{cells}=       Get WebElements          xpath://table[@id='${table_id}']//td
       FOR             ${cell}      IN          @{cells}
                       ${text}=    Get Text     ${cell}
                       Log                      ${text}
       END


Get Pagination Table Data First
        ${rows}=        Get WebElements         xpath://table[@id='productTable']//td
       FOR           ${row}      IN                @{rows}
                            ${row_elements}=              Get WebElements         ${row}
                            ${text}=                      Get Text                ${row_elements}
                            Log                           ${text}
       END

*** Test Cases ***
Main
   Open Browser            ${url}               browser=Chrome
   Maximize Browser Window
   Sleep                   2s
   Table Data
   Get Pagination Table Data First

*** Settings ***
Library                         SeleniumLibrary



*** Variables ***
${url}                          https://testautomationpractice.blogspot.com/


*** Keywords ***
Table Data
    Get Pagination Table Data First
    Get Pagination Table Data All
    #Pagination Web Table
    Click checkbox For One Page


Get Pagination Table Data First
       @{rows}=           Get WebElements                   xpath://table[@id='productTable']/tbody/tr
       FOR                ${row}        IN                  @{rows}
                          ${row_elements}=                  Get WebElements                 ${row}
                          ${text}=                          Get Text                        ${row_elements}
                          Log                               ${text}
       END

       Sleep               2s

Pagination Web Table
       @{elements}=         Get WebElements                 xpath://ul[@id='pagination']/li/a
       Sleep                2s
       FOR                  ${element}    IN                @{elements}
                            Click Element                    ${element}
                            Sleep                            3s
       END

Get Pagination Table Data All
      ${elements}=          Get WebElements                //ul[@id='pagination']/li/a
      FOR                   ${element}     IN               @{elements}
                            Click Element                   ${element}
                            Sleep                            2s
                            ${rows}=                        Get WebElements             //table[@id='productTable']/tbody/tr
      FOR                   ${row}         IN               @{rows}
                            ${row_elements}=                Get WebElements         ${row}
                            ${text}=                        Get Text                 ${row_elements}
                            Log                             ${text}
    END
    END

Click checkbox For One Page
     FOR                ${i}             IN RANGE           1                   6
                                         Click Element      //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[${i}]/td[4]/input
                       Sleep            2s
     END

Click Checkbox For All Page
    ${elements}=            Get WebElemnets                 //ul[@id='pagination']/li/a
    FOR                      ${element}      IN             @{elements}
                             Click Element                   ${element}
                             Sleep                            2s
    FOR                 ${i}    IN RANGE                      1             6
                             Click Element                    //html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[${i}]/td[4]/input
                             Sleep                             3s
    END
    END


*** Test Cases ***
Main
   Open Browser            ${url}               browser=Chrome
   Maximize Browser Window
   Sleep                   2s
   Table Data
*** Settings ***
Library                 SeleniumLibrary

*** Variables ***
${url}                                   https://webfront-uat.yogamovement.com/
${browser}                               Edge
${close_alert}                           css:.modal__btn-close.click-efx.circle.animated
${register}                              //*[@id="header"]/div[2]/div/div/nav[1]/ul/li[1]/a
${register_btn}                          //html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button
${femal}                                 //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[2]/label/div/div
${lastname}                              //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input
${country}                              //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div
${contry_search}                       //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[1]/input
${myanmar}                            //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[4]

${year}                             1998
${month}                            10
${day}                                 //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/div[4]
${country_img}                      xpath:img[@src="https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-th.png"]

*** Keywords ***
Register User
     Sleep                           3
     Click Element                   ${register}
     Sleep                           3
     Input Text                      name:email              wai21@yopmail.com
     Sleep                           3
     Input Text                      name:password            wai123
     Sleep                           3
     Click Button                   ${register_btn}
     Sleep                           5
     Input Text                     name:firstname                QA
     Sleep                            4
     Input Text                     ${lastname}                 Wai Wai
     Sleep                           3
     Click Element                  ${country}
     Sleep                            3
     Input Text                     ${contry_search}            Myanmar
     Sleep                           3
     Click Element                  ${myanmar}
     Sleep                           2
     Input Text                     name:mobile                 988766565
     Sleep                            2
     Click Element                 id:dob
     Sleep                          2
     #year
     Click Element                 xpath://select[2]/option[@value='${year}']
     Sleep                          2
     Select From List By Value     xpath://select[2]            ${year}
     Sleep                          2
     Select From List By Value    xpath://select[1]             ${month}
     Sleep                          2
    Click Element                ${day}
     Sleep                          3
     Click Element               ${femal}
    Sleep                           2
    Click Element               class:css-egispl
    Sleep                           2
    Click Element               xpath://img[@src="https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-th.png"]
    Sleep                           2
    Click Button                //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[6]/div/button




*** Test Cases ***
Main
    Open Browser                ${url}                      ${browser}
    Maximize Browser Window
    Sleep                       3
    Click Button                ${close_alert}
    Register User
    Sleep                       5
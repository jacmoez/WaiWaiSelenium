*** Settings ***
Library         SeleniumLibrary

Suite Setup       Open Browser      ${url}     ${browser}
Suite Teardown    Close Browser

*** Variables ***
${url}           https://www.saucedemo.com/
${browser}       Chrome


*** Test Cases ***
Login With Valid
    Maximize Browser Window
    Input Text      id=user-name        standard_user
    Sleep           2s
    Input Text      id=password         secret_sauce
    Sleep           2s
    PressKeys       id=user-name        ENTER
    Sleep           2s

Check Inventory Page
        Page Should Contain     Products
        Sleep                   2s

Add Item To Cart
        Click Button            id=add-to-cart-sauce-labs-backpack
        Sleep                   2s
        Click Button            name=add-to-cart-sauce-labs-fleece-jacket
        Sleep                   2s
        Click Button            xpath=//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]
        Sleep                   2s
        Click Button            id=remove-test.allthethings()-t-shirt-(red)
        Sleep                   2s

View Cart
       Click Element            class=shopping_cart_link
       Sleep                    2s
       Page Should Contain      Your Cart
       Click Element            class=inventory_item_name
       Sleep                    2s
       Click Button             id=remove
       Sleep                    2s
       Click Element            class=shopping_cart_link
       Sleep                    2s


Checkout Information
     Click Button               id=checkout
     Sleep                      2s
     Input Text                 id=first-name       QA
     Sleep                      2s
     Input Text                 id=last-name        Wai Wai
     Sleep                      2s
     Input Text                 id=postal-code      1111
     Sleep                      2s
     Click Button               id=continue
     Sleep                      2s

Verify Payment
     ${item_total}=             Get Text            class=summary_subtotal_label
     ${tax_total}=              Get Text            xpath=/html/body/div/div/div/div[2]/div/div[2]/div[7]
     ${total_price}=            Get Text            class=summary_total_label
     Sleep                      2s
     Log                        Item Total: ${item_total}
     #Log                        Tax:  ${tax_total}
     Log                        Total Price: ${total_price}

Finish Checkout

         Click Button           css=.btn.btn_action.btn_medium.cart_button
         Sleep                  5s
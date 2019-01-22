# -*- coding: utf-8 -*-
from random import randint
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    
    minIngredients = 4
    maxIngredients = 5
    minBurgers = 2
    maxBurgers = 6

    driver = webdriver.Firefox()
    driver.get("http://localhost:8080/#/")
    assert "Max Hamburgare" in driver.title
    elem = driver.find_element_by_id("createBurgerButton")
    elem.click()
    placeOrder(minBurgers, maxBurgers, minIngredients, maxIngredients, driver)
                
    driver.close()
    driver.quit()
    return

def placeOrder(
    minBurgers,
    maxBurgers,
    minIngredients,
    maxIngredients,
    driver):

    "Bestäm ett intervall av burgare och intervall av ingredienser"
    
    nrOfBurgers = randint(minBurgers,maxBurgers)
    print('Antal burgare: ' + str(nrOfBurgers))

    for index in range(0, nrOfBurgers):
        print('Påbörjar burgare ' +str(index+1))
        selectIngredients(minIngredients,maxIngredients, driver)
        print('Burgare ' + str(index+1) + ' klar')

        elem = driver.find_element_by_id('next-btn')
        elem.location_once_scrolled_into_view
        elem.click()

        elem = driver.find_elements_by_xpath("//input")[-1]
        randamount=randint(1,3)
        elem.clear()
        elem.send_keys(str(randamount))

        if index!=(nrOfBurgers-1):
            elem = driver.find_element_by_id('add-btn-div')
            elem.location_once_scrolled_into_view
            elem.click()
            elem = driver.find_element_by_id("createBurgerButton")
            elem.click()
            
    elem = driver.find_element_by_id('order-btn2')
    elem.location_once_scrolled_into_view
    elem.click()
            
    return

def selectIngredients(
    minIngredient,
    maxIngredient,
    driver):
    "Väljer ut ingredienser"

    nrOfIngredients = randint(minIngredient,maxIngredient)
    print('Antal ingredienser: ' + str(nrOfIngredients))

    allPlusButtons = driver.find_elements_by_class_name('PlusButton')
    forcePatty(driver,allPlusButtons[1])
    buttonsIndex=len(allPlusButtons)-1

    for x in range(0,nrOfIngredients):
        print('Ingrediens ' + str(x+2) + ' väljs' )
        while True:
            try:
                button=allPlusButtons[randint(0,buttonsIndex)]
                button.location_once_scrolled_into_view
                time.sleep(0.1)
                button.click()
                break
            except:
                print('Väljer ny knapp')

        print('Klickat på +')
        ingredients=driver.find_elements_by_class_name('ing-in-mod')
        numOfIngredients=len(ingredients)
        randIngredient = ingredients[randint(0,numOfIngredients-1)]
        print('Valt ingrediens')
        randIngredient.location_once_scrolled_into_view
        time.sleep(0.1)
        randIngredient.click()
        time.sleep(0.5)
        
    return

def forcePatty(driver,pattyButton):
    print('Tvingar ingrediens 1 som patty')
    pattyButton.click()
    ingredients=driver.find_elements_by_class_name('ing-in-mod')
    numOfIngredients=len(ingredients)
    randIngredient = ingredients[randint(0,numOfIngredients-1)]
    print('Valt ingrediens')
    randIngredient.location_once_scrolled_into_view
    time.sleep(0.1)
    randIngredient.click()
    time.sleep(0.5)
    return

main()

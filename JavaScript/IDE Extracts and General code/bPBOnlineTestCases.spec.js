// Generated by Selenium IDE
const { Builder, By, Key, until } = require('selenium-webdriver')
const assert = require('assert')

describe('BPB Online Test Cases', function() {
  this.timeout(30000)
  let driver
  let vars
  beforeEach(async function() {
    driver = await new Builder().forBrowser('firefox').build()
    vars = {}
  })
  afterEach(async function() {
    await driver.quit();
  })
  it('BPB Online Test Cases', async function() {
    // Test name: BPB Online Test Cases
    // Step # | name | target | value | comment
    // 1 | open | https://bpbonline.com/ |  | 
    await driver.get("https://bpbonline.com/")
    // 2 | setWindowSize | 1050x708 |  | 
    await driver.setRect(1050, 708)
    // 3 | click | id=bc-product-search |  | 
    await driver.findElement(By.id("bc-product-search")).click()
    // 4 | click | id=bc-product-search |  | 
    await driver.findElement(By.id("bc-product-search")).click()
    // 5 | type | id=bc-product-search | selenium | 
    await driver.findElement(By.id("bc-product-search")).sendKeys("selenium")
    // 6 | click | id=search |  | 
    await driver.findElement(By.id("search")).click()
    // 7 | verifyTitle | Computer & IT Books | Emerging & Trending Technologies l E-books – BPB Publications |  | 
    assert(await driver.getTitle() == "Computer & IT Books | Emerging & Trending Technologies l E-books – BPB Publications")
    // 8 | click | css=.tt-cursor .text-search-sn-search-shopify |  | 
    await driver.findElement(By.css(".tt-cursor .text-search-sn-search-shopify")).click()
    // 9 | type | id=bc-product-search | C Under DOS Test by Riku Parikh, Anup Jalan, Soham Desai | 
    await driver.findElement(By.id("bc-product-search")).sendKeys("C Under DOS Test by Riku Parikh, Anup Jalan, Soham Desai")
    // 10 | mouseOver | css=.active:nth-child(4) > .dropdown-link > span |  | 
    {
      const element = await driver.findElement(By.css(".active:nth-child(4) > .dropdown-link > span"))
      await driver.actions({ bridge: true }).moveToElement(element).perform()
    }
    // 11 | assertText | css=span > strong | Description: | 
    assert(await driver.findElement(By.css("span > strong")).getText() == "Description:")
    // 12 | click | css=.hover:nth-child(5) > a |  | 
    await driver.findElement(By.css(".hover:nth-child(5) > a")).click()
    // 13 | click | id=bc-product-search |  | 
    await driver.findElement(By.id("bc-product-search")).click()
    // 14 | click | css=.hover span |  | 
    await driver.findElement(By.css(".hover span")).click()
    // 15 | click | id=bc-product-search |  | 
    await driver.findElement(By.id("bc-product-search")).click()
    // 16 | type | id=bc-product-search | artif | 
    await driver.findElement(By.id("bc-product-search")).sendKeys("artif")
    // 17 | click | id=bc-product-search |  | 
    await driver.findElement(By.id("bc-product-search")).click()
    // 18 | assertText | css=.tt-cursor .content-lineal-sn-search-shopify | Artificial Intelligence | 
    assert(await driver.findElement(By.css(".tt-cursor .content-lineal-sn-search-shopify")).getText() == "Artificial Intelligence")
    // 19 | click | css=.tt-cursor .tt-highlight |  | 
    await driver.findElement(By.css(".tt-cursor .tt-highlight")).click()
    // 20 | type | id=bc-product-search | Artificial Intelligence | 
    await driver.findElement(By.id("bc-product-search")).sendKeys("Artificial Intelligence")
    // 21 | click | css=.grid |  | 
    await driver.findElement(By.css(".grid")).click()
    // 22 | mouseOver | css=.product-grid-item:nth-child(2) .featured-image |  | 
    {
      const element = await driver.findElement(By.css(".product-grid-item:nth-child(2) .featured-image"))
      await driver.actions({ bridge: true }).moveToElement(element).perform()
    }
    // 23 | click | css=.product-grid-item:nth-child(2) .featured-image |  | 
    await driver.findElement(By.css(".product-grid-item:nth-child(2) .featured-image")).click()
    // 24 | storeTitle | AI & ML - Powering the Agents of Automation – BPB Publications | AIBook | 
    vars["AIBook"] = await driver.getTitle()
    // 25 | click | id=add-to-cart |  | 
    await driver.findElement(By.id("add-to-cart")).click()
    // 26 | click | css=.action > .btn-default |  | 
    await driver.findElement(By.css(".action > .btn-default")).click()
    // 27 | mouseDownAt | id=checkout_email_or_phone | 407.15625,24.015625 | 
    {
      const element = await driver.findElement(By.id("checkout_email_or_phone"))
      await driver.actions({ bridge: true }).moveToElement(element).clickAndHold().perform()
    }
    // 28 | mouseMoveAt | id=checkout_email_or_phone | 407.15625,24.015625 | 
    {
      const element = await driver.findElement(By.id("checkout_email_or_phone"))
      await driver.actions({ bridge: true }).moveToElement(element).perform()
    }
    // 29 | mouseUpAt | id=checkout_email_or_phone | 407.15625,24.015625 | 
    {
      const element = await driver.findElement(By.id("checkout_email_or_phone"))
      await driver.actions({ bridge: true }).moveToElement(element).release().perform()
    }
    // 30 | click | id=checkout_email_or_phone |  | 
    await driver.findElement(By.id("checkout_email_or_phone")).click()
    // 31 | type | id=checkout_email_or_phone | abc@def.com | 
    await driver.findElement(By.id("checkout_email_or_phone")).sendKeys("abc@def.com")
    // 32 | type | name=checkout[shipping_address][first_name] | Selenium | 
    await driver.findElement(By.name("checkout[shipping_address][first_name]")).sendKeys("Selenium")
    // 33 | type | name=checkout[shipping_address][last_name] | User | 
    await driver.findElement(By.name("checkout[shipping_address][last_name]")).sendKeys("User")
    // 34 | type | name=checkout[shipping_address][address1] | 12345, Sixth Street | 
    await driver.findElement(By.name("checkout[shipping_address][address1]")).sendKeys("12345, Sixth Street")
    // 35 | type | name=checkout[shipping_address][address2] | Seventh Avenue | 
    await driver.findElement(By.name("checkout[shipping_address][address2]")).sendKeys("Seventh Avenue")
    // 36 | type | name=checkout[shipping_address][city] | Denver | 
    await driver.findElement(By.name("checkout[shipping_address][city]")).sendKeys("Denver")
    // 37 | type | name=checkout[shipping_address][country] | US | 
    await driver.findElement(By.name("checkout[shipping_address][country]")).sendKeys("US")
    // 38 | type | name=checkout[shipping_address][province] | Colorado | 
    await driver.findElement(By.name("checkout[shipping_address][province]")).sendKeys("Colorado")
    // 39 | type | name=checkout[shipping_address][zip] | 80201 | 
    await driver.findElement(By.name("checkout[shipping_address][zip]")).sendKeys("80201")
    // 40 | type | name=checkout[shipping_address][phone] | 9876543241 | 
    await driver.findElement(By.name("checkout[shipping_address][phone]")).sendKeys("9876543241")
    // 41 | click | id=checkout_remember_me |  | 
    await driver.findElement(By.id("checkout_remember_me")).click()
    // 42 | click | css=.icon-svg--size-18 |  | 
    await driver.findElement(By.css(".icon-svg--size-18")).click()
    // 43 | click | css=.btn__content |  | 
    await driver.findElement(By.css(".btn__content")).click()
    // 44 | click | css=.radio-wrapper:nth-child(2) > .radio__label |  | 
    await driver.findElement(By.css(".radio-wrapper:nth-child(2) > .radio__label")).click()
    // 45 | click | css=.shown-if-js > #continue_button > .icon-svg |  | 
    await driver.findElement(By.css(".shown-if-js > #continue_button > .icon-svg")).click()
    // 46 | selectFrame | index=0 |  | 
    await driver.switchTo().frame(0)
    // 47 | assertTitle | Razorpay Checkout |  | 
    assert(await driver.getTitle() == "Razorpay Checkout")
    // 48 | close |  |  | 
    await driver.close()
  })
})

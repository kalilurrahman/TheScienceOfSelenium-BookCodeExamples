// Generated by Selenium IDE
const { Builder, By, Key, until } = require('selenium-webdriver')
const assert = require('assert')

describe('Google News Test', function() {
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
  it('Google News Test', async function() {
    // Test name: Google News Test
    // Step # | name | target | value | comment
    // 1 | open | /?hl=en-IN&gl=IN&ceid=IN:en |  | 
    await driver.get("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en")
    // 2 | setWindowSize | 1050x708 |  | 
    await driver.setRect(1050, 708)
    // 3 | verifyText | linkText=More Headlines | More Headlines | 
    assert(await driver.findElement(By.linkText("More Headlines")).getText() == "More Headlines")
    // 4 | verifyTitle | Google News |  | 
    assert(await driver.getTitle() == "Google News")
    // 5 | assertText | linkText=More Headlines | More Headlines | 
    assert(await driver.findElement(By.linkText("More Headlines")).getText() == "More Headlines")
    // 6 | assertTitle | Google News |  | 
    assert(await driver.getTitle() == "Google News")
    // 7 | storeText | linkText=More Headlines | HL | 
    vars["HL"] = await driver.findElement(By.linkText("More Headlines")).getText()
    // 8 | click | css=.gb_tc:nth-child(1) > svg |  | 
    await driver.findElement(By.css(".gb_tc:nth-child(1) > svg")).click()
    // 9 | click | css=div:nth-child(7) .ICsaqd |  | 
    await driver.findElement(By.css("div:nth-child(7) .ICsaqd")).click()
    // 10 | runScript | window.scrollTo(0,0) |  | 
    await driver.executeScript("window.scrollTo(0,0)")
    // 11 | verifyText | css=.M9Bg4d | star_border\nFollow | 
    assert(await driver.findElement(By.css(".M9Bg4d")).getText() == "star_border\nFollow")
    // 12 | assertText | css=.M9Bg4d | star_border\nFollow | 
    assert(await driver.findElement(By.css(".M9Bg4d")).getText() == "star_border\nFollow")
    // 13 | click | css=.M9Bg4d > .FKF6mc |  | 
    await driver.findElement(By.css(".M9Bg4d > .FKF6mc")).click()
    // 14 | runScript | window.scrollTo(0,0) |  | 
    await driver.executeScript("window.scrollTo(0,0)")
    // 15 | click | css=.KL4X6e |  | 
    await driver.findElement(By.css(".KL4X6e")).click()
    // 16 | runScript | window.scrollTo(0,0) |  | 
    await driver.executeScript("window.scrollTo(0,0)")
    // 17 | click | css=.BiCknd |  | 
    await driver.findElement(By.css(".BiCknd")).click()
    // 18 | click | css=.FwR7Pc .jO7h3c |  | 
    await driver.findElement(By.css(".FwR7Pc .jO7h3c")).click()
    // 19 | close |  |  | 
    await driver.close()
  })
})

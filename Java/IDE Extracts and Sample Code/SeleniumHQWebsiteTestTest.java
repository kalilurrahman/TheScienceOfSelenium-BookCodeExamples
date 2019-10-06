// Generated by Selenium IDE
import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.core.IsNot.not;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Alert;
import org.openqa.selenium.Keys;
import java.util.*;
public class SeleniumHQWebsiteTestTest {
  private WebDriver driver;
  private Map<String, Object> vars;
  JavascriptExecutor js;
  @Before
  public void setUp() {
    driver = new FirefoxDriver();
    js = (JavascriptExecutor) driver;
    vars = new HashMap<String, Object>();
  }
  @After
  public void tearDown() {
    driver.quit();
  }
  @Test
  public void seleniumHQWebsiteTest() {
    // Test name: SeleniumHQ Website Test
    // Step # | name | target | value | comment
    // 1 | open | https://www.seleniumhq.org/ |  | 
    driver.get("https://www.seleniumhq.org/");
    // 2 | setWindowSize | 1050x708 |  | 
    driver.manage().window().setSize(new Dimension(1050, 708));
    // 3 | click | linkText=Projects |  | 
    driver.findElement(By.linkText("Projects")).click();
    // 4 | click | css=p:nth-child(3) > a |  | 
    driver.findElement(By.cssSelector("p:nth-child(3) > a")).click();
    // 5 | click | linkText=ChromeDriver |  | 
    driver.findElement(By.linkText("ChromeDriver")).click();
    // 6 | click | linkText=FindsByTagName |  | 
    driver.findElement(By.linkText("FindsByTagName")).click();
    // 7 | click | linkText=Download |  | 
    driver.findElement(By.linkText("Download")).click();
    // 8 | click | css=table:nth-child(13) tr:nth-child(1) > td:nth-child(4) > a |  | 
    driver.findElement(By.cssSelector("table:nth-child(13) tr:nth-child(1) > td:nth-child(4) > a")).click();
    // 9 | click | linkText=Documentation |  | 
    driver.findElement(By.linkText("Documentation")).click();
    // 10 | runScript | window.scrollTo(0,123) |  | 
    js.executeScript("window.scrollTo(0,123)");
    // 11 | click | linkText=Driver Specifics and Tradeoffs |  | 
    driver.findElement(By.linkText("Driver Specifics and Tradeoffs")).click();
    // 12 | click | css=#usage > .toggler-python |  | 
    driver.findElement(By.cssSelector("#usage > .toggler-python")).click();
    // 13 | click | css=#enabling-javascript > .toggler-csharp |  | 
    driver.findElement(By.cssSelector("#enabling-javascript > .toggler-csharp")).click();
    // 14 | click | css=#enabling-javascript > .toggler-python |  | 
    driver.findElement(By.cssSelector("#enabling-javascript > .toggler-python")).click();
    // 15 | click | css=#modifying-the-firefox-profile > .toggler:nth-child(5) |  | 
    driver.findElement(By.cssSelector("#modifying-the-firefox-profile > .toggler:nth-child(5)")).click();
    // 16 | click | css=.toggler-csharp:nth-child(10) |  | 
    driver.findElement(By.cssSelector(".toggler-csharp:nth-child(10)")).click();
    // 17 | click | css=.toggler-csharp:nth-child(15) |  | 
    driver.findElement(By.cssSelector(".toggler-csharp:nth-child(15)")).click();
    // 18 | click | css=#introducing-the-selenium-webdriver-api-by-example > .toggler-python |  | 
    driver.findElement(By.cssSelector("#introducing-the-selenium-webdriver-api-by-example > .toggler-python")).click();
    // 19 | click | css=#introducing-the-selenium-webdriver-api-by-example > .highlight-python pre |  | 
    driver.findElement(By.cssSelector("#introducing-the-selenium-webdriver-api-by-example > .highlight-python pre")).click();
    // 20 | click | id=container |  | 
    driver.findElement(By.id("container")).click();
    // 21 | click | id=introducing-the-selenium-webdriver-api-by-example |  | 
    driver.findElement(By.id("introducing-the-selenium-webdriver-api-by-example")).click();
    // 22 | click | linkText=Support |  | 
    driver.findElement(By.linkText("Support")).click();
    // 23 | close |  |  | 
    driver.close();
  }
}
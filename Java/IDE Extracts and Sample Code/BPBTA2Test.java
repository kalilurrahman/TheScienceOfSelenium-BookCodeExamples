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
public class BPBTA2Test {
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
  public void bPBTA2() {
    // Test name: BPBTA2
    // Step # | name | target | value | comment
    // 1 | open | https://bpbonline.com/ |  | 
    driver.get("https://bpbonline.com/");
    // 2 | setWindowSize | 1050x708 |  | 
    driver.manage().window().setSize(new Dimension(1050, 708));
    // 3 | click | css=.hover > .expand |  | 
    driver.findElement(By.cssSelector(".hover > .expand")).click();
    // 4 | click | css=.hover > .expand |  | 
    driver.findElement(By.cssSelector(".hover > .expand")).click();
    // 5 | assertText | linkText=Data Structure & Algorithms | Data Structure & Algorithms | 
    assertThat(driver.findElement(By.linkText("Data Structure & Algorithms")).getText(), is("Data Structure & Algorithms"));
    // 6 | mouseOver | linkText=Computer Books |  | 
    {
      WebElement element = driver.findElement(By.linkText("Computer Books"));
      Action builder = new Actions(driver);
      builder.moveToElement(element).perform();
    }
    // 7 | mouseOut | linkText=Computer Books |  | 
    {
      WebElement element = driver.findElement(By.tagName("body"));
      Action builder = new Actions(driver);
      builder.moveToElement(element, 0, 0).perform();
    }
    // 8 | click | css=.hover span |  | 
    driver.findElement(By.cssSelector(".hover span")).click();
    // 9 | assertText | css=.col-md-3:nth-child(2) h4 | Cloud Computing -Master Cloud Computing Concepts Architecture and Applications with Real-world examples and case studies | 
    assertThat(driver.findElement(By.cssSelector(".col-md-3:nth-child(2) h4")).getText(), is("Cloud Computing -Master Cloud Computing Concepts Architecture and Applications with Real-world examples and case studies"));
    // 10 | verifyText | css=.col-md-3:nth-child(1) h4 | SharePoint Online Modern Experience Practical Guide: Learn step by step how to use SharePoint Online Modern Experience  | 
    assertThat(driver.findElement(By.cssSelector(".col-md-3:nth-child(1) h4")).getText(), is("SharePoint Online Modern Experience Practical Guide: Learn step by step how to use SharePoint Online Modern Experience "));
    // 11 | mouseOver | css=#mCSB_1_container > li:nth-child(3) |  | 
    {
      WebElement element = driver.findElement(By.cssSelector("#mCSB_1_container > li:nth-child(3)"));
      Action builder = new Actions(driver);
      builder.moveToElement(element).perform();
    }
    // 12 | storeText | css=#mCSB_1_container > li:nth-child(3) | ListofBooks | 
    vars.put("ListofBooks", driver.findElement(By.cssSelector("#mCSB_1_container > li:nth-child(3)")).getText());
    // 13 | click | css=#mCSB_1_container > li:nth-child(1) |  | 
    driver.findElement(By.cssSelector("#mCSB_1_container > li:nth-child(1)")).click();
    // 14 | click | linkText=Skills |  | 
    driver.findElement(By.linkText("Skills")).click();
    // 15 | click | linkText=Management Team |  | 
    driver.findElement(By.linkText("Management Team")).click();
    // 16 | click | linkText=Home |  | 
    driver.findElement(By.linkText("Home")).click();
    // 17 | click | linkText=Home |  | 
    driver.findElement(By.linkText("Home")).click();
  }
}

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
public class GoogleNewsTestTest {
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
  public void googleNewsTest() {
    // Test name: Google News Test
    // Step # | name | target | value | comment
    // 1 | open | /?hl=en-IN&gl=IN&ceid=IN:en |  | 
    driver.get("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en");
    // 2 | setWindowSize | 1050x708 |  | 
    driver.manage().window().setSize(new Dimension(1050, 708));
    // 3 | verifyText | linkText=More Headlines | More Headlines | 
    assertThat(driver.findElement(By.linkText("More Headlines")).getText(), is("More Headlines"));
    // 4 | verifyTitle | Google News |  | 
    assertThat(driver.getTitle(), is("Google News"));
    // 5 | assertText | linkText=More Headlines | More Headlines | 
    assertThat(driver.findElement(By.linkText("More Headlines")).getText(), is("More Headlines"));
    // 6 | assertTitle | Google News |  | 
    assertThat(driver.getTitle(), is("Google News"));
    // 7 | storeText | linkText=More Headlines | HL | 
    vars.put("HL", driver.findElement(By.linkText("More Headlines")).getText());
    // 8 | click | css=.gb_tc:nth-child(1) > svg |  | 
    driver.findElement(By.cssSelector(".gb_tc:nth-child(1) > svg")).click();
    // 9 | click | css=div:nth-child(7) .ICsaqd |  | 
    driver.findElement(By.cssSelector("div:nth-child(7) .ICsaqd")).click();
    // 10 | runScript | window.scrollTo(0,0) |  | 
    js.executeScript("window.scrollTo(0,0)");
    // 11 | verifyText | css=.M9Bg4d | star_border\nFollow | 
    assertThat(driver.findElement(By.cssSelector(".M9Bg4d")).getText(), is("star_border\nFollow"));
    // 12 | assertText | css=.M9Bg4d | star_border\nFollow | 
    assertThat(driver.findElement(By.cssSelector(".M9Bg4d")).getText(), is("star_border\nFollow"));
    // 13 | click | css=.M9Bg4d > .FKF6mc |  | 
    driver.findElement(By.cssSelector(".M9Bg4d > .FKF6mc")).click();
    // 14 | runScript | window.scrollTo(0,0) |  | 
    js.executeScript("window.scrollTo(0,0)");
    // 15 | click | css=.KL4X6e |  | 
    driver.findElement(By.cssSelector(".KL4X6e")).click();
    // 16 | runScript | window.scrollTo(0,0) |  | 
    js.executeScript("window.scrollTo(0,0)");
    // 17 | click | css=.BiCknd |  | 
    driver.findElement(By.cssSelector(".BiCknd")).click();
    // 18 | click | css=.FwR7Pc .jO7h3c |  | 
    driver.findElement(By.cssSelector(".FwR7Pc .jO7h3c")).click();
    // 19 | close |  |  | 
    driver.close();
  }
}

// Licensed to the Software Freedom Conservancy (SFC) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The SFC licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

/**
 * @fileoverview This is an example of emulating a mobile device using the
 * ChromeDriver.
 */

'use strict';
const {Builder, By, Key, until} = require('..');
const {Options} = require('../chrome');
(async function() {
  let driver;
  var browsers = ["iPhone 5", "iPad Mini", "Nexus 5X", "Galaxy S5"];
  var i=0;
  var fs = require('fs')
  try {
    for (i = 0; i < browsers.length; i++) {
    var filename = "Chrome_Browser_Emulation_";
    filename = filename.concat(browsers[i],".png");
    console.log(filename);
    driver = await new Builder().forBrowser('chrome').setChromeOptions(new Options().setMobileEmulation({deviceName: browsers[i]})).build();
         await driver.get('http://www.google.com/ncr');
      	 await driver.findElement(By.name('q')).sendKeys('webdriver', Key.RETURN);
    	 await driver.wait(until.titleIs('webdriver - Google Search'), 1000);
         await driver.takeScreenshot().then(
           function (ScreenShotImage, err) {
            fs.writeFile(filename, ScreenShotImage, 'base64', function (error) {
                  if (error != null)
                      console.log("Error occured during screenshot" + error);
                  });
           }
         );
	 await driver.close();
    }
    } finally {
      await driver && driver.quit();
    }
})().then(_ => console.log('SUCCESS'), err => console.error('ERROR: ' + err));
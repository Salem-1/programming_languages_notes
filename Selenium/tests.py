import os
import pathlib
import unittest

from selenium import webdriver

#find the URI = uniform resource identifier  of a file ,"A string which identify that page"
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

#setup web browser using chrome
driver = webdriver.Chrome("C:\\Users\\Ahmed Salem\\tech\\fc\\venv\\Lib\\site-packages\\chromedriver_py\\chromedriver_win32.exe")


class webPagetest(unittest.TestCase):
    """defining all the tests I am going to run on my webpage"""

    def test_title(self):
        """testing the title"""
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title,"Counter")

    def test_increase(self):
        """testing the increase button"""
        driver.get(file_uri("counter.html")) # opening the file and returning it as string
        increase = driver.find_element_by_id("increase") # selecting the increase button throught it's ID
        increase.click() #Clicking the increase button
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1") # reading the h1 tag and returning it's value to compare it to the desired output "1"

    def test_decrease(self):
        """testing the decrease button"""
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element_by_id("decrease") #don't add self. to the driver sir
        decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1") # the -1 is string not integer sir

        def test_multiple_increase(self):
            driver.get(file_uri("counter.html")) # opening the file and returning it as string
            increase = driver.find_element_by_id("increase") # selecting the increase button throught it's ID
            for i in range(3):
                increase.click() #Clicking the increase button
            self.assertEqual(driver.find_element_by_tag_name("h1").text, 3) # reading the h1 tag and returning it's value to compare it to the desired output "1"

if __name__ == "__main__":
    unittest.main()
"""selenium commands in powershell
# Find the URI of our newly created file
>>> uri = file_uri("counter.html")

# Use the URI to open the web page
>>> driver.get(uri)

# Access the title of the current page
>>> driver.title
'Counter'

# Access the source code of the page
>>> driver.page_source
'<html lang="en"><head>\\n        <title>Counter</title>\\n        <script>\\n            \\n            // Wait for page to load\\n            document.addEventListener(\\'DOMContentLoaded\\', () => {\\n\\n                // Initialize variable to 0\\n                let counter = 0;\\n\\n                // If increase button clicked, increase counter and change inner html\\n                document.querySelector(\\'#increase\\').onclick = () => {\\n                    counter ++;\\n                    document.querySelector(\\'h1\\').innerHTML = counter;\\n                }\\n\\n                // If decrease button clicked, decrease counter and change inner html\\n                document.querySelector(\\'#decrease\\').onclick = () => {\\n                    counter --;\\n                    document.querySelector(\\'h1\\').innerHTML = counter;\\n                }\\n            })\\n        </script>\\n    </head>\\n    <body>\\n        <h1>0</h1>\\n        <button id="increase">+</button>\\n        <button id="decrease">-</button>\\n    \\n</body></html>'

# Find and store the increase and decrease buttons:
>>> increase = driver.find_element_by_id("increase")
>>> decrease = driver.find_element_by_id("decrease")

# Simulate the user clicking on the two buttons
>>> increase.click()
>>> increase.click()
>>> decrease.click()

# We can even include clicks within other Python constructs:
>>> for i in range(25):
...     increase.click()

#unittest methods
assertEqual
assertNOtEqual
asserTrue
assertFalse
assertIn
assertNotIn


"""

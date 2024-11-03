from selenium.webdriver.chrome.webdriver import WebDriver as chrome
from selenium.webdriver.edge.webdriver import WebDriver as edge

from pytest import fixture
import  pytest

class TestConfiguration:
    url="https://admin-demo.nopcommerce.com/login"

@fixture()
def _config(request):
    if request.config.option.env.upper() == 'TEST':
        return TestConfiguration
    else:
        return Exception('unknown environment ')


def pytest_addoption(parser):
    parser.addoption("--browser",action='store',dest='browser')
    parser.addoption("--env", action='store', dest='env')

@fixture()
def setup(request,_config):
    if request.config.option.browser.upper() == 'CHROME':
      print("chrome")
      driver= chrome()
      driver.get(_config.url)
    elif request.config.option.browser.upper() == "EDGE":
      print("edge")
      driver= edge()
      _config.url
    yield driver
    # driver.close()



# @fixture()
# def browser(request):
#     return  request.config.getoption("--browser")

# @pytest.mark.
# def pytest_configure(config):
#     config.



# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     # Adding custom metadata
#     metadata['Project Name'] = 'nop commerce'
#     metadata['Module Name'] = 'customer'
#     metadata['Tester'] = 'vishnu'
#
#     # Removing unwanted metadata
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
# #


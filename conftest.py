import pytest

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import Firefox, FirefoxProfile, FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store',
        default='firefox',
        help='firefox, edge, chrome',
        choices=('firefox', 'edge', 'chrome')
    )
    parser.addoption(
        '--language', action='store',
        default='en',
        help="Choose language. Example: 'ru', 'en' or other",
        choices=(
            'ar', 'ca', 'cs', 'da', 'de', 'en', 'el', 'es', 'fi', 'fr',
            'it', 'ko', 'nl', 'pl', 'pt', 'ro', 'ru', 'sk', 'uk', 'zh'
            )
    )


def get_driver(driver_name: str, **kwargs):

    if driver_name == 'firefox':
        fp = FirefoxProfile()
        fp.set_preference('intl.accept_languages', kwargs.get('language'))
        fp.set_preference('page_load_strategy', 'eager')
        driver = Firefox(
            firefox_profile=fp, service=FirefoxService(executable_path=GeckoDriverManager().install())
        )

    elif driver_name == 'edge':
        eo = EdgeOptions()
        eo.add_experimental_option('prefs', {'intl.accept_languages': kwargs.get('language')})
        driver = Edge(
            options=eo, service=EdgeService(executable_path=EdgeChromiumDriverManager().install())
        )

    elif driver_name == 'chrome':
        co = ChromeOptions()
        co.add_experimental_option('prefs', {'intl.accept_languages': kwargs.get('language')})
        driver = Chrome(
            options=co, service=ChromeService(executable_path=ChromeDriverManager().install())
        )
    driver.maximize_window()
    return driver


@pytest.fixture(scope='function', name='driver')
def browser(request):
    driver_name = request.config.getoption('--browser')
    language = request.config.getoption('--language')
    driver = get_driver(driver_name, language=language)
    print(f'\n..start {driver_name}..')
    yield driver
    print(f'\n..quit {driver_name}..')
    driver.close()
    driver.quit()
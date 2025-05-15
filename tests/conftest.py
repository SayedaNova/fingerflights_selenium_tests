import pytest
from tests.helpers.driver_utils import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
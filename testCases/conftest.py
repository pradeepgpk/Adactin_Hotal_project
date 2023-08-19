import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
@pytest.fixture()
def setup():
    service = Service(executable_path=EdgeChromiumDriverManager().install())
    return webdriver.Edge(service=service)


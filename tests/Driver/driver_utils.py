from selenium import webdriver
from selenium.webdriver.edge.service import Service

def get_driver():
    return webdriver.Edge(service=Service(executable_path="C:\\Users\\USER\\PycharmProjects\\AuthTest\\Browsers\\msedgedriver.exe"))


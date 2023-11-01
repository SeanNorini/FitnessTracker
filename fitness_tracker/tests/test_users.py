from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import pytest
import time



class UserTests(StaticLiveServerTestCase):  
    fixtures = ["testusers.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    
    def admin_login(self):
        """
        Returns a ChromeDriver logged in as Admin on index.html.
        """
        self.selenium.get(f"{self.live_server_url}/users/login")
        self.selenium.find_element(By.NAME, "username").send_keys("Admin")
        self.selenium.find_element(By.NAME, "password").send_keys("Admin")
        self.selenium.find_element(By.NAME, "login").click()
        

    def test_login(self):
        """
        Test verifies admin_login was successful by checking user greeting
        on index.html after log in attempt.
        Expected result: Admin is logged in.
        """
        self.admin_login()
        time.sleep(15)
        greeting = self.selenium.find_element(By.ID, "greeting")
        assert greeting.text == "Welcome, Admin."

    def test_logout(self):
        """
        Test verifies log out was successful by checking user greeting
        on index.html after log out attempt.
        Expected result: User is logged out.
        """
        self.admin_login()
        self.selenium.find_element(By.ID, "logout").click()
        greeting = self.selenium.find_element(By.ID, "greeting")
        assert greeting.text == "Not signed in."

    def test_redirect(self):
        """
        Test verifies that logged out users are redirected to the log in page.
        Expected result: Logged out user returned to log in page.
        """
        self.selenium.get(f"{self.live_server_url}")
        url = self.selenium.current_url
        assert url == f"{self.live_server_url}/users/login"
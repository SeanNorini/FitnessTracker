from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from users.models import User, UserAttributes
from django.core.exceptions import ObjectDoesNotExist
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

    def create_user(self):
        self.selenium.get(f"{self.live_server_url}/users/registration")
        self.selenium.find_element(By.NAME, "username").send_keys("test_name")
        self.selenium.find_element(By.NAME, "first_name").send_keys("first_name")
        self.selenium.find_element(By.NAME, "last_name").send_keys("last_name")
        self.selenium.find_element(By.NAME, "password").send_keys("test_pass")
        self.selenium.find_element(By.NAME, "confirm_password").send_keys("test_pass")
        self.selenium.find_element(By.NAME, "email").send_keys("snorini@gmail.com")
        self.selenium.find_element(By.NAME, "weight").send_keys("150")
        self.selenium.find_element(By.NAME, "height").send_keys("75")
        self.selenium.find_element(By.NAME, "age").send_keys("28")
        self.selenium.find_element(By.NAME, "register").click()
        

    def test_login(self):
        """
        Test verifies admin_login was successful by checking user greeting
        on index.html after log in attempt.
        Expected result: Admin is logged in.
        """
        self.admin_login()
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
        url = self.selenium.current_url
        assert url == f"{self.live_server_url}/users/login"

    def test_redirect(self):
        """
        Test verifies that logged out users are redirected to the log in page.
        Expected result: Logged out user returned to log in page.
        """
        self.selenium.get(f"{self.live_server_url}")
        url = self.selenium.current_url
        assert url == f"{self.live_server_url}/users/login"

    def test_registration(self):
        """
        Test verifies registration functionality by making sure a user is not in the database, then
        using the registration form to create a user and confirm user is in database.
        
        """
        # Confirm user does not exist
        with pytest.raises(ObjectDoesNotExist):
            User.objects.get(username="test_name")

        # Create user
        self.create_user()

        # Confirm user created
        assert User.objects.get(username="test_name")
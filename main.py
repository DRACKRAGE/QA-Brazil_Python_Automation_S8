import time
import data
import helpers

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from pages import UrbanRoutesPages


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)
        # Verificação da conexão com o servidor, retornando em verdadeiro ou falso se foi possivel conectar
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor UrbanRoutes")
        else:
            print("Não foi posssível conectar ao Urban Routes")

    def test_set_route (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes = UrbanRoutesPages(self.driver)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        assert urban_routes.get_from_location() == data.ADDRESS_FROM
        assert urban_routes.get_to_location() == data.ADDRESS_TO

    def test_select_plan (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes = UrbanRoutesPages(self.driver)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.click_taxi_comfort_option()
        assert urban_routes.check_comfort_active()

    def teste_fill_phone_number (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes = UrbanRoutesPages(self.driver)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.click_taxi_comfort_option()
        urban_routes.click_number_text(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in urban_routes.confirm_number()


    def test_fill_card (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes = UrbanRoutesPages(self.driver)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.click_taxi_comfort_option()
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.click_add_card(data.CARD_NUMBER, data.CARD_CODE)
        assert "Cartão" in urban_routes.confirm_cards()

    def test_comment_for_driver (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes = UrbanRoutesPages(self.driver)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.click_taxi_comfort_option()
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.add_comment_driver(data.MESSAGE_FOR_DRIVER)
        assert data.MESSAGE_FOR_DRIVER in urban_routes.comment_confirm()

    def test_order_blanket_and_handkerchiefs (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes = UrbanRoutesPages(self.driver)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.click_taxi_comfort_option()
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.switch_button_blanket()
        assert urban_routes.switch_blanket_verify() is True

    def test_order_2_ice_creams (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes = UrbanRoutesPages(self.driver)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.click_taxi_comfort_option()
        WebDriverWait(self.driver, 5).until(lambda d: True)
        for _ in range(2):
            urban_routes.add_icecream_button()
        WebDriverWait(self.driver, 5).until(lambda d: True)
        assert int(urban_routes.qnt_icecream_insert()) == 2

    def test_car_search_model_appears (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes = UrbanRoutesPages(self.driver)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.click_taxi_comfort_option()
        WebDriverWait(self.driver, 5).until(lambda d: True)
        urban_routes.click_number_text(data.PHONE_NUMBER)
        urban_routes.click_add_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_routes.add_comment_driver(data.MESSAGE_FOR_DRIVER)
        urban_routes.call_submit()
        assert "Buscar carro" in  urban_routes.pop_up_show()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
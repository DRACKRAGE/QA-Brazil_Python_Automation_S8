import time
import data
import helpers

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(UrbanRoutesPages.from_locator_field))
        urban_routes.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert urban_routes.get_from_location() == data.ADDRESS_FROM
        assert urban_routes.get_to_location() == data.ADDRESS_TO

    def _prepare_default_flow(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes = UrbanRoutesPages(self.driver)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(UrbanRoutesPages.from_locator_field))
        urban_routes.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(UrbanRoutesPages.call_taxi_locator))
        urban_routes.click_taxi_comfort_option()
        return urban_routes

    def test_select_plan (self):
        urban_routes = self._prepare_default_flow()
        assert urban_routes.check_comfort_active()

    def test_fill_phone_number (self):
        urban_routes = self._prepare_default_flow()
        urban_routes.click_number_text(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in urban_routes.confirm_number()


    def test_fill_card (self):
        urban_routes = self._prepare_default_flow()
        urban_routes.click_add_card(data.CARD_NUMBER, data.CARD_CODE)
        assert "Cartão" in urban_routes.confirm_cards()

    def test_comment_for_driver (self):
        urban_routes = self._prepare_default_flow()
        urban_routes.add_comment_driver(data.MESSAGE_FOR_DRIVER)
        assert data.MESSAGE_FOR_DRIVER in urban_routes.comment_confirm()

    def test_order_blanket_and_handkerchiefs (self):
        urban_routes = self._prepare_default_flow()
        urban_routes.switch_button_blanket()
        assert urban_routes.switch_blanket_verify() is True

    def test_order_2_ice_creams (self):
        urban_routes = self._prepare_default_flow()
        for _ in range(2):
            urban_routes.add_icecream_button()
        WebDriverWait(self.driver, 5).until(lambda d: True)
        assert int(urban_routes.qnt_icecream_insert()) == 2

    def test_car_search_model_appears (self):
        urban_routes = self._prepare_default_flow()
        urban_routes.click_number_text(data.PHONE_NUMBER)
        urban_routes.click_add_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_routes.add_comment_driver(data.MESSAGE_FOR_DRIVER)
        urban_routes.call_submit()
        assert "Buscar carro" in  urban_routes.pop_up_show()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
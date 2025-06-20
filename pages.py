import time

# from html.parser import commentclose
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import retrieve_phone_code

class UrbanRoutesPages:
    # campos de e para
    from_locator_field = (By.ID, 'from')
    to_locator_field = (By.ID, 'to')

    # Taxi selecionado por padrão, acionar botão de chamar, entrar a opção comfort e ativar
    call_taxi_locator= (By.XPATH, '//button[contains(text(), "Chamar")]')
    comfort_icon_locator = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')
    comfort_active_selection = (By.XPATH, '//div[contains(@class, "tcard") and contains(@class, "active") and .//div[text()="Comfort"]]')

    # adicionar numero de telefone e confirmação de código
    number_text_locator = (By.CSS_SELECTOR, '.np-button')
    number_enter_field = (By.ID, 'phone')
    number_confirm_button = (By.CSS_SELECTOR, '.button.full')
    number_code_fill = (By.ID, 'code')
    code_confirm_action = (By.XPATH, '//button[contains(text(), "Confirmar")]')
    number_finish = (By.CSS_SELECTOR, '.np-text')

    # Escolher métodos de pagamento
    payment_method = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    card_number = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, 'input.card-input#code')
    finish_card_button = (By.XPATH, '//button[contains(text(), "Adicionar")]')
    close_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
    confirm_card = (By.CSS_SELECTOR, '.pp-value-text')

    # inserir comentario para o motorista
    add_comment = (By.ID, 'comment')

    # escolher cobertor/lencois
    switch_blanket = (By.CSS_SELECTOR, '.switch .slider') # clicavel
    switch_blanket_active = (By.CSS_SELECTOR, '.switch-input') # verificação

    # adicionando quantidade de sorvetes
    add_icecream = (By.CSS_SELECTOR, '.counter-plus')
    qnt_icecream = (By.CSS_SELECTOR, '.counter-value')

    # finalizar a chamada do transporte
    call_vehicle = (By.CSS_SELECTOR, '.smart-button')
    pop_up = (By.CSS_SELECTOR, '.order-header-title')

    def __init__(self, driver):
        self.driver = driver

    # Rota
    def enter_from_location(self, from_text):
        # localizar o campo DE e preencher
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.from_locator_field))
        self.driver.find_element(*self.from_locator_field).send_keys(from_text)

    # Rota
    def get_from_location(self):
        # retorna se o campo DE for identificado conforme o elemento encontrado
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.from_locator_field)).get_attribute('value')

    # Rota
    def enter_to_location(self, to_text):
        # localizar o campo PARA e preencher
        WebDriverWait(self.driver, 5).until(
            # localizar o campo PARA e preencher
            EC.presence_of_element_located(self.to_locator_field))
        self.driver.find_element(*self.to_locator_field).send_keys(to_text)

    # Rota
    def get_to_location(self):
        # retorna se o campo PARA for identificado conforme o elemento encontrado
       return WebDriverWait(self.driver, 5).until(
           EC.visibility_of_element_located(self.to_locator_field)).get_attribute('value')

    # opcoes de escolha de modos e tipos de transporte
    def click_taxi_comfort_option(self):
        # Identifica o botão para chamar o taxi e clica
       WebDriverWait(self.driver, 5).until(
           EC.visibility_of_element_located(self.call_taxi_locator))
       self.driver.find_element(*self.call_taxi_locator).click()
       WebDriverWait(self.driver, 5).until(
           EC.visibility_of_element_located(self.comfort_icon_locator))
       self.driver.find_element(*self.comfort_icon_locator).click()

    # verificacao de tarifa
    def check_comfort_active(self):
        # verifica se o botão da tarifa selecionada está ativa
        try:
            active_button = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.comfort_active_selection))
            return "active" in active_button.get_attribute("class")
        except:
            return False

    # retorna confirmacao do campo com o numero de telefone inserido
    def confirm_number(self):
        # verifica se o elemento localizado está com o telefone preenchido
        verify_number= WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.number_finish))
        return verify_number.text

    # retorna confirmacao do cartao inserido
    def confirm_cards(self):
        return self.driver.find_element(*self.confirm_card).text

    # insere comentarios para o motorista no campo especifico
    def add_comment_driver(self, comments):
        self.driver.find_element(*self.add_comment).send_keys(comments)

    # verifica se está inserido o texto no campo
    def comment_confirm(self):
        return self.driver.find_element(*self.add_comment).get_attribute('value')

    # aciona o botao de cobertor como preferencia
    def switch_button_blanket(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.switch_blanket))
        self.driver.find_element(*self.switch_blanket).click()
    # verifica o estado do botao ativado
    def switch_blanket_verify(self):
        switch_verify = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.switch_blanket_active))
        return switch_verify.is_selected()

    # clica para inserir x quantidade de sorvetes
    def add_icecream_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.add_icecream))
        self.driver.find_element(*self.add_icecream).click()

    # verifica se no campo está descrito a quantidade desejada
    def qnt_icecream_insert(self):
        return self.driver.find_element(*self.qnt_icecream).text

    # clica no botào para reservar o transporte escolhido
    def call_submit(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.call_vehicle))
        self.driver.find_element(*self.call_vehicle).click()

    # verifica se o pop-up de confirmação surge na tela
    def pop_up_show(self):
        pop_up = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.pop_up))
        return pop_up.text

    # funções de chamada agregadas
    def enter_location(self, from_text, to_text):
        # juncao de funcoes para selecionar a rota
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def click_number_text(self, phone_number):
        # Encontra os campos para inserir os dados fr telefone, busca o código SMS gerado, confirma e valida
        self.driver.find_element(*self.number_text_locator).click()
        self.driver.find_element(*self.number_enter_field).send_keys(phone_number)
        self.driver.find_element(*self.number_confirm_button).click()

        code = retrieve_phone_code(self.driver) # digita o cdoigo recebido
        code_input = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.number_code_fill))
        code_input.clear()
        code_input.send_keys(code)

        self.driver.find_element(*self.code_confirm_action).click()

    # Identifica o campo de metodo de pagamento, icone de cartão, numero do cartao, codigo, finaliza
    def click_add_card(self, card, cvc_code):
        self.driver.find_element(*self.payment_method).click()
        self.driver.find_element(*self.add_card).click()
        self.driver.find_element(*self.card_number).send_keys(card)
        self.driver.find_element(*self.code_card).send_keys(cvc_code)
        self.driver.find_element(*self.finish_card_button).click()
        self.driver.find_element(*self.close_button_card).click()




import data
import helpers
from data import URBAN_ROUTES_URL
from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Verificação da conexão com o servidor, retornando em verdadeiro ou falso se foi possivel conectar
        if is_url_reachable(URBAN_ROUTES_URL):
            print("Conectado ao servidor UrbanRoutes")
        else:
            print("Não foi posssível conectar ao Urban Routes")

    def test_set_route (self):
    #Adicionar em S8
        print("função criada para definir a rota")
    pass
    def test_select_plan (self):
    #Adicionar em S8
        print("função criada para selecionar os planos")
    pass
    def teste_fill_phone_number (self):
    #Adicionar em S8
        print("função criada para inserir numero de telefone")
    pass
    def test_fill_card (self):
    #Adicionar em S8
        print("função criada para inserir cartao de credito/debito")
    pass
    def test_comment_for_driver (self):
    #Adicionar em S8
        print("função criada para inserir comentarios do motorista")
    pass
    def test_order_blanket_and_handkerchiefs (self):
    #Adicionar em S8
        print("função criada para selecionar o pedido, espaço em branco e outros")
    pass
    def test_order_2_ice_creams (self):
    #Adicionar em S8
        for i in range (2):
            #Adicionar em S8
            pass
        print("função criada para pedido adicionais")
    pass
    def test_car_search_model_appears (self):
    #Adicionar em S8
        print("função criada para definir modelo dos veiculos no mapa")
    pass


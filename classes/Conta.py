from datetime import datetime


class Conta:

    def __init__(self, titular, valor_a_pagar, data_ultimo_pagamento, data_ultima_compra):
        self.__titular = titular
        self.__valor_a_pagar = valor_a_pagar
        self.__data_ultimo_pagamento = datetime.strptime(data_ultimo_pagamento, '%d/%m/%Y').date()
        self.__data_ultima_compra = datetime.strptime(data_ultima_compra, '%d/%m/%Y').date()

    # GETS
    def get_titular(self):
        return self.__titular

    def get_valor_a_pagar(self):
        return self.__valor_a_pagar

    def get_data_ultimo_pagamento(self):
        return self.__data_ultimo_pagamento

    def get_data_ultima_compra(self):
        return self.__data_ultima_compra

    # SETS
    def set_titular(self, nova_titular):
        self.__titular = nova_titular

    def set_valor_a_pagar(self, nova_valor_a_pagar):
        self.__valor_a_pagar = nova_valor_a_pagar

    def set_data_ultimo_pagamento(self, nova_data_ultimo_pagamento):
        self.__data_ultimo_pagamento = nova_data_ultimo_pagamento

    def set_data_ultima_compra(self, nova_data_ultima_compra):
        self.__data_ultima_compra = nova_data_ultima_compra

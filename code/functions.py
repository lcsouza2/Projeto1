import json
import string
import random

class GenerateCode:
        
    def generate_code(existing_codes):
        """
        Gera um código aleatório com letras minúsculas, maiúsculas e números
        
        Args:
            existing_codes: lista dos códigos existentes

        Retorna: 
            código diferente dos já existentes
        """
    
        #Gera o código aleatório
        while (True):
            code = "".join(random.choice(string.ascii_letters + string.digits)for _ in range(6))
            if code not in existing_codes:
                return code

    def generate_pwd(char_amount):
        #Gera a senha 
        pwd = "".join(random.choice(string.ascii_letters + string.ascii_punctuation, string.digits)for _ in range(char_amount))
        return pwd
        
class JsonManagment:
    def __init__(self, file):
        self.file = file

    def read_json(self):
        """
        Lê um arquivo json e retorna seu conteúdo
    
        Args:
            Arquivo json a ser lido 
        """
        try:
            with open(self.file, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        except FileNotFoundError:
            with open(self.file, "w"):
                return []
    
    def add_data(self, data):
        """
        Escreve dados no json

        Args:
            data: Dados a serem adicionados ao json
        Retorna:
            True se os dados forem adicionados
        """

        current_data = self.read_json()
        current_data.append(data)
        
        with open(self.file, "w") as f:
            json.dump(current_data, f, indent = 4, ensure_ascii=False)

    def remove_data(self, ctrl_code):
        """
        Remove dados do json
        
        Args:
            ctrl_code: código de controle do item a ser removido
        """
        current_data = self.read_json()

        #Adiciona os itens a lista
        new_data = [item for item in current_data if item.get("ctrl_code") != ctrl_code]

        with open(self.file, "w") as f:
            json.dump(new_data, f, indent=4, ensure_ascii=False)

    def alt_data(self, new_data):
        """
        Altera dados no json

        Args:
            new_data: dados alterados a serem adicionados

        Retorna:
            True se alterado
            False se não
        """
        current_data = self.read_json()
        
        for i, item in enumerate(current_data):
            #Pega o dicionário que contém o código de controle
            if item.get("ctrl_code") == new_data.get("ctrl_code"):
                current_data[i] = new_data

                #Reescreve os dados 
                with open(self.file, "w") as f:
                    json.dump(current_data, f, indent=4, ensure_ascii=False)
                return True
                
            #LEvanta um erro caso o código não seja encontrado
            raise ValueError("Código de controle não encontrado!")
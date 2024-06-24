import json
import string
import random

def generate_code(json_file):
    """
    Gera um código aleatório com letras minúsculas, maiúsculas e números
    Args:
        json_file: arquivo json para ler os códigos já existentes no arquivo
    """

    #Gera o código aleatório
    code = ""
    for j in range(6):
        code += str(
            random.choice(
                [random.choice(string.ascii_letters),
                 random.randint(0, 10)]))

    #Caso o codigo esteja no arquivo gera outro
    existing_codes = []
    for i in read_json(json_file):
        existing_codes.append(i["ctrl_code"])

    while code in existing_codes:
        for j in range(6):
            code += str(
                random.choice([
                    random.choice(string.ascii_letters),
                    random.randint(0, 10)
                ]))
    return code

def generate_pwd(char_amount):
    pwd = ""
    for i in range(char_amount):
        pwd += str(
            random.choice([
                random.choice(string.ascii_letters),
                random.choice(string.punctuation),
                random.randint(0, 10)
            ]))
    return pwd

def read_json(file: str):
    """
    Lê um arquivo json e retorna seu conteúdo

    Args:
        Arquivo json a ser lido 
    """
    try:
        with open(file, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        with open(file, "w"):
            return []

def write_json(
    file: str,
    method: str,
    data: dict,
):
    """
    Manipula um arquivo json dependendo do método

    Args:
        file: arquivo a ser manipulado
        method: "add" (adicionar), "rmv" (remover), "alt" (alterar)
        data: dados em formato dicionário para adicionar ou remover ou alterar
    """

    try:
        open(file, "r")
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado")

    match method:
        case "add":
            add_data = read_json(file)
            add_data.append(data)
            with open(file, "w") as f:
                json.dump(add_data, f, ensure_ascii=False, indent=4)
            return True

        case "rmv":
            found = False
            rmv_data = read_json(file)
            for i in read_json(file):
                if i["ctrl_code"] == data["ctrl_code"]:
                    found = True
                    rmv_data.remove(i)
                    break
            with open(file, "w") as f:
                json.dump(rmv_data, f, ensure_ascii=False, indent=4)

            return found

        case "alt":
            found = False
            alt_data = read_json(file)

            for i in read_json(file):
                if i["ctrl_code"] == data["ctrl_code"]:
                    found = True
                    alt_data.remove(i)
                    alt_data.append(data)

            with open(file, "w") as f:
                json.dump(alt_data, f, ensure_ascii=False, indent=4)
            return found

        case _:
            raise ValueError("Método inválido")
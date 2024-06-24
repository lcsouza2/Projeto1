import tkinter as tk
import tkinter.ttk as ttkfrom 
from tkinter import messagebox, font
import json
import hashlib

def read_json(file:str):
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
        file:str, 
        method:str,
        data:dict,
        data_alt:dict=None
    ):
    """
    Manipula um arquivo json dependendo do método

    Args:
        file: arquivo a ser manipulado
        method: "add" (adicionar), "rmv" (remover), "alt" (alterar)
        data: dados em formato dicionário para adicionar ou remover, dados antigos caso alterar
        data_alt: dicionário com os dados novos caso method seja alt    
    """

    match method:
        case "add":
            old_data = read_json(file)
            old_data.append(data)
            with open(file, "w") as f:
                json.dump(old_data, f, indent=4)

        case "rmv":
            rmv_data = read_json(file)
            for i in read_json(file):
                if i["Nome"] == data["Nome"]:
                    rmv_data.remove(i)
                    break
            with open(file, "w") as f:
                json.dump(rmv_data, f, indent=4)

        case "alt":
            pass

data = {
    "Nome" : "Luiz"
}

write_json("data/users.json", "rmv", data)


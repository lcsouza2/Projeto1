import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, font

class ManageWidgets:            

    def generate_entry(
        master_widget,
        relwidth:float, 
        relheigth:float, 
        width:str|None,
        heigth:str|None,
        relx:float|None,
        rely:float|None,
        x:int|None,
        y:int|None,
        foreground:str="#FFFFFF",
        background:str="#FFFFFF",
        placeholder:str="",
        cursor:str=""
    ):
        entry = ttk.Entry(
            master_widget,
            background=background,
            cursor=cursor,
            foreground=foreground,    
        )

        def FocusIn(event):
            
            
        entry.bind("<FocusIn>", lambda x:entry.insert(0, ""))
    
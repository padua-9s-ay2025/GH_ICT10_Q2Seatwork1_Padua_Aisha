# Inputs 

from pyscript import display, document

def show_nickname(e):
    nickname = document.getElementById("country_name").value
    document.getElementById("result").innerHTML = f"Nickname: {nickname}"
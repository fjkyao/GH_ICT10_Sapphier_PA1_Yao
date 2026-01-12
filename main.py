# if and if-else statement in Python
from pyscript import display, document


def temp_check(e):
    document.getElementById('output').innerhtml = ' '
    rusick = float(document.getElementById('input_temp').value)
    celsius = (rusick - 32) / (9/5)

    if celsius >= 37.8:
        display(f"Your temperature is {celsius:.2f} °C. You are sick", target="output")

    else: 
        display(f"Your temperature is {celsius:.2f} °C. You are fine :3", target="output")

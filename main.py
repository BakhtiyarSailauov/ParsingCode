import os
from input_modul import writer
from actions_modul import get_data_array

def play():
    try:
        os.mkdir("images_result")
    except:
        pass
    items = list(get_data_array())
    writer(items)

play()
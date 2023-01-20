import os
from input_modul import writer
from actions_modul import get_data_array

def play():
    try:
        os.mkdir("images_result")
    except:
        pass
    writer(get_data_array)

play()
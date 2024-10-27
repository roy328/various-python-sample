import pyautogui
from PIL import Image, ImageDraw
import csv
import pytesseract
import time
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# Define the region to capture

s_width, s_height = pyautogui.size()
region = (int(s_width * 0.25), int(s_height * 0.2), int(s_width * 0.61),  int(s_height * 0.1))
# region = (350, 250, 740, 300) 

def remove_single_quotes(input_string):
    return (input_string
	    .replace("() ", "")
            .replace("’", '')
            .replace("'", "")
            .replace("‘", "")
	    .replace('&', 'e')
            .replace('€', 'e')
	    .replace('I', 'l')
            .replace('|', 'l')
            .replace('U', 'l')
            .replace('L', 'l')
            .replace('é', 'e')
            .replace('è', 'e')
            .replace('ù', 'u')
            .replace('à', 'a')
            .replace('d', 'o')
            .replace('ò', 'o')
            .replace('0', 'o')
            .replace('  ', ' ')
            .replace(' } ', ' ') 
            .replace('- ', '-')
	    .replace('ll', 'i')
	    .replace('il', 'i')
            .replace('ii', 'i')
            .replace('i ', ' ')
            .replace('li', 'l')
            .replace('ti', 't')
	    .replace(' o', 'o')
            .replace('ee', 'e')
            .replace('do', 'o')
            .replace('od', 'o')
            .replace('oo', 'o')
            .replace(' a', 'a')
            .replace('o a', 'oa')
            .replace('li', 'l'))

def draw_dot(color):
    
    # Create the main window
    root = tk.Tk()
    root.geometry("5x5+800+500")    
    root.configure(background=color)
    root.overrideredirect(True)
    root.after(1000, root.destroy)

    root.mainloop()
    

def main_process():
    screenshot = pyautogui.screenshot(region=region)

    extracted_text = remove_single_quotes(pytesseract.image_to_string(screenshot).replace("\n", " ").rstrip())
    print(f'row string: {pytesseract.image_to_string(screenshot)}')
    screenshot.save("screenshot.png")

    filename = 'quizzes.csv'
    # filename = '~/Documents/driving/quizzes.csv'
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        
        header = next(csvreader)
        
        found = False
        for row in csvreader:
            cleaned_row = [remove_single_quotes(cell) for cell in row]
            if(extracted_text == ""):
                continue
	    
            if any(extracted_text in cell for cell in cleaned_row):
                print(f'Found in row: {row}')
                found = True
                if(row[1] == 'V'):
                    draw_dot('green')
                else:
                    draw_dot('red')
        if not found:
            print(f'String "{extracted_text}" not found in the CSV.')
            draw_dot('black')

while(1):
    try:
        main_process()
        time.sleep(1)

    except KeyboardInterrupt:
        break

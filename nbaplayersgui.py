import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def find_nba_player():
    target_player = player_entry.get()
    year = 1947
    i = 0

    while i < 77:
        url = 'https://basketball.realgm.com/nba/players/' + str(year)
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        for tr in soup.select('tbody tr'):
            values = tr.text.strip().split('\n')
            if target_player.lower() in values[0].lower():
                result_text.insert(tk.END, str(year - 1) + '\n')
        year += 1
        i += 1

def clear_result():
    result_text.delete(1.0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("NBA Player Finder")

# Create and place GUI widgets
player_label = tk.Label(root, text="What player are you trying to find:")
player_label.pack()

player_entry = tk.Entry(root, width=30)
player_entry.pack()

find_button = tk.Button(root, text="Find Player", command=find_nba_player)
find_button.pack()

clear_button = tk.Button(root, text="Clear Result", command=clear_result)
clear_button.pack()

result_label = tk.Label(root, text="Results:")
result_label.pack()

result_text = tk.Text(root, width=30, height=10)
result_text.pack()

root.mainloop()

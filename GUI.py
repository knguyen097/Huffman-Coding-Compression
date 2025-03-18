#simple python GUI

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo



def open_file():
    file_path = fd.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        selected_file_label.config(text=f"Selected file: {file_path}")
        process_file(file_path)


def process_file(file_path):
    #file processing logic goes here

    #1st , display contents of file

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            file_text.delete(1.0, tk.END)
            file_text.insert(tk.END, file_content)
    #erorr handling
    except Exception as e:
        selected_file_label.config(text=f"Error reading file: {e}")
    
    #2nd, perform Huffman encoding and display the result


#when button is pressed, perform huffman decoding and display the result
def huffman_decoding():
    #huffman decoding logic goes here

    #get input from huffman_text widget
    input = huffman_text.get(1.0, tk.END)
    huffman_text.delete


#create root window
root = tk.Tk()
root.title("Huffman App")
root.geometry("900x700")
root.config(background = "white")

#Title
title_lbl = tk.Label(root, text="Huffman Coding Compression Tool", font=("Arial", 16))
title_lbl.pack(padx=5, pady=5)

#Open file button
open_button = ttk.Button(root, text="Open File", command=open_file)
open_button.pack(padx=5, pady=5)

#Label to display selected file
selected_file_label = ttk.Label(root, text="No file selected", wraplength=200)
selected_file_label.pack()

#File contents label
lbl = tk.Label(root, text="File Contents:")
lbl.pack(padx=5, pady=5)

#Text widget to display file contents
file_text = tk.Text(root, height=7, width=80, wrap=tk.WORD)
file_text.pack(padx=5, pady=5)

#Huffman encoding label
huffman_lbl = tk.Label(root, text="Huffman Encoding:")
huffman_lbl.pack(padx=5, pady=5)

#Text widget to display Huffman encoding
huffman_text = tk.Text(root, height=7, width=80, wrap=tk.WORD)
huffman_text.pack(padx=5, pady=5)

#Huffman decoding button
decode_button = ttk.Button(root, text="Decode", command=huffman_decoding)
decode_button.pack(padx=5, pady=5)

#Text widget to display Huffman decoding
decode_text = tk.Text(root, height=7, width=80, wrap=tk.WORD)
decode_text.pack(padx=5, pady=5)

root.mainloop()

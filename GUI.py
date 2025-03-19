#simple python GUI

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import scrolledtext
from tkinter.messagebox import showinfo

import HuffmanCoding
from HuffmanCoding import *



def open_file():
    file_path = fd.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        selected_file_label.config(text=f"Selected file: {file_path}")
        process_file(file_path)

def open_file_to_decode():
    file_path = fd.askopenfilename(title="Select a File", filetypes=[("Binary files", "*.bin"), ("All files", "*.*")])
    if file_path:
        huffman_decoding(file_path)

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            file_text.delete(1.0, tk.END)
            file_text.insert(tk.END, file_content)
    except Exception as e:
        selected_file_label.config(text=f"Error reading file: {e}")
        return

    # Perform Huffman encoding and display the result
    try:
        root = hc.compress_file(file_path, "compressed.bin")
        huffman_text.delete(1.0, tk.END)
        huffman_text.insert("1.0", "\n".join(f"'{char}': {code}" for char, code in hc.codes.items()))
        selected_file_label.config(text="File compressed successfully!")
        return root  # Return the root for decompression
    except Exception as e:
        selected_file_label.config(text=f"Error during compression: {e}")

def huffman_decoding(file_path):
    try:
        root = process_file(file_path)  # Rebuild the Huffman tree
        hc.decompress_file("compressed.bin", "decompressed.txt", root)
        with open("decompressed.txt", "r") as f:
            decoded_text = f.read()
            decode_text.delete("1.0", tk.END)
            decode_text.insert("1.0", decoded_text)
        selected_file_label.config(text="File decompressed successfully!")
    except Exception as e:
        selected_file_label.config(text=f"Error during decompression: {e}")

#instantiate the HuffmanCoding class
hc = HuffmanCoding()

#-----------------------------Main GUI-----------------------------------

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
file_text = scrolledtext.ScrolledText(root, height=7, width=80, wrap=tk.WORD)
file_text.pack(padx=5, pady=5)

#Huffman encoding label
huffman_lbl = tk.Label(root, text="Huffman Encoding:")
huffman_lbl.pack(padx=5, pady=5)

#Text widget to display Huffman encoding
huffman_text = scrolledtext.ScrolledText(root, height=7, width=80, wrap=tk.WORD)
huffman_text.pack(padx=5, pady=5)

#Huffman decoding button
decode_button = ttk.Button(root, text="Decode", command=open_file_to_decode)
decode_button.pack(padx=5, pady=5)

#Text widget to display Huffman decoding
decode_text = scrolledtext.ScrolledText(root, height=7, width=80, wrap=tk.WORD)
decode_text.pack(padx=5, pady=5)

root.mainloop()

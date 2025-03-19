import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# Importing the HuffmanCoding class from backend
from HuffmanCoding import HuffmanCoding

huffman = HuffmanCoding()
root_node = None  

def open_file():
    file_path = fd.askopenfilename(
        title="Select a File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        selected_file_label.config(text=f"Selected file: {file_path}")
        process_file(file_path)

def process_file(file_path):
    global root_node
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        
        # Display the original text
        file_text.delete(1.0, tk.END)
        file_text.insert(tk.END, file_content)

        # Build the Huffman tree
        root_node = huffman.build_huffman_tree(file_content)
        # Generate Huffman codes
        huffman.generate_huffman_codes(root_node)
        # Generate the encoded text
        encoded_text = "".join(huffman.codes[char] for char in file_content)

        # Display the encoded text in the Huffman text widget
        huffman_text.delete(1.0, tk.END)
        huffman_text.insert(tk.END, encoded_text)

    except Exception as e:
        selected_file_label.config(text=f"Error reading file: {e}")

def huffman_decoding():
    global root_node
    if root_node is None:
        showinfo("Error", "No Huffman tree found. Please open and process a file first.")
        return
    
    encoded_str = huffman_text.get(1.0, tk.END).strip()
    if not encoded_str:
        showinfo("Error", "No encoded text to decode.")
        return
    
    decoded_str = ""
    current_node = root_node

    for bit in encoded_str:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right


        if current_node.char is not None:
            decoded_str += current_node.char
            current_node = root_node 
    

    decode_text.delete(1.0, tk.END)
    decode_text.insert(tk.END, decoded_str)

# ------------------- GUI SETUP -------------------
root = tk.Tk()
root.title("Huffman App")
root.geometry("900x700")
root.config(background="white")

# Title
title_lbl = tk.Label(root, text="Huffman Coding Compression Tool", font=("Arial", 16))
title_lbl.pack(padx=5, pady=5)

# Open file button
open_button = ttk.Button(root, text="Open File", command=open_file)
open_button.pack(padx=5, pady=5)

# Label to display selected file
selected_file_label = ttk.Label(root, text="No file selected", wraplength=200)
selected_file_label.pack()

# File contents label
lbl = tk.Label(root, text="File Contents:")
lbl.pack(padx=5, pady=5)

# Text widget to display file contents
file_text = tk.Text(root, height=7, width=80, wrap=tk.WORD)
file_text.pack(padx=5, pady=5)

# Huffman encoding label
huffman_lbl = tk.Label(root, text="Huffman Encoding:")
huffman_lbl.pack(padx=5, pady=5)

# Text widget to display Huffman encoding
huffman_text = tk.Text(root, height=7, width=80, wrap=tk.WORD)
huffman_text.pack(padx=5, pady=5)

# Huffman decoding button
decode_button = ttk.Button(root, text="Decode", command=huffman_decoding)
decode_button.pack(padx=5, pady=5)

# Text widget to display Huffman decoding
decode_text = tk.Text(root, height=7, width=80, wrap=tk.WORD)
decode_text.pack(padx=5, pady=5)

root.mainloop()

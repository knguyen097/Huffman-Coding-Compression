import heapq
import os
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self):
        self.codes = {}

    def build_huffman_tree(self, text):
        frequency = Counter(text)
        heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)
        
        return heap[0]

    def generate_huffman_codes(self, root, prefix=""):
        if root:
            if root.char is not None:
                self.codes[root.char] = prefix
            self.generate_huffman_codes(root.left, prefix + "0")
            self.generate_huffman_codes(root.right, prefix + "1")
    
    def display_codes(self):
        return self.codes  # Return the codes dictionary instead of printing

    def compress_file(self, input_file, output_file):
        with open(input_file, "r") as f:
            text = f.read()
        
        root = self.build_huffman_tree(text)
        self.generate_huffman_codes(root)
        
        encoded_text = "".join(self.codes[char] for char in text)
        padding = 8 - len(encoded_text) % 8
        encoded_text += "0" * padding
        
        byte_array = bytearray()
        for i in range(0, len(encoded_text), 8):
            byte_array.append(int(encoded_text[i:i+8], 2))
        
        with open(output_file, "wb") as f:
            f.write(bytes([padding]))  # Store padding at start
            f.write(bytes(byte_array))
            
        return root  # Return the root for decompression
    
    def decompress_file(self, input_file, output_file, root):
        try:
            with open(input_file, "rb") as f:
                padding = ord(f.read(1))  # Read padding
                byte_data = f.read()
            
            binary_string = "".join(f"{byte:08b}" for byte in byte_data)
            binary_string = binary_string[:-padding]  # Remove padding
            
            decoded_text = []
            node = root
            for bit in binary_string:
                node = node.left if bit == "0" else node.right
                if node.char is not None:
                    decoded_text.append(node.char)
                    node = root
            
            with open(output_file, "w") as f:
                f.write("".join(decoded_text))
            
            print(f"Decompressed file saved as {output_file}")
        except FileNotFoundError:
            print(f"Error: File {input_file} not found.")
        except Exception as e:
            print(f"Error during decompression: {e}")

if __name__ == "__main__":
    input_txt = "input.txt"
    compressed_file = "compressed.bin"
    decompressed_txt = "decompressed.txt"
    
    huffman = HuffmanCoding()
    root = huffman.compress_file(input_txt, compressed_file)
    huffman.decompress_file(compressed_file, decompressed_txt, root)

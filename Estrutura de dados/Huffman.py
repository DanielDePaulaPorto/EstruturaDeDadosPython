from collections import defaultdict
from heapq import heappush, heappop


class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_frequency_table(text):
    frequency_table = defaultdict(int)
    for char in text:
        frequency_table[char] += 1
    return frequency_table


def build_huffman_tree(frequency_table):
    heap = []
    for char, frequency in frequency_table.items():
        node = Node(char, frequency)
        heappush(heap, node)

    while len(heap) > 1:
        left_child = heappop(heap)
        right_child = heappop(heap)
        parent = Node(None, left_child.frequency + right_child.frequency)
        parent.left = left_child
        parent.right = right_child
        heappush(heap, parent)

    return heap[0]


def build_encoding_table(root):
    encoding_table = {}

    def build_code(node, code):
        if node.char is not None:
            encoding_table[node.char] = code
        else:
            build_code(node.left, code + '0')
            build_code(node.right, code + '1')

    build_code(root, '')
    return encoding_table


def huffman_encode(text):
    frequency_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)

    encoded_text = ''
    for char in text:
        encoded_text += encoding_table[char]

    return encoded_text


def huffman_decode(encoded_text, huffman_tree):
    decoded_text = ''
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree

    return decoded_text


def get_string_binaria(string):
    string_binaria = ""
    for caractere in string:
        valor_decimal = ord(caractere)
        valor_binario = bin(valor_decimal)[2:]  # [2:] para remover o prefixo "0b"
        string_binaria += valor_binario.zfill(8)  # zfill(8) para preencher com zeros à esquerda
    return string_binaria


# Exemplo de uso
texto = "Daniel de Paula Porto"

strinBinaria = get_string_binaria(texto)
print(f"Texto original: {strinBinaria}")

encoded_text = huffman_encode(texto)
print("Texto codificado:", encoded_text)

decoded_text = huffman_decode(encoded_text, build_huffman_tree(build_frequency_table(texto)))
print("Texto decodificado:", decoded_text)

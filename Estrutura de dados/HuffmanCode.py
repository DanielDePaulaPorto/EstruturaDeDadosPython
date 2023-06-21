from pythonds import BinaryTree

# Aluno - Gabriel Araujo De Paiva
# Árvore binária - Código de Huffman

huffman_codes_table = {}


def letters_quantity(text):
    hash_table = {}

    for letter in text:
        try:
            hash_table[letter] += 1
        except:
            hash_table[letter] = 1

    return sorted([BinaryTree(tuple([letter, hash_table[letter]])) for letter in hash_table], key=lambda n: -n.key[1])


def huffman_tree(nodes):
    while len(nodes) > 1:

        last = nodes.pop()
        penult = nodes.pop()

        dad = BinaryTree(tuple(['', last.key[1] + penult.key[1]]))
        dad.insertLeft(penult)
        dad.insertRight(last)

        for i in range(len(nodes)):
            if dad.getRootVal()[1] >= nodes[i].getRootVal()[1]:
                nodes.insert(i, dad)
                break

    return dad


def get_codes(node, code=""):
    if node.isLeaf():
        huffman_codes_table[node.key[0]] = code
    else:
        get_codes(node.leftChild, code + '0')
        get_codes(node.rightChild, code + '1')


def print_compressed_message(message):
    for character in message:
        print(huffman_codes_table[character], end='')
    print('\n')


text = input("\nDigite o texto a ser codificado aqui: ")

histogram = letters_quantity(text)
print(f"\nHash map das letras com suas respectivas quantidades:\n\t")

print('\t{')
for letter in histogram:
    print(f"\t {letter.key[0]} : {letter.key[1]}")
print('\t}')

r = huffman_tree(histogram)
print(f"\nÁrvore de Huffman escrita em ordem:\n\n")
r.inorder()

get_codes(r)
print(f"\nTabela de códigos por letra:\n\n\t{huffman_codes_table}\n")
print(f"Mensagem antes do processo de compressão de dados:\n\n", end='\t')

for character in text:
    print(f"{ord(character):08b}", end='')
print('\n')

print(f"Mensagem após o processo de compressão de dados:\n\n", end='\t')
print_compressed_message(text)

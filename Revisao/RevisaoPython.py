# REVISÃO DE PYTHON
# -----------------
# Daniel Porto
# Baseado em: https://www.freecodecamp.org/news/the-python-guide-for-beginners/
# -----------------

# Python é uma linguagem de programação interpretada, orientada a objetos, de alto nível e com semântica dinâmica.
# A simplicidade do Python reduz a manutenção de um programa. Python suporta módulos e pacotes,
# que encoraja a programação modularizada e reuso de códigos.
# É uma das linguagens que mais tem crescido devido sua compatibilidade (roda na maioria dos sistemas operacionais)
# e capacidade de auxiliar outras linguagens. Programas como Dropbox, Reddit e Instagram são escritos em Python.
# Python também é a linguagem mais popular para análise de dados e conquistou a comunidade científica.

# Python foi criada em 1990 por Guido Van Rossum no Centro de Matemática Stichting (CWI, veja http://www.cwi.nl)
# na Holanda como uma sucessora da linguagem ABC.
# A linguagem ABC foi desenhada para uso de não programadores, mas logo de início mostrou certas limitações e restrições.
# A maior reclamação dos primeiros alunos não programadores dessa linguagem era a presença de regras arbitrárias que as
# linguagens de programação haviam estabelecido tradicionalmente - muita coisa de baixo nível ainda era feita e não agradou o público.
# Guido então se lançou na tarefa de criar uma linguagem de script simples que possuísse algumas das melhores propriedades da ABC.
# Listas Python, dicionários, declarações básicas e uso obrigatório de indentação diferenciam Python da linguagem ABC.
# Guido pretendia que Python fosse uma segunda linguagem para programadores C ou C++ e não uma linguagem principal para programadores - o que mais tarde se tornou para os usuários de Python.

# Características:
# - linguagem de programação de alto nível
# - interpretada
# - modular
# - multiplataforma
# - orientada a objetos

# Para que é usada:
# - Scripting e automação
# - Desenvolvimento web
# - Enquadramento de testes
# - Big Data
# - Ciência de dados
# - Computação gráfica
# - Inteligência artificial

# -----------------------------

# A sintaxe
# Python é conhecida por sua sintaxe limpa.
# A linguagem evita o uso de caracteres desnecessários para indicar alguma especificidade.


# Ponto-e-vírgula
# Python não usa ponto-e-vírgula para terminar linhas.
# Uma nova linha é suficiente para dizer ao intérprete que um novo comando está começando.

# O método print() é usado para exibir algo no console.
# Neste exemplo, temos dois comandos que exibirão as mensagens dentro de aspas simples.

print('Primeiro comando')
print('Segundo comando')

# Mas o seguinte está "errado" devido aos ponto-e-vírgula no final:

print('Primeiro comando');
print('Segundo comando');


# Indentação
# Muitas linguagens utilizam chaves para definir o escopo.

# O intinterpretador Python usa apenas indentação para definir quando um escopo termina e outro começa.
# Isto significa que você tem que estar ciente dos espaços brancos no início de cada linha
# Eles têm significado e podem quebrar seu código se mal colocados
# Esta definição de uma função funciona:

def my_function():
    print('Primeiro comando')


# Essa aqui não funciona porque falta a recuo da segunda linha. Vai lançar um erro:
def my_function():
print('Primeiro comando')


# Variáveis e Case sensitivity
# Python é sensível a maiúsculas e minúsculas.
# Portanto, o nome e Nome das variáveis não são a mesma coisa e armazenam valores diferentes.

nome = 'Daniel'
Nome = 'Porto'


# As variáveis são facilmente criadas apenas atribuindo valores a elas usando o símbolo =
# Isto significa que nome armazena 'Daniel' e Nome armazena 'Porto'




# Comentários
# Finalmente, para comentar algo no código, pode-se o caracter hash #
# A parte comentada não influencia o fluxo do programa

# esta função imprime algo
def my_function():
    print('Primeiro comando')

# Quando você trabalha sozinho, talvez os comentários não sejam algo que você deva escrever. # Afinal, no momento, você sabe os porquês de cada linha de código.
# Mas se novas pessoas entrarem no seu projeto após um ano e o projeto tiver 3 módulos, cada um com 10.000 linhas de código?
# Pense em pessoas que não sabem nada sobre seu programa e que, de repente, estão tendo que mantê-lo, consertá-lo ou adicionar novas funcionalidades.
# Lembre-se, não há uma solução única para um determinado problema. Sua maneira de resolver as coisas é sua e somente sua.
# Se você pedir a 10 pessoas para resolver o mesmo problema, elas encontrarão 10 soluções diferentes.
# Se você quiser que outros entendam totalmente seu raciocínio, um bom projeto de código é obrigatório, mas os comentários são parte integrante de qualquer base de código.


# Como escrever comentários em Python
# A sintaxe dos comentários em Python é simples: basta usar o símbolo hash na frente do texto que você quer que seja um comentário.

# Este é um comentário e não influenciará o fluxo do meu programa
# Você pode usar um comentário para explicar o que algum pedaço de código faz.

# calcula a soma de quaisquer dois números dados
a + b


# Existem outras formas de se comentar um código, podendo fazê-lo na frente da linha digitada,
# ou usando três aspas simples (''') ou três aspas duplas (“””) para comentários que ultrapassam mais de uma linha.
# Veja a seguir:

soma = 5+5          # Criando uma variável de soma

'''
A partir do momento que coloquei três aspas simples, tudo o que eu escrever aqui dentro será considerado comentário.
É muito útil quando queremos explicar alguma coisa, ou deixar instruções dentro ou antes do código.
'''

"""
O mesmo ocorre com as aspas duplas.
Você pode escolher o que você quer usar.
A comunidade Python recomenda usar as aspas simples, mas fica a seu critério escolher.
"""


# Variáveis
# Em qualquer programa, você precisa armazenar e manipular dados para criar um fluxo ou alguma lógica específica.
# É para isso que servem as variáveis.
# Você pode ter uma variável para armazenar um nome, outra para armazenar a idade de uma pessoa,
# ou até mesmo usar um tipo mais complexo para armazenar tudo isso de uma vez, como um dicionário.

# Criar, também conhecido como Declarar
# Declarar uma variável é uma operação básica e direta em Python

# Basta escolher um nome e atribuir um valor a ele usando o símbolo =

nome = 'Matuzalem'

idade = 32
# Você pode usar a função print() para mostrar o valor de uma variável

print(nome)

print(idade)

# Note que em Python não há nenhuma palavra especial para declarar uma variável.
# No momento em que você atribui um valor, a variável é criada na memória.
# Python também tem tipagem dinâmica, o que significa que você não precisa dizer se sua variável é um texto ou um número, por exemplo.
# O interpretador infere a tipagem com base no valor atribuído.
# Se você precisar, você também pode redeclarar uma variável apenas alterando seu valor.

# declarando o nome como uma string
nome = 'Matuzalem'

# re-declarando o nome como um int
nome = 32

# Tenha em mente, no entanto, que isto não é recomendado, uma vez que as variáveis devem ter significado e contexto.
# Se eu tiver uma variável chamada nome, não espero que ela tenha um número armazenado nela.



# Conveção de nomenclatura
# Use nomes significativos. Não use nomes aleatórios de variáveis como x ou y.
# Digamos que você queira armazenar a hora de uma festa, basta chamá-la de hora_festa.
# Você notou o sublinhado _ ?
# Por convenção, se você quiser usar um nome variável que seja composto de duas ou mais palavras, você as separa por sublinhados. Isto é chamado de Snake Case.
# Outra opção seria usar CamelCase como em horaFesta. Isto é muito comum em outras línguas, mas não a convenção em Python, como já foi dito anteriormente.
# Lembre-se que as variáveis são sensíveis a maiúsculas e minúsculas, portanto, hora_festa e Hora_festa não são a mesma coisa. Além disso, tenha em mente que a convenção nos diz para usarmos sempre letras minúsculas.
# Lembre-se, use nomes que você possa lembrar facilmente dentro de seu programa. A má nomenclatura pode lhe custar muito tempo e causar bugs irritantes.

# Em resumo, sobre os nomes de variáveis:

# são sensíveis a maiúsculas e minúsculas: tempo e TEMPO não são a mesma coisa
# têm que começar com um sublinhado _ ou uma letra (NÃO comece com um número!)
# têm permissão para ter apenas números, letras e sublinhados. Nenhum caractere especial como: #, $, &, @, etc.
# Isto, por exemplo, não é permitido: hora#festa, 10horafesta.




# Tipos
# Para armazenar dados em Python você precisa usar uma variável. E cada variável tem seu tipo, dependendo do valor dos dados armazenados.
# Python tem tipagem dinâmica, o que significa que você não precisa declarar explicitamente o tipo de sua variável, mas se você quiser, você pode.


# Determinando o tipo
# Antes de tudo, vamos aprender como determinar o tipo de dados.

# Basta usar a função type() e passar a variável de sua escolha como um argumento, como o exemplo abaixo.

print(type(minha_variavel))

# Booleano
# O tipo booleano é um dos tipos mais básicos de programação.
# Uma variável do tipo booleano só pode representar verdadeiro ou falso.

valor_booleano = True
print(type(valor_booleano))

valor_booleano = bool(1024)
print(type(valor_booleano))

# Números
# Existem três tipos de números: int, float e complexo.

# Inteiro
valor_inteiro = 32
print(type(valor_inteiro))

valor_inteiro = int(32)
print(type(valor_inteiro))

# Ponto flutuante - Real
valor_real = 32.85   # Usar o . como separador de casa decimal. Está em Inglês!
print(type(valor_real))

valor_real = float(32.85)
print(type(valor_real))

# Complexo
valor_complexo = 32+4j
print(type(valor_complexo))

valor_complexo = complex(32+4j)
print(type(valor_complexo))


# String (texto)
# O tipo texto é um dos tipos mais comuns e é frequentemente chamado de string ou, em Python, apenas str.

minha_cidade = "Porto Velho"
print(type(minha_cidade))

# As áspas simples têm exatamente o mesmo uso que as áspas duplas
minha_cidade = "Porto Velho"
print(type(minha_cidade))

# Definindo explicitamente o tipo de variável
minha_cidade = str("Porto Velho")
print(type(minha_cidade))

# Você pode usar o + operador para concatenar as strings.
# A concatenação é quando você tem duas ou mais strings e deseja juntá-las em uma só.

palavra1 = 'Porto '
palavra2 = 'Velho'

print(palavra1 + palavra2)

# O tipo de string tem muitos métodos embutidos que nos permitem manipulá-los:
 # A função len() retorna o comprimento de uma string.

print(len('Porto Velho'))

# O método replace() substitui uma parte da string por outra.
# Como exemplo, vamos substituir 'Velho' por 'Seguro'.

print('Porto Velho'.replace('Velho', 'Seguro'))

# O método upper() devolverá todos os caracteres como maiúsculas.

print('Porto Velho'.upper())

# O método lower() faz o oposto, e retorna todos os caracteres em minúsculas.

print('Porto Velho'.lower())

# Mudança de tipos - Typecasting
# Permite a conversão entre diferentes tipos.
# Assim você pode ter um int transformado em um str, ou um float transformado em uma int, por exemplo.


# Conversão explícita
# Para transformar uma variável para uma string basta usar a função str().

# Esta é apenas uma intialização explícita
variavel_string = str('32')
print(variavel_string)

# int to str
variavel_string = str(32)
print(variavel_string)

# float to str
variavel_string = str(32.0)
print(variavel_string)

# Para transformar uma variável para um número inteiro, basta usar a função int().

 # Esta é apenas uma intialização explícita
variavel_inteiro = int(32)
print(variavel_inteiro)

# float to int: arredondamento para baixo (para 3)
variavel_inteiro = int(3.2)
print(variavel_inteiro)

# str to int
variavel_inteiro = int('32')
print(variavel_inteiro)

# Para transformar uma variável para um ponto flutuante basta usar a função float().

 # Esta é uma intialização explícita
variavel_float = float(3.2)
print(variavel_float)

# int para flutuar
variavel_float = float(32)
print(variavel_float)

# str to float
variavel_float = float('32')
print(variavel_float)

# Acima temos a conversão explícita do tipo.
# Em alguns casos você não precisa fazer a conversão explicitamente, já que Python pode fazê-lo por si só.


# Conversão implícita
# O exemplo abaixo mostra a conversão implícita ao adicionar um int e um float.

# Note que minha_soma é do tipo float.
# Python usa float para evitar perda de dados, uma vez que o tipo de int não pode representar os dígitos decimais.

variavel_int = 32
variavel_float = 3.2

minha_soma = variavel_int + variavel_float

print(minha_soma)
print(type(minha_soma))

# Por outro lado, neste exemplo, quando se adiciona um int e um str, Python não será capaz de fazer a conversão
# implícita, e a conversão do tipo explícito é necessária

variavel_int = 32
variavel_string = '32'

# trabalhos explícitos de conversão
minha_soma = variavel_int + int(variavel_string)
print(minha_soma)

# a conversão implícita lança um erro
minha_soma = variavel_int + variavel_string

# O mesmo erro é lançado quando se tenta adicionar tipos float e strings sem fazer uma conversão explícita.

variavel_float = 3.2
variavel_string = '32'

# trabalhos explícitos de conversão
minha_soma = variavel_float + float(variavel_string)
print(minha_soma)

# a conversão implícita lança um erro
minha_soma = variavel_float + variavel_string




# Entrada de usuário
# Se você precisar interagir com um usuário ao executar seu programa na linha de comando
# (por exemplo, para pedir uma informação), você pode usar a função input().

pais = input("Qual é seu país?") # usuário entra em 'Brasil'.
print(pais)

# O valor capturado é sempre string. Basta lembrar que você pode precisar convertê-lo usando a digitação.

idade = input("Quantos anos você tem?") # o usuário entra '29'

print(idade)
print(type(idade))
idade = int(idade)
print(type(idade))

# Observe que a idade de 29 anos é capturada como string e depois convertida explicitamente para int.




# Operadores
# Em uma linguagem de programação, os operadores são símbolos especiais que você pode aplicar a suas variáveis e
# valores a fim de realizar operações como aritmética/matemática e comparação.

# Python tem muitos operadores que você pode aplicar a suas variáveis e eu vou demonstrar os mais utilizados.


# Operadores aritméticos
# Os operadores aritméticos são o tipo mais comum de operadores e também os mais reconhecíveis.
# Eles permitem que você realize operações matemáticas simples.
# Eles são:
# +: Adição
# -: Subtração
# *: Multiplicação
# /: Divisão
# **: Exponenciação
# //: Divisão de Piso, redondeia o resultado de uma divisão
# %: Modulus, dá o restante de uma divisão
# Vamos ver um programa que mostra como cada uma delas é utilizada.

print('Adição:', 5 + 2)
print('Subtração:', 5 - 2)
print('Multiplicação:', 5 * 2)
print('Divisão:', 5 / 2)
print('Divisão inteira:', 5 // 2)
print('Exponenciação:', 5 ** 2)
print('Módulo:', 5 % 2)


# Concatenação
# A concatenação é quando você tem duas ou mais cordas e quer juntá-las em uma só.
# Isto é útil quando você tem informações em múltiplas variáveis e quer combiná-las.
# Por exemplo, neste próximo exemplo, eu combino duas variáveis que contêm meu primeiro nome e meu sobrenome respectivamente para ter meu nome completo.
# O operador + também é usado para concatenar.

primeiro_nome = 'Daniel'
ultimo_nome = 'Porto'

print(primeiro_nome + ultimo_nome)

# Como a concatenação é aplicada a strings, para concatenar strings com outros tipos, é necessário fazer uma
# digitação explícita usando str().
# Tenho que digitar o valor int 30 para concatenar a string com str() para concatená-la com o resto da string.

idade = 'Eu tenho ' + str(30) + ' anos de idade'
print(idade)


# Operadores de Comparação
# Use operadores de comparação para comparar dois valores.
# Estes operadores retornam Verdadeiro ou Falso.
# Eles são:

# ==: Igual
# !=: Não iguais
# >: Maiores do que
# <: Menor do que
# >=: Maior ou igual a
# <=: Menor ou igual a
# Vamos ver um programa que mostra como cada um deles é usado.

print('Igual:', 5 == 2)
print('Não igual:', 5 != 2)
print('Maior do que:', 5 > 2)
print('Menor do que:', 5 < 2)
print('Maior ou igual a:', 5 >= 2)
print('Menor ou igual a:', 5 <= 2)


# Operadores de Atribuição
# Como o nome indica, estes operadores são usados para atribuir valores a variáveis.
# x = 7 no primeiro exemplo é uma atribuição direta que armazena o número 7 na variável x.
# A operação de atribuição toma o valor à direita e o atribui à variável à esquerda.
# Os outros operadores são abreviações simples para os Operadores Aritméticos.
# No segundo exemplo, x começa com 7 e x += 2 é apenas outra forma de escrever x = x + 2.
# Isto significa que o valor anterior de x é adicionado por 2 e reatribuído a x que agora é igual a 9.

# =: atribuição simples
x = 7
print(x)

# +=: adição e atribuição
x = 7
x += 2
print(x)

# -=: subtração e atribuição
x = 7
x -= 2
print(x)

# *=: multiplicação e atribuição
x = 7
x *= 2
print(x)

# /=: divisão e atribuição
x = 7
x /= 2
print(x)

# %=: módulo e atribuição
x = 7
x %= 2
print(x)

# //=: divisão e atribuição de andares
x = 7
x //= 2
print(x)

# **=: exponenciação e atribuição
x = 7
x **= 2
print(x)


# Operadores lógicos
# Operadores lógicos são usados para combinar declarações aplicando álgebra booleana.

# Eles são:
# e: Verdade somente quando ambas as afirmações são verdadeiras
# ou: Falso somente quando ambos x e y são falsos
# não: O operador não operador simplesmente inverte a entrada, True torna-se Falso e vice-versa.
# Vamos ver um programa que mostra como cada um é utilizado.

x = 5
y = 2
print(x == 5 and y > 3)
print(x == 5 or y > 3)
print(not (x == 5))




# Condicionais
# Os condicionais são uma das pedras angulares de qualquer linguagem de programação.
# Eles permitem controlar o fluxo do programa de acordo com condições específicas que você pode verificar.
# A forma como você implementa um condicional é através da declaração de se.

# A forma geral de uma declaração de if é:

if expression:
    statement

# A expressão contém alguma lógica que retorna um booleano,
# e a declaração é executada somente se o retorno for Verdadeiro.

 # Um exemplo simples:

idade_Conan = 32
idade_Xena = 29

if idade_Conan > idade_Xena:
    print('Conan é mais velho que Xena')

# Temos duas variáveis que indicam as idades de Conan e Xena. A condição em inglês simples diz
# "se a idade de Conan é maior do que a de Xena, então imprima a frase 'Conan é mais velho que Xena'".
# Como a condição retorna True, a frase será impressa no console.

# No nosso último exemplo, o programa só faz algo se a condição retorna True.
# Mas também queremos que ele faça algo se retornar Falso ou mesmo verificar uma segunda ou terceira condição se a primeira não foi atendida.
# Neste exemplo, trocamos a idade de Conan e Xena.
 # A primeira condição retornará Falso desde que Xena é mais velha agora, e então o programa imprimirá a frase depois da outra, em vez disso.

idade_Conan = 29
idade_Xena = 32

if idade_Conan > idade_Xena:
    print('Conan é mais velho que Xena')
else:
    print('Conan é mais jovem que Xena')

# Agora, considere o exemplo abaixo com o elif.

idade_Conan = 32
idade_Xena = 32

if idade_Conan > idade_Xena:
    print('Conan é mais velho que Xena')
elif idade_Conan == idade_Xena:
    print('Conan e Xena têm a mesma idade')
else:
    print('Conan é mais jovem que Xena')


# O objetivo do elif é fornecer uma nova condição a ser verificada antes que a outra seja executada.
# Mais uma vez mudamos suas idades e agora ambos têm 32 anos de idade.

# Como tal, a condição no elif é cumprida. Como ambos têm a mesma idade, o programa irá imprimir
# "Conan e Xena têm a mesma idade".

# Note que você pode ter quantos elifs quiser, basta colocá-los em sequência.

idade_Conan = 32
idade_Xena = 32

if idade_Conan > idade_Xena:
    print('Conan é mais velho que Xena')
elif idade_Conan < idade_Xena:
    print('Conan é mais jovem que Xena')
elif idade_Conan == idade_Xena:
    print('Conan e Xena têm a mesma idade')
else:
    print('Este nunca é executado')


# Neste exemplo, o else nunca é executado porque todas as possibilidades estão cobertas nas condições anteriores e,
# portanto, poderiam ser removido.


# Condicionais aninhadas
# Você pode precisar verificar mais de uma condição para que algo aconteça.

# Neste caso, você pode aninhar suas declarações.

 # Por exemplo, a segunda frase "Conan é o mais velho" é impressa somente se ambos os ifs passarem.

idade_Conan = 32
idade_Xena = 28
idade_Hercules = 25


if idade_Conan > idade_Xena:
    print('Conan é mais velho que Xena')
    if idade_Conan > idade_Hercules:
        print('Conan é o mais velho')

# Ou, dependendo da lógica, torná-la mais simples com Álgebra Booleana.
# Desta forma, seu código é menor, mais legível e mais fácil de manter.

idade_Conan = 32
idade_Xena = 28
idade_Hercules = 25


if idade_Conan > idade_Xena and idade_Conan > idade_Hercules:
    print('Conan é o mais velho')




# Operadores Ternários
# O operador ternário é uma declaração de uma linha se.

# É muito útil para condições simples.

# Este é o aspecto:
# <expressão> se <condição> outra <expressão>
# Considere o seguinte código Python:

a = 25
b = 50
x = 0
y = 1

resultado = x if a > b else y

print(resultado)

# Aqui usamos quatro variáveis, a e b são para a condição, enquanto x e y representam as expressões.
# a e b são os valores que estamos verificando uns contra os outros para avaliar alguma condição.
# Neste caso, estamos verificando se a é maior que b.
# Se a expressão for verdadeira, isto é, a for maior que b, então o valor de x será atribuído ao resultado que será igual a 0.
# Entretanto, se a for menor que b, então teremos o valor de y atribuído ao resultado, e o resultado manterá o valor 1.
# Como a é menor que b, 25 < 50, o resultado terá 1 como valor final de y.

# A maneira mais fácil de lembrar como a condição é avaliada é lê-la em inglês simples.

# Nosso exemplo seria: o resultado será x se a for maior que b; caso contrário será y.


# while Loops
# Loops são usados quando você precisa repetir um bloco de código um certo número de vezes ou aplicar a mesma lógica
# sobre cada item de uma coleção.

# Há dois tipos de loops: for e while.

 # Sintaxe básica
# A sintaxe básica de um loop while é a seguinte.

while condition:
    statement

# O laço continuará enquanto a condição for verdadeira.

# Ex: O quadrado de um número. O exemplo abaixo toma cada valor de número e calcula seu valor quadrático.

numero = 1
while numero <= 5:
    print(numero, 'ao quadrado é', numero ** 2)
    numero = numero + 1

# Você pode usar qualquer nome variável, mas eu escolhi o número porque faz sentido no contexto.
# Uma escolha genérica comum seria simplesmente i.

# O laço continuará até que o número (inicializado com 1) seja menor ou igual a 5.
# Observe que após o comando print(), o número da variável é incrementado em 1 para tomar o próximo valor.

# Se você não fizer a incrementação, você terá um loop infinito, pois o número nunca alcançará um valor maior que 5.
# Este é um detalhe muito importante!


# Bloco else
# Quando a condição retornar Falso, o bloco else será chamado.

numero = 1
while numero <= 5:
    print(numero, 'ao quadrado é', numero ** 2)
    numero = numero + 1
else:
    print('Não sobraram números!')

# Observe que a frase 'Não sobraram números!' é impressa após o fim do laço, ou seja, após o número da condição <= 5
# avalia para Falso.


# Como quebrar um loop em Python
# Simplesmente use a palavra-chave break, e o loop irá parar sua execução.

numero = 1
while numero <= 5:
    print(numero, 'ao quadrado é', numero ** 2)
    numero = numero + 1
    if numero == 4:
        break

# O loop funciona normalmente, e quando o número chega a 4 a declaração se avalia para True e o comando de quebra
# (break) é chamado. Isto termina o loop antes que o valor ao quadrado dos números 4 e 5 seja calculado.


# Como pular um item em um loop de tempo
# O continue fará isso por você.

# Tive que inverter a ordem da instrução if e da impressão() para mostrar como ela funciona corretamente.

numero = 1
while numero <= 5:
    numero = numero + 1
    if numero == 4:
        continue
    print(numero, 'ao quadrado é', numero ** 2)

# O programa sempre verifica se 4 é o valor atual do número. Se for, o quadrado de 4 não será calculado e o
# continue saltará para a próxima iteração quando o valor do número for 5.
# *


# Loops for
# Loops for são similares aos loops while no sentido de que são usados para repetir blocos de código.

# A diferença mais importante é que você pode facilmente iterar sobre os tipos seqüenciais.

# Sintaxe básica
# A sintaxe básica de um para loop é a que se segue.

for item in coleção:
    declaração


# Para passar por uma lista
# Para percorrer uma lista ou qualquer outra coleção, basta proceder como mostrado no exemplo abaixo.

carros = ['BMW', 'Ferrari', 'McLaren']
for carro in carros:
    print(carro)

# A lista de carros contém três itens. O loop for irá iterar sobre a lista e armazenar cada item na variável do carro,
# e então executar uma declaração, neste caso imprimir (carro), para imprimir cada carro no console.
#  A função para loop é amplamente utilizada para loops porque lhe dá uma maneira simples de listar números.

 # Este código fará um loop através dos números de 0 a 5 e imprimirá cada um deles.

for numero in range(5):
    print(numero)

# Por outro lado, sem a função de range(), faríamos algo assim.

numeros = [0, 1, 2, 3, 4]
for numero in numeros:
    print(numero)

# Você também pode definir um inicio e um fim usando o range().

 # Aqui estamos começando em 5 e parando em 10. O número que você definir para parar não está incluído.

for numero in range(5, 10):
    print(numero)

# Finalmente, também é possível definir um passo.
# Aqui começamos em 10 e aumentamos em 2 até 20, já que 20 é a parada, ela não está incluída.

for numero in range(10, 20, 2):
    print(numero)


# Bloco else
# Quando os itens da lista tiverem terminado, o bloco else será chamado.

carros = ['BMW', 'Ferrari', 'McLaren']
for carro in carros:
    print(carro)
else:
    print('Não há mais carros!')

# Como sair de um loop for em Python
# Simplesmente use a palavra-chave break, e o loop irá parar sua execução.

carros = ['BMW', 'Ferrari', 'McLaren']
for carro in carros:
    print(carro)
    if carro == 'Ferrari':
        break

# O loop irá iterar através da lista e imprimir cada carro.

# Neste caso, após o loop chegar a 'Ferrari', o break é chamado e a 'McLaren' não será impressa.


# Como pular um item em um loop
# Nesta seção, aprenderemos como continue pode fazer isso por você.

# Tive que inverter a ordem da declaração de se e continuar mostrando como ela funciona corretamente.

# Note que eu sempre verifico se 'Ferrari' é o item atual.
# Se for, 'Ferrari' não será impresso, e o continue irá pular para o próximo item 'McLaren'.

carros = ['BMW', 'Ferrari', 'McLaren']
for carro in carros:
    if carro == 'Ferrari':
        continue
    print(carro)

# Loop dentro de Loop: Loops aninhados
# Às vezes você tem coleções mais complexas, como uma lista de listas.
# Para iterar sobre estas listas, você precisa aninhar-se para os loops.
# Neste caso, eu tenho três listas: uma de modelos BMW, outra de modelos Ferrari e finalmente uma com modelos McLaren.
# A primeira iteração de loop sobre a lista de cada marca, e a segunda irá iterar sobre os modelos de cada marca.

modelo_carros = [
    ['BMW I8', 'BMW X3',
     'BMW X1'],
    ['Ferrari 812', 'Ferrari F8',
     'Ferrari GTC4'],
    ['McLaren 570S', 'McLaren 570GT',
     'McLaren 720S']
]

for marca in modelo_carros:
    for modelo in marca:
        print(modelo)

# Loop sobre outras estruturas de dados
# A mesma lógica que se aplica para loops sobre uma lista pode ser estendida às outras estruturas de dados:
# tuple, set, e dicionário.

# Como fazer um loop básico sobre cada uma delas:

 # loop com uma Tuple
pessoas = ('Conan', 'Xena')
for pessoa in pessoas:
    print(pessoa)

# Loop com uma set
pessoas = ('Conan', 'Xena')
for pessoa in pessoas:
    print(pessoa)

# Loop com um Dicionário
# Para imprimir as chaves:
pessoas = {'Conan': 30, 'Xena': 25}
for pessoa in pessoas:
    print(pessoa)

# Para imprimir os valores:
pessoas = {'Conan': 30, 'Xena': 25}
for pessoa in pessoas:
    print(pessoas[pessoa])




# Operadores de associação
# Estes operadores fornecem uma maneira fácil de verificar se um determinado objeto está presente em uma sequência:
# string, lista, tupla, set e dicionário.

# Estes operadores são:

# in: retorna Verdadeiro se o objeto está presente
# not in: retorna Verdadeiro se o objeto não está presente
# Vamos ver um programa que mostra como cada um deles é utilizado.

lista_número = [1, 2, 4, 5, 6]
print(1 in number_list)
print(5 not in number_list)
print(3 not in number_list)


# Listas
# Uma lista tem os seus itens ordenados e podemos adicionar o mesmo item quantas vezes quisermos.
# Um detalhe importante é que as listas são mutáveis!
# Mutabilidade significa que pode alterar uma lista após a sua criação, adicionando itens, removendo-os, ou mesmo apenas alterando os seus valores.

# Inicialização
# Lista Vazia
pessoas = []

# Lista com valores iniciais
pessoas = ['Bob', 'Mary']

# Adicionando numa lista
# Para adicionar um item no final de uma lista, utilize o append().
pessoas = ['Bob', 'Mary']
pessoas.append('Sarah')

print(pessoas)

# Para especificar a posição para o novo item, devemos utilizar o método insert().
pessoas = ['Bob', 'Mary']
pessoas.insert(0, 'Sarah')

print(pessoas)

# Atualização numa lista
# Especifique a posição do item a atualizar e defina o novo valor
pessoas = ['Bob', 'Mary']
pessoas[1] = 'Sarah'
print(pessoas)

# Remoção em um lista
# Utilizar o método remove() para eliminar o item passado como argumento.
pessoas = ['Bob', 'Mary']
pessoas.remove('Bob')
print(pessoas)

# Para apagar toda a lista, utilizar o método clear():
pessoas = ['Bob', 'Mary']
pessoas.clear()

# Recuperando numa lista
# Use o índice para referenciar o item.
# Lembre-se de que o índice começa em 0.
# Por isso, para recuperar o segundo item, utilize o índice 1.
pessoas = ['Bob', 'Mary']
print(pessoas[1])

# Verificar se um determinado item já existe numa Lista
pessoas = ['Bob', 'Mary']

if 'Bob' in pessoas:
  print('Bob existe!')
else:
  print('Não existe Bob!')




# Tuplas
# Um tupla é semelhante a uma lista: é ordenada, e permite a repetição de itens.
# Há apenas uma diferença: um tupla é imutável.
# A imutabilidade, significa que não se pode mudar uma tupla após a sua criação.
# Se tentarmos adicionar um item ou atualizar um item, por exemplo, o interpretador Python irá mostrar um erro.

# Inicialização
# Tupla Vazio
pessoas = ()

# Tupla com valores iniciais
pessoas = ('Bob', 'Mary')

# Adicionando numa Tupla
# As tuplas são imutáveis. Isto significa que, se tentarmos adicionar um item, teremos um erro.
pessoas = ('Bob', 'Mary')
pessoas[2] = 'Sarah'

# Atualização num Tupla
# A atualização de um item também devolverá um erro.

# Mas há um truque: podemos converter a tupla numa lista, alterar o item, e depois convertê-la de volta para uma Tupla.
pessoas = ('Bob', 'Mary')
lista_de_pessoas = list(pessoas)
lista_de_pessoas[1] = 'Sarah'
pessoas = tuple(lista_de_pessoas)
print(pessoas)

# Remoção em uma Tupla
# Pela mesma razão que não se pode adicionar um item, também não se pode apagar um item, uma vez que são imutáveis.

# Recuperando num Tupla
# Use o índice para referenciar o item.
pessoas = ('Bob', 'Mary')
print(pessoas[1])

# Verificar se um determinado item já existe num Tupla
pessoas = ('Bob', 'Mary')

if 'Bob' in pessoas:
  print('Bob existe!')
else:
  print('Não existe Bob!')




# Sets
# Os Sets não garantem a ordem dos itens e não são indexados.
# Um ponto chave ao utilizar sets: não permitem a repetição de um item.

# Inicialização
# Set Vazio
pessoas = set()

# Set com valores iniciais
pessoas = {'Bob', 'Mary'}

# Adicionando num Set
# Use o método add() para adicionar um item.
pessoas.add('Sarah')

# Utilizar o método update() para adicionar vários itens ao mesmo tempo.
pessoas.update(['Carol', 'Susan'])

# Lembre-se, os sets não permitem a repetição, por isso se voltar a acrescentar 'Mary', nada muda.
pessoas = {'Bob', 'Mary'}
pessoas.add('Mary')
print(pessoas)

# Atualização em um Set
# Os itens de um set não são mutáveis. É necessário adicionar ou apagar um item.

# Remoção em um Set
# Para remover Bob do set:

pessoas = {'Bob', 'Mary'}
pessoas.remove('Bob')
print(pessoas)

# Para apagar todo o set:
pessoas.clear()

# Verificar se um determinado item já existe em um set
pessoas = {'Bob', 'Mary'}

if 'Bob' in pessoas:
  print('Bob existe!')
else:
  print('Não existe Bob!')




# Dicionários
# O dicionário não garante a ordem dos elementos e é mutável.
# Uma característica importante dos dicionários é que podemos definir as suas chaves de acesso personalizadas para cada elemento.

# Inicialização de um Dicionário
# Dicionário Vazio
pessoas = {}

# Dicionário com valores iniciais
pessoas = {'Bob':30, 'Mary':25}

# Adicionando em um Dicionário
# Se a chave ainda não existe, é anexada ao dicionário.
pessoas['Sarah'] = 32

# Atualização de um Dicionário
# Se a chave já existir, o valor é apenas atualizado.

#A idade do Bob é agora 28 anos
pessoas['Bob'] = 28

# Repare que o código é praticamente o mesmo.

# Remoção em um Dicionário
# Para remover Bob do dicionário:
pessoas.pop('Bob')

# Para apagar todo o dicionário:
pessoas.clear()

# Recuperação de um valor no Dicionário
bob_age = pessoas['Bob']
print(bob_age)

# Verificar se uma determinada chave já existe num Dicionário
if 'Bob' in pessoas:
  print('Bob existe!')
else:
  print('Não existe Bob!')




# Funções
# À medida que o código cresce, a complexidade também cresce. E as funções ajudam a organizar o código.
# As funções são uma maneira útil de criar blocos de código que você pode reutilizar.

# Definição e Chamada
# Em Python use a palavra-chave def para definir uma função.

# Dar-lhe um nome e usar parênteses para informar 0 ou mais argumentos.
# Na linha após o início da declaração, lembre-se de recuar o bloco de código.

# Aqui está um exemplo de uma função chamada minha_primeira_funcao() que imprime apenas uma frase 'Minha primeira função!'

# Para chamar a função basta usar seu nome, conforme definido.

def minha_primeira_funcao():
    print('Minha primeira função!')

minha_primeira_funcao()


# Retornar um valor
# Use a palavra-chave return para retornar um valor da função.

# Neste exemplo, a função segunda_funcao() retorna a string 'Minha segunda função!'
# Note que print() é uma função embutida e nossa função é chamada de dentro dela.
# A string retornada pela second_function() é passada como um argumento para a função print().

def segunda_funcao():
    return 'Minha segunda função!'

print(segunda_funcao())


# retornar múltiplos valores
# Funções também podem retornar múltiplos valores ao mesmo tempo.

# retorna_numeros() retorna dois valores simultaneamente.

def retorna_numeros():
    return 10, 2


print(retorna_numeros())


# Argumentos
# Você pode definir parâmetros entre os parênteses.
# Ao chamar uma função com parâmetros você tem que passar argumentos de acordo com os parâmetros definidos.
# Os exemplos anteriores não tinham parâmetros, portanto, não havia necessidade de argumentos.
# Os parênteses permaneceram vazios quando as funções foram chamadas.

# Um argumento
# Para especificar um parâmetro, basta defini-lo dentro dos parênteses.
# Neste exemplo, a função meu_numero espera um número como argumento definido pelo número do parâmetro.
# O valor do argumento é então acessível dentro da função a ser utilizada.

def meu_numero(num):
    return 'Meu número é: ' + str(num)


print(meu_numero(10))


# Dois ou mais argumentos
# Para definir mais parâmetros, basta usar uma vírgula para separá-los.
# Aqui temos uma função adicionar que acrescenta dois números.
# Ela espera dois argumentos definidos por primeiro_numero e segundo_numero.
# Os argumentos são adicionados pelo operador + e o resultado é então retornado pelo return.

def adicionar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

print(adicionar(10, 2))


# Este exemplo é muito parecido com o último. A única diferença é que temos 3 parâmetros em vez de 2.

def adicionar(primeiro_numero, segundo_numero, terceiro_numero):
    return primeiro_numero + segundo_numero + terceiro_numero

print(adicionar(10, 2, 3))


# Esta lógica de definir parâmetros e passar argumentos é a mesma para qualquer número de parâmetros.
# É importante ressaltar que os argumentos devem ser passados na mesma ordem em que os parâmetros são definidos.


# Valor padrão.
# Você pode definir um valor padrão para um parâmetro se nenhum argumento for dado usando o operador = e um valor de escolha.
# Nesta função, se nenhum argumento for dado, o número 30 é assumido como o valor esperado por padrão.

def meu_numero(meu_numero=30):
    return 'Meu número é: ' + str(meu_numero)


print(meu_numero(10))
print(meu_numero())


# Palavras-chave ou Argumentos nomeados
# Quando se chama uma função, a ordem dos argumentos tem que corresponder à ordem dos parâmetros.
# A alternativa é se você usar a palavra-chave ou argumentos nomeados.
# Ajuste os argumentos para seus respectivos parâmetros diretamente, usando o nome dos parâmetros e os = operadores.
# Este exemplo inverte os argumentos, mas a função funciona como esperado porque eu lhe digo qual valor vai para qual parâmetro pelo nome.

def meus_numeros(primeiro_numero, segundo_numero):
    return 'Os números são: ' + str(primeiro_numero) + ' e ' + str(segundo_numero)


print(meus_numeros(segundo_numero=30, primeiro_numero=10))


# Qualquer número de argumentos: *args Se você não quiser especificar o número de parâmetros, basta usar o * antes do
# nome do parâmetro. Em seguida, a função levará tantos argumentos quantos forem necessários.

# O nome do parâmetro pode ser qualquer coisa como *numbers, mas existe uma convenção em Python para usar *args
# para esta definição de um número variável de argumentos.

def meus_numeros(*args):
    for arg in args:
        print(numero)

meus_numeros(10, 2, 3)


# Qualquer número de argumentos de palavra-chave ou nome: **kwargs
# Similar a *args, podemos usar **kwargs para passar tantos argumentos de palavras-chave quantos quisermos, desde que usemos **.

 # novamente, o nome poderia ser qualquer coisa como **numbers, mas **kwargs é uma convenção.

def meus_numeros(**kwargs):
    for chave, valor in kwargs.items():
        print(chave)
        print(valor)


meus_numeros(primeiro_numero=30, segundo_numero=10)


# Outros tipos como argumentos
# Os exemplos anteriores usavam principalmente números, mas você pode passar qualquer tipo como argumento e eles
# serão tratados como tal dentro da função.

# Este exemplo toma como argumentos as cadeias de caracteres.

def meu_esporte_favorito(sport):
    print('Eu gosto de ' + sport)


meu_esporte_favorito('futebol')
meu_esporte_favorito('nadar')


# Esta função toma como argumento uma lista.

def meus_numeros(numeros):
    for numero in numeros:
        print(numero)


meus_numeros([30, 10, 64, 92, 105])




# Escopo
# O local onde uma variável é criada define sua disponibilidade para ser acessada e manipulada pelo resto do código.
# Este é conhecido como escopo.

# Há dois tipos de escopo: local e global.


# Escopo global
# Um escopo global permite que você use a variável em qualquer lugar em seu programa.

# Se sua variável estiver fora de uma função, ela tem escopo global por padrão.

nome = 'Conan'

def imprime_nome():
    print('Meu nome é ' + nome)

imprime_nome()


# Note que a função poderia usar o nome da variável e imprimir 'Meu nome é Conan'.
# Quando você declara uma variável dentro de uma função, ela só existe dentro dessa função e não pode ser acessada de
# fora.


def imprime_nome():
    nome = "Conan"
    print('Meu nome é ' + nome)

imprime_nome()


# O nome da variável foi declarado dentro da função, portanto a saída é a mesma de antes.
# Mas isto vai lançar um erro:

def imprime_nome():
    nome = 'Conan'
    print('Meu nome é ' + nome)


print(nome)

# Tentei imprimir o nome da variável de fora da função, mas o escopo da variável era local e não podia ser 
# encontrado em um escopo global.

# Se você usar o mesmo nome para variáveis dentro e fora de uma função, a função usará a que está dentro de seu escopo.
# Então quando você chama imprime_nome(), o nome='Conan' é usado para imprimir a frase.

# Por outro lado, ao chamar print() fora do escopo da função, nome="Xena" é usado por causa de seu escopo global.

nome = "Xena"


def imprime_nome():
    nome = 'Conan'
    print('Meu nome é ' + nome)


imprime_nome()
print(nome)




# Módulos
# Após algum tempo, seu código começa a ficar mais complexo com muitas funções e variáveis.
# Para facilitar a organização do código, usamos os Módulos.

# Um Módulo bem projetado também tem a vantagem de ser reutilizável, assim você escreve o código uma vez e o reutiliza em todos os lugares.
# Você pode escrever um módulo com todas as operações matemáticas e outras pessoas podem usá-lo.
# E, se você precisar, pode usar os módulos de outra pessoa para simplificar seu código, acelerando seu projeto.
# Em outras linguagens de programação, estas também são chamadas de bibliotecas.


# Usando um módulo
# Para usar um módulo, usamos a palavra-chave importação.
# Como o nome implica, temos que dizer a nosso programa qual módulo importar.
# Depois disso, podemos usar qualquer função disponível nesse módulo.

# Vamos ver um exemplo usando o módulo de matemática.
# Primeiro, vamos ver como ter acesso a uma constante, o número do Euler.

import math

math.e
# 2.718281828459045

# Neste segundo exemplo, vamos usar uma função que calcula a raiz quadrada de um número.
# Também é possível usar a palavra-chave para criar um pseudônimo.

import math as m

m.sqrt(121)
m.sqrt(729)

# Finalmente, usando a palavra-chave from, podemos especificar exatamente o que importar em vez de todo o módulo
# e usar a função diretamente sem o nome do módulo.
# Este exemplo usa a função floor() que retorna o maior número inteiro menor ou igual a um determinado número.

from math import floor

floor(9.8923)


# Criando um módulo
# Agora que sabemos como usar os módulos, vamos ver como criar um.

 # Vai ser um módulo com as operações matemáticas básicas adicionar, subtrair, multiplicar, dividir e vai ser
# chamado de operacoes_basicas.

 # Criar o arquivo basic_operations.py com as quatro funções.

def adicionar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

def multiplicar(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero

def dividir(primeiro_num, segundo_num):
    return primeiro_num / segundo_num

# Depois, basta importar o módulo de operações_básicas e usar as funções.

import operacoes_basicas

operacoes_basicas.adicionar(10, 2)
operacoes_basicas.subtrair(10, 2)
operacoes_basicas.multiplicar(10, 2)
operacoes_basicas.dividir(10, 2)


# se __nome__ == '__main__' #
# Você está no processo de construção de um módulo com as operações matemáticas básicas adicionar, subtrair,
# multiplicar e dividir chamadas operações_base salvas no arquivo basic_operations.py.
# Para garantir que tudo esteja bem, você pode executar alguns testes.

def adicionar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero


def multiplicar(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero


def dividir(primeiro_num, segundo_num):
    return primeiro_num / segundo_num


print(adicionar(10, 2))
print(subtrair(10, 2))
print(multiplicar(10, 2))
print(dividir(10, 2))


# porto@home:~$ python3 basic_operations.py

# A saída para esses testes é o que esperávamos.
# nosso código está certo e pronto para ser compartilhado.
# Vamos importar o novo módulo para rodá-lo no console Python.
# Python 3.6.9 (padrão, Nov 7 2019, 10:44:02)
# [GCC 8.3.0] no linux
# Digite "ajuda", "copyright", "créditos" ou "licença" para mais informações.
# >>> importar operações_básicas

# Quando o módulo é importado, nossos testes são exibidos na tela mesmo que não tenhamos feito nada além de
# importar operações_básicas.

 # Para corrigir isso, usamos if __name__ == '__main__' no arquivo basic_operations.py como este:

def adicionar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero


def multiplicar(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero


def dividir(primeiro_num, segundo_num):
    return primeiro_num / segundo_num

if __name__ == '__main__':
    print(adicionar(10, 2))
    print(subtrair(10, 2))
    print(multiplicar(10, 2))
    print(dividir(10, 2))

# A execução do código diretamente no terminal continuará a exibir os testes. Mas quando você importa como um módulo,
# os testes não aparecerão e você poderá usar as funções da maneira que você pretendia.

# Python 3.6.9 (padrão, Nov 7 2019, 10:44:02)
# [GCC 8.3.0] no linux
# Digite "ajuda", "copyright", "créditos" ou "licença" para mais informações.
# >>> import operacoes_basicas
# >>> operacoes_basicas.multiplicar(10,2)
# 20
# >>>

# Agora que você sabe como usar o if __name__ == '__main__', vamos entender como ele funciona.
# A condição diz quando o interpretador está tratando o código como um módulo ou como um programa em si sendo executado diretamente.
# Python tem esta variável nativa chamada __name__.
# Esta variável representa o nome do módulo que é o nome do arquivo.py.
# Criar um arquivo meu_programa.py com o seguinte e executá-lo.

print(__name__)
# A saída será:


# Isto nos diz que quando um programa é executado diretamente, a variável __name__ é definida como __main__.
# Mas quando é importada como um módulo, o valor de __nome__ é o nome do módulo.

# Python 3.6.9 (padrão, Nov 7 2019, 10:44:02)
# [GCC 8.3.0] no linux
# Tipo "ajuda", "copyright", "créditos" ou "licença" para mais informações.
# >>> import meu_programa
# meu_programa
# >>>

# É assim que o intérprete Python diferencia o comportamento de um módulo importado e de um programa executado
# diretamente no terminal.


# --------------
# Arquivos
# Classes, heranças...
# Exceções


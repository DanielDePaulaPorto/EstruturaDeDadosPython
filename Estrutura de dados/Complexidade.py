
# 1
for i in range(n):
    for j in range(n):
        k = i + j


# A complexidade é O(n^2), pois há um loop for aninhado dentro de outro loop for, que executa n * n vezes.
#---

# 2
for i in range(n):
    for j in range(i):
        k = i + j

# A complexidade é O(n^2), pois há um loop for aninhado dentro de outro loop for, que executa n * n vezes.
#---

# 3
for i in range(n):
    k = 2 + 2

# A complexidade é O(n), pois há apenas um loop for que executa n vezes.
#---

# 4
for i in range(n):
    for j in range(n):
        for k in range(n):
            l = i + j + k

# A complexidade desse código é O(n^3), pois temos três loops aninhados que dependem da entrada n.
#---
# 5
i = n
while i > 0:
    k = i + 1
    i = i // 2

# A complexidade desse código é O(log n). O loop while executa log2(n) vezes, pois a cada iteração o valor de i é dividido por 2.
#---

# 6
def exibir_primeiro_ultimo_elemento(lista):
    if not lista:
        print("A lista está vazia.")
    else:
        print(f"O primeiro elemento é {lista[0]} e o último é {lista[-1]}")

# A complexidade é O(1), pois o tempo de execução não depende do tamanho da lista, mas apenas se a lista está vazia ou não.
#---

# 7
def f(n):
    if n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)

# A complexidade é O(2^n), pois a função recursiva é chamada duas vezes em cada iteração, levando a um número de chamadas de função exponencial: T(n) = T(n-1) + T(n-2) + O(1)
#---

# 8
for i in range(n):
    for j in range(i*i):
        k = i + j

# A complexidade é O(n^3). O primeiro loop for tem complexidade O(n), o segundo loop for tem complexidade O(i^2), que é equivalente a O(n^2) no pior caso.
#---

# 9
for i in range(n):
    for j in range(n):
        if i != j:
            k = i + j

# A complexidade é O(n^2), pois há um loop for aninhado dentro de outro loop for, que executa n * n vezes.
#---

# 10
i = 0
while i < n:
    for j in range(n):
        k = i + j
    i = i + 2

# A complexidade é O(n^2). O loop while executa n/2 vezes, enquanto o loop for executa n vezes em cada iteração, resultando em um total de n^2/2 operações. Como a constante 1/2 é descartada, a complexidade final é O(n^2).
#---

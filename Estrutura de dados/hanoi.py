def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Move {n} de {origem} para {destino}")
    else:
        hanoi(n-1,origem,auxiliar,destino)
        print(f"Move {n} de {origem} para {destino}")
        hanoi(n-1, auxiliar, destino,origem)

ori = "A"
dest = "C"
aux = "B"

num = 5

hanoi(num,ori,dest,aux)

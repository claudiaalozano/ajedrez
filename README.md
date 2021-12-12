# ajedrez
Mi Link de GitHub es: https://github.com/claudiaalozano/ajedrez.git

Mi código es: 
```tablero= [
    ["8" , " " , " " , " ", " ", " " , " " , " " , " "],
    ["7" , " " , " " , " ", " ", " " , " " , " " , " "],
    ["6" , " " , " " , " ", " ", " " , " " , " " , " "],
    ["5" , " " , " " , " ", " ", " " , " " , " " , " "],
    ["4" , " " , " " , " ", " ", " " , " " , " " , " "],
    ["3" , " " , " " , " ", " ", " " , " " , " " , " "],
    ["2" , " " , " " , " ", " ", " " , " " , " " , " "],
    ["1" , " " , " " , " ", " ", " " , " " , " " , " "],
    [" " , "a" , "b" , "c", "d", "e" , "f" , "g" , "h"]
]

#Defino las fichas
#NEGROS
rey_negro= chr(0x265A)
reina_negro=chr(0x265B)
caballo_negro=chr(0x265E)
torre_negra= chr(0x265C)
alfil_negro=chr(0x265D)
peon_negro=chr(0x265F)

#BLANCOS
rey_blanco= chr(0x2654)
reina_banco=chr(0x2655)
caballo_blanco=chr(0x2658)
torre_blanco=chr(0x2656)
alfin_blanco=chr(0x2657)
peon_blanco=chr(0x2659)

#Posición inicial de las fichas
#NEGROS
(tablero[0])[5]= rey_negro
(tablero[0])[4]= reina_negro
(tablero[0])[1]= torre_negra
(tablero[0])[2]= caballo_negro
(tablero[0])[3]= alfil_negro
(tablero[0])[6]= alfil_negro
(tablero[0])[7]= caballo_negro
(tablero[0])[8]= torre_negra
(tablero[1])[1]= peon_negro
(tablero[1])[2]= peon_negro
(tablero[1])[3]= peon_negro
(tablero[1])[4]= peon_negro
(tablero[1])[5]= peon_negro
(tablero[1])[6]= peon_negro
(tablero[1])[7]= peon_negro
(tablero[1])[8]= peon_negro

#BLANCOS
(tablero[7])[1]= torre_blanco
(tablero[7])[2]= caballo_blanco
(tablero[7])[3]= alfin_blanco
(tablero[7])[4]=reina_banco
(tablero[7])[5]= rey_blanco
(tablero[7])[6]= alfin_blanco
(tablero[7])[7]= caballo_blanco
(tablero[7])[8]= torre_blanco
(tablero[6])[1]= peon_blanco
(tablero[6])[2]= peon_blanco
(tablero[6])[3]= peon_blanco
(tablero[6])[4]= peon_blanco
(tablero[6])[5]= peon_blanco
(tablero[6])[6]= peon_blanco
(tablero[6])[7]= peon_blanco
(tablero[6])[8]= peon_blanco

#Movimientos fichas.

print ("Comienza la partida.")
print(tablero)
movimiento = 0
if movimiento == 0:
    while True:
        ficha= print(input("¿Que ficha desea mover?"))
        i=print(input("¿En que fila está la ficha que deseas mover?:"))
        j=print(input("¿En que columna está la ficha que deseas mover?:"))
        (tablero[i])[j] = ficha
        break
    while True:
        movimiento= movimiento + 1
        i_= print(input("¿A qué fila desea moverla?"))
        j_ = print (input("¿A qué columna desa moverla?"))
        (tablero[i_])[j_]= ficha
        (tablero[i])[j]= " "
        print(tablero) ```

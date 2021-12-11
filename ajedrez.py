tablero= [
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
(tablero[5])[0]= rey_negro
(tablero[4])[0]= reina_negro
(tablero[1])[0]= torre_negra
(tablero[2])[0]= caballo_negro
(tablero[3])[0]= alfil_negro
(tablero[6])[0]= alfil_negro
(tablero[7])[0]= caballo_negro
(tablero[8])[0]= torre_negra
(tablero[1])[1]= peon_negro
(tablero[2])[1]= peon_negro
(tablero[3])[1]= peon_negro
(tablero[4])[1]= peon_negro
(tablero[5])[1]= peon_negro
(tablero[6])[1]= peon_negro
(tablero[7])[1]= peon_negro
(tablero[8])[1]= peon_negro

#BLANCOS
(tablero[1])[7]= torre_blanco
(tablero[2])[7]= caballo_blanco
(tablero[3])[7]= alfin_blanco
(tablero[4])[7]=reina_banco
(tablero[5])[7]= rey_blanco
(tablero[6])[7]= alfin_blanco
(tablero[7])[7]= caballo_blanco
(tablero[8])[7]= torre_blanco
(tablero[1])[6]= peon_blanco
(tablero[2])[6]= peon_blanco
(tablero[3])[6]= peon_blanco
(tablero[4])[6]= peon_blanco
(tablero[5])[6]= peon_blanco
(tablero[6])[6]= peon_blanco
(tablero[7])[6]= peon_blanco
(tablero[8])[6]= peon_blanco
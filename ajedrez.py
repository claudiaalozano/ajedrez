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
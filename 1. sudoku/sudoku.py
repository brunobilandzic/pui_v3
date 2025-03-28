
# 	0	1	2	3	4	5	6	7	8	
# 	9	10	11	12	13	14	15	16	17	
# 	18	19	20	21	22	23	24	25	26	

# 	27	28	29	30	31	32	33	34	35	
# 	36	37	38	39	40	41	42	43	44	
# 	45	46	47	48	49	50	51	52	53	

# 	54	55	56	57	58	59	60	61	62	
# 	63	64	65	66	67	68	69	70	71	
# 	72	73	74	75	76	77	78	79	80

class Sudoku:
    
    
    EASYSTR =  "53##7####6##195####98####6#8###6###34##8#3##17###2###6#6####28####419##5####8##79"
    EASY1STR = "53##7####6##1#5####98####6#8###6###34##8#3##17###2###6#6####28####419##5####8##79"
    EASY2STR = "###6###########5#1369#8#4#######68#####13###94#5##9#########3####6##7###1##34####"
    MEDSTR =   "#7###9#4#2#314###6#######3#8######7##1#562#9##5######4#4#######7###248#1#6#7###2#"
    HARDSTR =  "###7#####1###########43#2##########6###5#9#########418####81#####2####5##4####3##"

    # svakom polju je pridruzen skup polja koja ne smiju imati isti broj 
    # ključevi ovog objekta su indeksi polja, a vrijednosti su skupovi indeksa polja
    # koji ne smiju biti isti kao to polje

    #praktički, ovo je jednako kao GROUPS samo što je u obliku rječnika

    CONSTRAINS = {
            0 : {1, 2, 3, 4, 5, 6, 7, 8, 9, 72, 10, 11, 18, 19, 20, 27, 36, 45, 54, 63} ,
            1 : {0, 2, 3, 4, 5, 6, 7, 8, 64, 10, 73, 9, 11, 18, 19, 20, 28, 37, 46, 55} ,
            2 : {0, 1, 3, 4, 5, 6, 7, 8, 65, 74, 11, 9, 10, 18, 19, 20, 29, 38, 47, 56} ,
            3 : {0, 1, 2, 4, 5, 6, 7, 8, 66, 75, 12, 13, 14, 21, 22, 23, 30, 39, 48, 57} ,
            4 : {0, 1, 2, 3, 5, 6, 7, 8, 67, 76, 13, 12, 14, 21, 22, 23, 31, 40, 49, 58} ,
            5 : {0, 1, 2, 3, 4, 6, 7, 8, 68, 12, 77, 14, 13, 21, 22, 23, 32, 41, 50, 59} ,
            6 : {0, 1, 2, 3, 4, 5, 7, 8, 69, 78, 15, 16, 17, 24, 25, 26, 33, 42, 51, 60} ,
            7 : {0, 1, 2, 3, 4, 5, 6, 8, 70, 79, 16, 15, 17, 24, 25, 26, 34, 43, 52, 61} ,
            8 : {0, 1, 2, 3, 4, 5, 6, 7, 71, 15, 80, 17, 16, 24, 25, 26, 35, 44, 53, 62} ,
            9 : {0, 1, 2, 72, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 36, 45, 54, 63} ,
            10 : {64, 1, 0, 2, 9, 11, 12, 13, 14, 15, 16, 17, 73, 19, 18, 20, 28, 37, 46, 55} ,
            11 : {0, 65, 2, 1, 9, 10, 12, 13, 14, 15, 16, 17, 74, 18, 20, 19, 29, 38, 47, 56} ,
            12 : {66, 3, 4, 5, 9, 10, 11, 13, 14, 15, 16, 17, 75, 21, 22, 23, 30, 39, 48, 57} ,
            13 : {67, 4, 3, 5, 9, 10, 11, 12, 14, 15, 16, 17, 76, 21, 22, 23, 31, 40, 49, 58} ,
            14 : {3, 68, 5, 4, 9, 10, 11, 12, 13, 15, 16, 17, 77, 21, 22, 23, 32, 41, 50, 59} ,
            15 : {69, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 78, 24, 25, 26, 33, 42, 51, 60} ,
            16 : {70, 7, 6, 9, 10, 11, 12, 13, 14, 15, 17, 79, 24, 25, 26, 34, 8, 43, 52, 61} ,
            17 : {6, 71, 8, 9, 10, 11, 12, 13, 14, 15, 16, 80, 24, 25, 26, 35, 7, 44, 53, 62} ,
            18 : {0, 1, 2, 72, 9, 10, 11, 19, 20, 21, 22, 23, 24, 25, 26, 27, 36, 45, 54, 63} ,
            19 : {64, 1, 0, 2, 73, 10, 9, 11, 18, 20, 21, 22, 23, 24, 25, 26, 28, 37, 46, 55} ,
            20 : {0, 65, 2, 1, 9, 74, 11, 10, 18, 19, 21, 22, 23, 24, 25, 26, 29, 38, 47, 56} ,
            21 : {66, 3, 4, 5, 75, 12, 13, 14, 18, 19, 20, 22, 23, 24, 25, 26, 30, 39, 48, 57} ,
            22 : {67, 4, 3, 5, 76, 13, 12, 14, 18, 19, 20, 21, 23, 24, 25, 26, 31, 40, 49, 58} ,
            23 : {3, 68, 5, 4, 12, 77, 14, 13, 18, 19, 20, 21, 22, 24, 25, 26, 32, 41, 50, 59} ,
            24 : {69, 6, 7, 8, 78, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 33, 42, 51, 60} ,
            25 : {70, 7, 6, 8, 79, 16, 15, 18, 19, 20, 21, 22, 23, 24, 26, 17, 34, 43, 52, 61} ,
            26 : {6, 71, 8, 7, 15, 80, 17, 18, 19, 20, 21, 22, 23, 24, 25, 16, 35, 44, 53, 62} ,
            27 : {0, 72, 9, 18, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 54, 63} ,
            28 : {64, 1, 73, 10, 19, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 55} ,
            29 : {65, 2, 74, 11, 20, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 56} ,
            30 : {66, 3, 75, 12, 21, 27, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 48, 49, 50, 57} ,
            31 : {67, 4, 76, 13, 22, 27, 28, 29, 30, 32, 33, 34, 35, 39, 40, 41, 48, 49, 50, 58} ,
            32 : {68, 5, 77, 14, 23, 27, 28, 29, 30, 31, 33, 34, 35, 39, 40, 41, 48, 49, 50, 59} ,
            33 : {69, 6, 78, 15, 24, 27, 28, 29, 30, 31, 32, 34, 35, 42, 43, 44, 51, 52, 53, 60} ,
            34 : {70, 7, 79, 16, 25, 27, 28, 29, 30, 31, 32, 33, 35, 42, 43, 44, 51, 52, 53, 61} ,
            35 : {71, 8, 80, 17, 26, 27, 28, 29, 30, 31, 32, 33, 34, 42, 43, 44, 51, 52, 53, 62} ,
            36 : {0, 72, 9, 18, 27, 28, 29, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 54, 63} ,
            37 : {64, 1, 73, 10, 19, 27, 28, 29, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 55} ,
            38 : {65, 2, 74, 11, 20, 27, 28, 29, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 56} ,
            39 : {66, 3, 75, 12, 21, 30, 31, 32, 36, 37, 38, 40, 41, 42, 43, 44, 48, 49, 50, 57} ,
            40 : {67, 4, 76, 13, 22, 30, 31, 32, 36, 37, 38, 39, 41, 42, 43, 44, 48, 49, 50, 58} ,
            41 : {68, 5, 77, 14, 23, 30, 31, 32, 36, 37, 38, 39, 40, 42, 43, 44, 48, 49, 50, 59} ,
            42 : {69, 6, 78, 15, 24, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 51, 52, 53, 60} ,
            43 : {70, 7, 79, 16, 25, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 51, 52, 53, 61} ,
            44 : {71, 8, 80, 17, 26, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 51, 52, 53, 62} ,
            45 : {0, 72, 9, 18, 27, 28, 29, 36, 37, 38, 46, 47, 48, 49, 50, 51, 52, 53, 54, 63} ,
            46 : {64, 1, 73, 10, 19, 27, 28, 29, 36, 37, 38, 45, 47, 48, 49, 50, 51, 52, 53, 55} ,
            47 : {65, 2, 74, 11, 20, 27, 28, 29, 36, 37, 38, 45, 46, 48, 49, 50, 51, 52, 53, 56} ,
            48 : {66, 3, 75, 12, 21, 30, 31, 32, 39, 40, 41, 45, 46, 47, 49, 50, 51, 52, 53, 57} ,
            49 : {67, 4, 76, 13, 22, 30, 31, 32, 39, 40, 41, 45, 46, 47, 48, 50, 51, 52, 53, 58} ,
            50 : {68, 5, 77, 14, 23, 30, 31, 32, 39, 40, 41, 45, 46, 47, 48, 49, 51, 52, 53, 59} ,
            51 : {69, 6, 78, 15, 24, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 60} ,
            52 : {70, 7, 79, 16, 25, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 61} ,
            53 : {71, 8, 80, 17, 26, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 62} ,
            54 : {0, 64, 65, 72, 9, 73, 74, 18, 27, 36, 45, 55, 56, 57, 58, 59, 60, 61, 62, 63} ,
            55 : {64, 1, 65, 72, 73, 10, 74, 19, 28, 37, 46, 54, 56, 57, 58, 59, 60, 61, 62, 63} ,
            56 : {64, 65, 2, 72, 73, 74, 11, 20, 29, 38, 47, 54, 55, 57, 58, 59, 60, 61, 62, 63} ,
            57 : {66, 3, 67, 68, 75, 12, 76, 77, 21, 30, 39, 48, 54, 55, 56, 58, 59, 60, 61, 62} ,
            58 : {66, 67, 4, 68, 75, 76, 13, 77, 22, 31, 40, 49, 54, 55, 56, 57, 59, 60, 61, 62} ,
            59 : {66, 67, 68, 5, 75, 76, 77, 14, 23, 32, 41, 50, 54, 55, 56, 57, 58, 60, 61, 62} ,
            60 : {69, 6, 70, 71, 78, 15, 79, 80, 24, 33, 42, 51, 54, 55, 56, 57, 58, 59, 61, 62} ,
            61 : {69, 70, 7, 71, 78, 79, 16, 80, 25, 34, 43, 52, 54, 55, 56, 57, 58, 59, 60, 62} ,
            62 : {69, 70, 71, 8, 78, 79, 80, 17, 26, 35, 44, 53, 54, 55, 56, 57, 58, 59, 60, 61} ,
            63 : {64, 65, 66, 67, 68, 69, 70, 71, 0, 9, 72, 73, 74, 18, 27, 36, 45, 54, 55, 56} ,
            64 : {65, 66, 67, 68, 69, 70, 71, 1, 73, 10, 72, 74, 19, 28, 37, 46, 54, 55, 56, 63} ,
            65 : {64, 66, 67, 68, 69, 70, 71, 2, 72, 74, 11, 73, 20, 29, 38, 47, 54, 55, 56, 63} ,
            66 : {64, 65, 67, 68, 69, 70, 71, 3, 75, 12, 76, 77, 21, 30, 39, 48, 57, 58, 59, 63} ,
            67 : {64, 65, 66, 68, 69, 70, 71, 4, 75, 76, 13, 77, 22, 31, 40, 49, 57, 58, 59, 63} ,
            68 : {64, 65, 66, 67, 69, 70, 71, 5, 75, 76, 77, 14, 23, 32, 41, 50, 57, 58, 59, 63} ,
            69 : {64, 65, 66, 67, 68, 70, 71, 6, 78, 15, 79, 80, 24, 33, 42, 51, 60, 61, 62, 63} ,
            70 : {64, 65, 66, 67, 68, 69, 71, 7, 78, 79, 16, 80, 25, 34, 43, 52, 60, 61, 62, 63} ,
            71 : {64, 65, 66, 67, 68, 69, 70, 8, 78, 79, 80, 17, 26, 35, 44, 53, 60, 61, 62, 63} ,
            72 : {0, 64, 65, 73, 74, 75, 76, 77, 78, 79, 80, 9, 18, 27, 36, 45, 54, 55, 56, 63} ,
            73 : {64, 1, 65, 72, 74, 75, 76, 77, 78, 79, 80, 10, 19, 28, 37, 46, 54, 55, 56, 63} ,
            74 : {64, 65, 2, 72, 73, 75, 76, 77, 78, 79, 80, 11, 20, 29, 38, 47, 54, 55, 56, 63} ,
            75 : {66, 3, 67, 68, 72, 73, 74, 76, 77, 78, 79, 80, 12, 21, 30, 39, 48, 57, 58, 59} ,
            76 : {66, 67, 4, 68, 72, 73, 74, 75, 77, 78, 79, 80, 13, 22, 31, 40, 49, 57, 58, 59} ,
            77 : {66, 67, 68, 5, 72, 73, 74, 75, 76, 78, 79, 80, 14, 23, 32, 41, 50, 57, 58, 59} ,
            78 : {69, 6, 70, 72, 73, 74, 75, 76, 77, 79, 80, 15, 24, 33, 71, 42, 51, 60, 61, 62} ,
            79 : {69, 70, 7, 72, 73, 74, 75, 76, 77, 78, 80, 16, 25, 34, 71, 43, 52, 60, 61, 62} ,
            80 : {69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 8, 17, 26, 35, 44, 53, 60, 61, 62} ,
        }

    # sve grupe ovisnih polja (redovi, stupci i podpodjela)
    # ovisna polja u obliku liste listi
    # podijeljena je u 3 kategorije listi: redovi, stupci i kvadrati
    GROUPS = [
        [ 	0,	1,	2,	3,	4,	5,	6,	7,	8,	],
        [	9,	10,	11,	12,	13,	14,	15,	16,	17,	],
        [ 	18,	19,	20,	21,	22,	23,	24,	25,	26,	],        
        [ 	27,	28,	29,	30,	31,	32,	33,	34,	35,	],
        [ 	36,	37,	38,	39,	40,	41,	42,	43,	44,	],
        [ 	45,	46,	47,	48,	49,	50,	51,	52,	53,	],
        [ 	54,	55,	56,	57,	58,	59,	60,	61,	62,	],
        [ 	63,	64,	65,	66,	67,	68,	69,	70,	71,	],
        [ 	72,	73,	74,	75,	76,	77,	78,	79,	80, ],

        [0, 9, 18, 27, 36, 45, 54, 63, 72],
        [1, 10, 19, 28, 37, 46, 55, 64, 73],
        [2, 11, 20, 29, 38, 47, 56, 65, 74],
        [3, 12, 21, 30, 39, 48, 57, 66, 75],
        [4, 13, 22, 31, 40, 49, 58, 67, 76],
        [5, 14, 23, 32, 41, 50, 59, 68, 77],
        [6, 15, 24, 33, 42, 51, 60, 69, 78],
        [7, 16, 25, 34, 43, 52, 61, 70, 79],
        [8, 17, 26, 35, 44, 53, 62, 71, 80],
        
        [0, 1, 2, 9, 10, 11, 18, 19, 20],
        [27, 28, 29, 36, 37, 38, 45, 46, 47],
        [54, 55, 56, 63, 64, 65, 72, 73, 74],
        [3, 4, 5, 12, 13, 14, 21, 22, 23],
        [30, 31, 32, 39, 40, 41, 48, 49, 50],
        [57, 58, 59, 66, 67, 68, 75, 76, 77],
        [6, 7, 8, 15, 16, 17, 24, 25, 26],
        [33, 34, 35, 42, 43, 44, 51, 52, 53],
        [60, 61, 62, 69, 70, 71, 78, 79, 80],
        ]
                
    def __init__(self, inistr=EASYSTR):
        # iniciramo ploču, # umjesto '0' jer je lakše za čitanje
        # pa sada pretvaramo u int jer nam je lakše raditi s brojevima
        self._board = [ 0 if  c == "#" else int(c) for c in inistr  ]
        # iniciramo opcije za svako polje koje je u state._board
        # znamo da ima 81 polje, pa idemo od 0 do 81
        # svaki indeks postaje ključ u rječniku, a vrijednost je skup brojeva koji su mogući za to polje
        self._options = { c: self.cell_options(c) for c in range(81) if self._board[c] == 0 }
        self._stack = []
    
    def __str__(self):
        s = ""
        s += "-" + "--" * 12 + "\n"
        for y in range(9):
            s += "| "
            for x in range(9):
                s += "# " if self._board[9*y+x] == 0 else str(self._board[9*y+x]) + " "
                if (x+1) % 3 == 0:
                    s += "| "
            s += "\n"
            if (y+1) % 3 == 0:
                s += "-" + "--" * 12 + "\n"
        return s
    
    def solved(self):
        # ako više nema opcija, onda je ploča riješena
        # opcije za neko polje izbacimo ako upišemo broj u to polje jer nam više ne trebaju
        return len(self._options) == 0
    
    # ispunjava liste potencijalnih brojeva za zadano polje prema stanju grupe
    # odbire one grupe koje sadrže zadano polje (različiti redovi, stupci i kvadrati)
    # za svako polje u svakoj pojedinoj grupi, vraća broj koji je upisan u tom indeksu
    def cell_options(self, cell):
        # nalaženje relevantnih grupa za polje cell
        groups = [ g for g in self.GROUPS if cell in g ]
        # nalaženje svih brojeva koji su već upisani u polja relevantnih grupama
        filled = set( self._board[c] for g in groups for c in g )
        # vraćanje mogućih opcija za polje cell
        return set(range(1, 10)) - filled
    
    # kreira listu svih mogucih akcija (polje, broj)
    # pretvara riječnik self._options u listu (key, value[i]) za svaki ključ i svaki value[i]
    # generirat ce se dakle value[i] parova za svaki ključ c
    def actions(self):
        actions = []
        for c in self._options:
            actions += [ (c, b) for b in self._options[c] ]
        
        return actions

    # kreira listu svih mogućih akcija za polje koje ima najmanje opcija
    # to nam treba za brže rješavanje jer je vjerojatnije da će se u polju s manje opcija naći ispravan broj
    def actions_min_cell(self):
        min_actions = [ 0 ] * 10
        for c in self._options:
            actions = [ (c, b) for b in self._options[c] ]
            if len(actions) < len(min_actions):
                min_actions = actions
        return min_actions

    # upisuje broj u polje i azurira sve opcije drugih polja
    # stog nam sluzi da bi mogli brzo ponistiti akciju 
    def do_action(self, action):
        # akcija se sastoji od para (indeks, broj)
        cell, number = action
        # upis broja u polje
        self._board[cell] = number
        # uklanjanje polja iz opcija jer je broj upisan u to polje
        # metoda .pop() vraća vrijednost za ključ i briše ga iz rječnika
        # tako da taj indeks više nije upisan u riječniku self._options
        cell_options = self._options.pop(cell)

        restore_constrained = []
        # idemo po svim poljima
        for c in self.CONSTRAINS[cell]:
            if c in self._options and number in self._options[c]:
                # ako je polje u riječniku opcija (još nije u njega upisan broj) te ako je broj koji upisujemo u polje c u opcijama za to polje
                # makni broj number iz opcija polja c jer je vec upisan u polje cell
                self._options[c].remove(number)
                # kako bi mogli ponistiti akciju, spremamo polje c iz čijih opcija smo uklonili broj number
                # kako bi ga kasnije mogli vratiti u opcije za to polje c
                restore_constrained.append(c)
        # trebamo sve opcije za polje c koje smo sada izbrisali jer smo upisali broj number u polje cell
        #  i trebamo listu brojeva c kojima smo iz opcija izbacili broj number
        #  kako bi ga kasnije mogli vratiti u opcije za to polje c        
        self._stack.append((cell_options, restore_constrained))
    
    # poništava akciju i azurira opcije drugih polja
    def undo_action(self, action):
        cell, number = action
        # upisujemo 0 u polje jer poništavamo akciju
        self._board[cell] = 0
        # vraćamo opcije za polje cell koje smo izbrisali jer smo upisali broj number u to polje
        
        cell_options, restore_constrained = self._stack.pop()
        self._options[cell] = cell_options
        # restore_constrained je lista polja c iz čijih opcija smo izbacili broj number
        for c in restore_constrained:
            # vraćamo broj number u opcije za polje c
            self._options[c].add(number)


from sys import platform
version = "Beta Multi-Edition 1.1.0"
direction = "up"
lang = "fr"
mapx, mapy, x, y, ax, ay, aax, aay= 1, 1, 64 , 16, 64 , 15, 64, 14
apparenceplayernb, apparencetnb = 1, 2
listofapparence = ["?","☺",":","_","*","%","="]
apparenceplayer, apparencet = "☺", ":"
fullblock, InteractBlock = "a1!", "!"
GAME = True
F3Mode = False
IsCoteeGauche = True
OldCoteeIsGauche = True
if platform[:3] == 'win':
    sysexp = "Win"
    try:
        with open('winkeysave.txt', 'rb') as f:
            allkeylist = f.readline()
        allkeylistafter = allkeylist.split(b'\xb6')
        up = allkeylistafter[0].decode()
        down = allkeylistafter[1].decode()
        right = allkeylistafter[2].decode()
        left= allkeylistafter[3].decode()
        escap = allkeylistafter[4].decode()
        enter = allkeylistafter[5].decode()
        delete = allkeylistafter[6].decode()
        f3 = allkeylistafter[7].decode()

        
    except:
        up = 'up'
        down = 'down'
        right = 'right'
        left= 'left'
        escap = '\x1b'
        enter = '\r'
        delete = '\x08'
        f3 = 'f3'
        
elif platform[:3] == 'lin' or platform[:3] == 'dar':
    if platform[:3] == 'lin': sysexp = "Lin"
    else: sysexp = "Mac"
    try:
        with open('linkeysave.txt', 'rb') as f:
            allkeylist = f.readline()
        allkeylistafter = allkeylist.split(b'\xb6')
        up = allkeylistafter[0].decode()
        down = allkeylistafter[1].decode()
        right = allkeylistafter[2].decode()
        left= allkeylistafter[3].decode()
        escap = allkeylistafter[4].decode()
        enter = allkeylistafter[5].decode()
        delete = allkeylistafter[6].decode()
        f3 = allkeylistafter[7].decode()
    except:
        up = '\x1b[A'
        down = '\x1b[B'
        right = '\x1b[C'
        left= '\x1b[D'
        escap = '\x1b\x1b'
        enter = '\r'
        delete = '\x7f'
        f3 = '\x1bO'


def cls():
    print("\033[1;1H\033[2J")


Updates = \
"1.0.0:\n\
\t- Point de spawn\n\
\t- Mouvements\n\
\t- Colisions avec full-block\n\
1.0.1:\n\
\t- Touche Ctrl+C\n\
\t- Menu Escap\n\
1.0.2:\n\
\t- Separation entre varfile et le reste\n\
\t- Ajout des Updates\n\
\t- Ajout d\'une deuxième map et déplacement entre eux\n\
\t- Ajout de posibles couleurs\n\
\t- Ajout d\'une trainé derière\n\
1.0.3:\n\
\t- Amilioration du menu echap\n\
\t- Amilioration des apparences\n\
\t- Personalisations des personnages\n\
1.0.4:\n\
\t- Ajout de la bordure option\n\
\t- Optimisation du code\n\
\t- Ajout de couleurs dans le jeu\n\
1.0.5:\n\
\t- Ajout de la posibilité d\'Interaction avec le décors\n\
\t- Affichage des options du menu option\n\
1.0.5:\n\
\t- Sortie de la Linux Edition(Avec un peu de bug)\n\
\t- Plus besoin de WConio2 pour la WinEd\n\
\t- Ajout des options et asignement des touches\n\
\n\
\n\
Ce qui reste à faire:\n\
\t- Ajout de plusieurs maps\n\
\t- Inventaire avec money\n\
\t- Resize obligatoires\n\
\t- Gestion Anti Ereurr\n\
\t- Corrections des fautes d\'orthographe\n\
\t- Ajouts des Credits\n\
\t- Mode multioueurs\n\
\t- Multiplatform avec la meme aplication\n\
\t- Nom et Chat(Avec potentielements des commandes)\n\
\t- Interaction avec le décors\n\
\t- Anti cheat (Avec un hebergement full serveur)\n\
\t- Sauvegardes\n\
\t- Multilanguage (fr,en,esp...)\n\
\t- Ajout d\'argent virtuels\n\
\t- F3 = Debug Mode\n\
\t- Fenètre de chargements au début\n\
\t- Aceuil du debut\n\
\t- Comptes pour avoir plusieurs personages\n\
\t- \n\
\t- \n\
\t- XXX"

def StyleofTyping(EnterSelectOption, nboptions):
    a = EnterSelectOption%nboptions
    print((lambda: "\033[13;50H \033[31m ╔═╗╔═╗╔╦╗╦╔═╗╔╗╦╔═╗  \033[0m" if a==0 else "\033[13;50H ╔═╗╔═╗╔╦╗╦╔═╗╔╗╦╔═╗   ")())
    print((lambda: "\033[14;50H \033[31m ║ ║╠═╝ ║ ║║ ║║║║╚═╗  \033[0m" if a==0 else "\033[14;50H ║ ║╠═╝ ║ ║║ ║║║║╚═╗   ")())
    print((lambda: "\033[15;50H \033[31m ╚═╝╩   ╩ ╩╚═╝╩╚╝╚═╝  \033[0m" if a==0 else "\033[15;50H ╚═╝╩   ╩ ╩╚═╝╩╚╝╚═╝   ")())
    print((lambda: "\033[16;50H \033[31m ╔═╗╔═╗╦ ╦╔═╗╔═╗  \033[0m" if a==1 else "\033[16;50H ╔═╗╔═╗╦ ╦╔═╗╔═╗    ")())
    print((lambda: "\033[17;50H \033[31m ╚═╗╠═╣║ ║╠╣ ╚═╗  \033[0m" if a==1 else "\033[17;50H ╚═╗╠═╣║ ║╠╣ ╚═╗    ")())
    print((lambda: "\033[18;50H \033[31m ╚═╝╩ ╩╚╦╝╚═╝╚═╝  \033[0m" if a==1 else "\033[18;50H ╚═╝╩ ╩╚╦╝╚═╝╚═╝    ")())
    print((lambda: "\033[19;50H \033[31m ╔╦╗╔═╗╔╗╦╦ ╦  \033[0m" if a==2 else "\033[19;50H ╔╦╗╔═╗╔╗╦╦ ╦    ")())
    print((lambda: "\033[20;50H \033[31m ║╩║╠╣ ║║║║ ║  \033[0m" if a==2 else "\033[20;50H ║╩║╠╣ ║║║║ ║    ")())
    print((lambda: "\033[21;50H \033[31m ╩ ╩╚═╝╩╚╝╚═╝  \033[0m" if a==2 else "\033[21;50H ╩ ╩╚═╝╩╚╝╚═╝    ")())
    print((lambda: "\033[22;50H \033[31m ╔═╗╦ ╦╦╔╦╗  \033[0m" if a==3 else "\033[22;50H ╔═╗╦ ╦╦╔╦╗    ")())
    print((lambda: "\033[23;50H \033[31m ║╦║║ ║║ ║   \033[0m" if a==3 else "\033[23;50H ║╦║║ ║║ ║     ")())
    print((lambda: "\033[24;50H \033[31m ╚╬╝╚═╝╩ ╩   \033[0m" if a==3 else "\033[24;50H ╚╬╝╚═╝╩ ╩     ")())

def OptionofTyping(OptionSelectOption, nbptionoptions):
    a = OptionSelectOption%nbptionoptions
    print((lambda: "\033[8;7H \033[31m Controls  \033[0m" if a==0 else "\033[8;7H Controls   ")())
    print((lambda: "\033[9;7H \033[31m music  \033[0m" if a==1 else "\033[9;7H music   ")())
    print((lambda: "\033[10;7H \033[31m lang  \033[0m" if a==2 else "\033[10;7H lang   ")())
    print((lambda: "\033[11;7H \033[31m Settings  \033[0m" if a==3 else "\033[11;7H Settings    ")())
    print((lambda: "\033[12;7H \033[31m Visuel  \033[0m" if a==4 else "\033[12;7H Visuel    ")())
    print((lambda: "\033[13;7H \033[31m Textures  \033[0m" if a==5 else "\033[13;7H Textures   ")())
    print((lambda: "\033[14;7H \033[31m Comptes  \033[0m" if a==6 else "\033[14;7H Comptes    ")())
    print((lambda: "\033[15;7H \033[31m Updates  \033[0m" if a==7 else "\033[15;7H Updates    ")())
    print((lambda: "\033[16;7H \033[31m Styles  \033[0m" if a==8 else "\033[16;7H Styles    ")())
    print((lambda: "\033[17;7H \033[31m Return Bug  \033[0m" if a==9 else "\033[17;7H Return Bug    ")())
    print((lambda: "\033[18;7H \033[31m Debug   \033[0m" if a==10 else "\033[18;7H Debug     ")())

ARKANTitleStyle = \
"\033[31m\033[7;47H█████  █████  █   █  █████  ██  █\n"+\
        "\033[8;47H█   █  █   █  █ ██   █   █  █ █ █\n"+\
        "\033[9;47H█████  ████   ██     █████  █ █ █\n"+\
       "\033[10;47H█   █  █ █    █ ██   █   █  █ █ █\n"+\
       "\033[11;47H█   █  █  ██  █   █  █   █  █  ██\n\
\033[12;47H" + version+ "\033[12;77H"+sysexp+"\033[0m" 

def AffichefenetreOptions():
    print("\
\033[3;5H┌─────────────────────┐\
\033[4;5H│ ╔═╗╔═╗╔╦╗╦╔═╗╔╗╦╔═╗ │\
\033[5;5H│ ║ ║╠═╝ ║ ║║ ║║║║╚═╗ │\
\033[6;5H│ ╚═╝╩   ╩ ╩╚═╝╩╚╝╚═╝ │\
\033[7;5H├─────────────────────┴" + "─"*94 + "┐")
    for i in range(20):
        print("\033["+str(8+i)+";5H│"+ " "*116 + "│")
    print("\033[28;5H"+"└"+ "─"*116 + "┘")


def AffichefenetreOptionsContols():
    print("\
\033[3;5H┌──────────────────────────┐\
\033[4;5H│ ╔═╗╔═╗╔╗╦╔╦╗╔═╗╔═╗╦  ╔═╗ │\
\033[5;5H│ ║  ║ ║║║║ ║ ╠╦╝║ ║║  ╚═╗ │\
\033[6;5H│ ╚═╝╚═╝╩╚╝ ╩ ╩╚ ╚═╝╚═╝╚═╝ │\
\033[7;5H├──────────────────────────┴" + "─"*89 + "┐")
    for i in range(20):
        print("\033["+str(8+i)+";5H│"+ " "*116 + "│")
    print("\033[28;5H"+"└"+ "─"*116 + "┘")


def PrintEcrandacceuil():
    print("\033[103m\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
\033[32m██████                                                                                                                          \n\
██████████                                                                                                                      \n\
████████████                                                                                                                    \n\
█████████████                                                                                                                   \n\
██████████████                                                                                                                  \n\
██████████████                                                                                                                  \n\
\033[44m███████████████                                                                                                                 \n\
████████████████                                                                                                                \n\
██████████████████                                                                                                              \n\
█████████████████████                                                                                                           \n\
████████████████████████                                                                                                        \n\
████████████████████████████████                                                                                                \n\
█████████████████████████████████████████████                                                                                   \n\
████████████████████████████████████████████████████████████                                                                    \n\
██████████████████████████████████████████████████████████████████████████████                                                  \n\
████████████████████████████████████████████████████████████████████████████████████████████████                                \n\
██████████████████████████████████████████████████████████████████████████████████████████████████████████                      \n\
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████             \n\
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████      \n\
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████   \n\
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████\n\
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████\n\
\033[42m\033[31mhttps://github.com/ARKANYOTA/ArkanYotaGameCmd\033[32m██████████████████████████████████████████████████████████████\033[42m\033[31mCreated by Arkan Yota\033[0m", sep="", end="")
    print("\033[103m", ARKANTitleStyle,"\033[0m", sep="")

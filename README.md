
#import AcciArt

# print AcciArt.carro
# print AcciArt.gato

Tama=(5,4)

A = 1
J = 11
Q = 12
K = 13

Donde = (5,4)

tesoros=[(1,3),(3,2),(1,1),]
camino=[]
# camino=[7,9,A,9,A,8,A,7,A,7,Q]
dire=0
presenta=0
def cuadricula(x=Tama[0],y=Tama[1],a=11,b=5,c=' '):
    global Donde,dire,A,J,Q,K
    Inicio = (x,y)
    Donde = (x,y)

    ue = '|'+a*' '
    ul = '|'+a*'-'

    L = (a//2)*' '+x*ul+'|\n'
    E = (a//2)*' '+x*ue+'|\n'

    ux = '|'+(a//2)*' '+c+(a//2)*' '
    P = (a//2)*' '+x*ux+'|\n'

    G = L+(b//2)*E+P+(b//2)*E
    GRL = list(y*G+L)

    def Dist(v, vv=1):
        if type(v)==int:
            equis=v
            ye=vv
        else:
            equis=v[0]
            ye=v[1]
        return (ye-1)*(b+1)*len(L)+((b//2+1)*len(L)) + equis*len(ue)-1
        # return (b - b // 2) * ((2 * ye - 1) * len(L) + equis * (a // 2 + 1)) - 1

    GRL[Dist(Donde) - 2] = 'I'
    if presenta == 1:
        GRL[Dist(Donde) - 2] = 'I'
        GRL[Dist(Donde)-1] = 'n'
        GRL[Dist(Donde)] = 'i'
        GRL[Dist(Donde)+1] = 'c'

    def Coord(v,vv=0):
        if type(v) == int:
            equis = v
            ye = vv
        else:
            equis = v[0]
            ye = v[1]
        return ye*len(L)+2*equis*(a//2+1)-1


    for d in tesoros:
        i=d[0]
        j=d[1]
        GRL[Dist(i,j)]='.'

    for c in camino:

        if c in [7,8,9,10,11,12]:
            ver = ['7','8','9','D', 'J', 'Q']
            pintos=['<','^','>','v']
            brincos = 1 if dire in [0,2] else len(L)
            espa = (a+1) if dire in [0,2] else (b+1)
            deta = 1 if dire in [0,2] else 0
            sent= -1 if dire >1 else 1
            sent = sent  if c < 10 else -sent
            cc = c - 6 if c < 10 else c-9
            for i in range((cc)*espa-3*deta):
                cordist=Dist(Donde) - brincos*i*sent
                GRL[cordist-2*sent*deta] = pintos[dire] if GRL[cordist-2*sent*deta] not in ver else GRL[cordist-2*sent*deta]
            GRL[Dist(Donde)]=ver[c-7]
            if dire in [0, 2]:
                Donde=(Donde[0]-sent*cc,Donde[1])
            else:
                Donde = (Donde[0], Donde[1] - sent * cc)

        elif c in [1,2,3,4,5,6]:
            ver=['','A','2','3','4','5','6']
            GRL[Dist(Donde)-2] = ver[c]
            GRL[Dist(Donde)-1] = ','
            dire=(dire+c)%4
        GRL[Dist(Donde)]='O'

    GR=''.join(GRL)
    return GR

class Alumno():
    animales=[]
    comidas=[]
    juegos=[]
    personal=''

def entronombre(vv):
    vvv=Nombre.title()
    Nomv=vvv
    # print vv,vvv,Nomv
    if vvv in LAlumnos:
        Nomv=vvv
    elif vvv not in reconocibles3:
        NomV='Foraneo'
    elif vvv == 'Fernanda':
        Nomv='Yazmin'
    try:
        luga=LAlumnos.index(Nomv)
    except:
        print('Repite tu nombre si estas en la siguiente lista copialo identico')
        for i in LAlumnos:
            print i


    if Nomv in LAlumnos[0:-1]:
        print('\n--TE RECONOCI--\n')
        print('Hola '+Nomv.upper())
        medicen=raw_input('\n'+ALpersonal[luga]+'\n..>')
        if medicen in LRafirmacioes:
            print('Que bueno '+ Nomv +' te has gando una pista\nSi conoces el codigo secreto\n'
                              'te puedo dibujar un mapa\n...')
            confirmo=1
        elif medicen in LRnegaciones:
            print('Que lastima')
        else:
            print('Vuelve a escribir tu nombre')

LRPNocomprendo=['No entiendo la pabra']
PNC=0
LRPNocomprendo2=['\nestoy programada para reconocer solo algunas palabras y codigos.\nIntenta decirme algo mas.']
PNC2=0
LRPEdu=['\nEscribe despues de la linea punteda y\nluego presiona la tecla -Enter-,-Intro-, o -Return-\n..>','...']
PED=0
LRPinsit=['BIENVENIDO','Hola Escribe','Escribe algo','Algo que comentar?','']
PIS=0
LRPpistas=['--Me gusta que me saluden--','--Me gusta que me hablen en codigo--',
           'alguna vez haz escondido un tesoro??', 'El Misterio tiene que ver con codigos']
PIST=0
LRPalent=['--Escribiste algo que tiene que ver con mi MISTERIO--']
PAL=0

LRPpresenta=['\n\n  ---ESTE ES UN JUEGO DE MISTERIO PARA TI (EXPERIMENTA)---\n']
PPS=0

LRPpistin=[('--EL NUMERO ',' ME PARECE ESPECIAL--\n') ,
           ('--Ese numero tambien es especial ',' para ti es especial??--\n'),
           ('--Ese numero tambien es especial ',' para ti es especial??--\n'),
           ('--Ese numero tambien es especial ',' para ti es especial??--\n'),
           ('--Ese numero tambien es especial ',' para ti es especial??--\n'),
           ('--Ese numero tambien es especial ',' para ti es especial?--\n'),
           ('--Si hablamos de mapas y cartas en este salon el ',' es especial--\n'),
           ('--ME GUSTA QUE ME SALUDEN el numero ',' es especial si lo sigues de una coma y otro numero especial--\n')]
pistin=0

LRanimales=['caballo','perro','gato','cacatua','panda','perico loco','lobo']
LRclaves=['9,7,A,9,A,9,7,A,8,A,9,A,7,A,9','[9,7,A,9,A,9,7,A,8,A,9,A,7,A,9]','integritat','mixi','integri',
          'mapa','tesoro','']
LRsaludos=['hola','Hola''alo','que hubo','buenas','que tal','hi','chocala','buenas','ondas']
LRsalidas=['salir','salte','quit','exit','aburrido','adios','chao','sal']
LRafirmacioes=['si','Si','SI','S','s','sip','Sip']
LRnegaciones=['No','no','NO','nop','nel','nelfas','N']
LRcalculos=['suma','sumale','resta','restale','multiplica','multiplicalo',
    '+','-','*','/','mas','menos','por','entre','divide','dividelo','elevalo']
Hs=0

LAlumnos=['Alvaro','Majo','Dario','Alexis','Atreyu','Oscar','Yazmin','Foraneo']
LAnimales=[['borrego cimarron', 'venado', 'obeja'],['guacamaya', 'lobo'],
         ['puma', 'tigre', 'lobo', 'chita'], ['leon', 'puma', 'tiburon', 'tigre'],
         ['megalodon', 'quetzalcoatl'],['serpientes', 'camaleon'],
         ['gato', 'perro', 'lobo', 'axolotl', 'tiburon'],[]]
LComidas=[['sushi', 'hamburguesa', 'papas a la francesa'],['espaguetti fumata', 'milanesa', 'sopa maruchan'],
        ['pizza', 'haburguesa', 'papas fritas', 'nuguets de pollo'],['torta de milanesa', 'hot cakes', 'pizza'],
        ['hamburguesa', 'pizza', 'hot dog'],['enchiladas verdes', 'hamburguesa'],
        ['dulces', 'paleta lucas con chilito'],[]]
LGrados=[]
LEdad=[]

ALpersonal=['Tu eres el Alvaro que tiene una gran coleccion de piedres preciosas??',
            'Tu eres la Maria Jose a la que le gusta leer libros\ny consigue pastas de chocolate delicioso\nque hacen oler todo el salon ?? ',
            'Tu eres el Dario que inventa robots como Mixi ?? ',
            'Tu eres el Alexis al que le gusta divertise en Facebook ??',
            'Tu eres el Atreyu que tiene un reloj al que se le insertan discos?',
            'Tu eres el Oscar que una vez volo un dron tan alto que perdio la senial\ny luego se estampo contra el suelo ??',
            'Tu eres la Yazmin que una vez etubo a punto de caer a una cascada\npor meter su moto al rio en el rancho\nde tus abuelos ??']

reconocibles=[1,2,3,4,5,6,7,8,9,10,11,12,13]
reconocibles1=['A','J','Q','K',',']
reconocibles2=[str(i) for i in reconocibles]
reconocibles3=['Alvaro','Maria Jose','Dario','Alexis','Atreyu','Oscar','Yazmin',
               'Majo','Fernanda','Mixi','Maxi','Oskar','Albaro']
reconocibles3=reconocibles3+[i.lower() for i in reconocibles3]
reconocibles3=reconocibles3+[i.upper() for i in reconocibles3]
TR=reconocibles1+reconocibles2+reconocibles3+[str(i) for i in reconocibles]

medijeronNC=[]
medijeronNB=[]
medijeronNS=[]
medijeronCV=[]

medicen=''
Nombre='desconocido'
lemovio=0
mapo=0
animalf=''
comidaf=''
juegof=''

while medicen != 'salexqu0':
    if PPS==0:
        print(LRPpresenta[PPS])
        print('Si escribes cosas en el teclado y despues precionas ENTER podras investigar.'
              '\nExperimenta escribiendo.\n\n  --DEVES AVERIGUAR PARA QUE TE PUEDO SERVIR--\n')

        medicen=raw_input('...')
        if len(medicen) > 0:
            print('\n--MUY BIEN--\nEscuche que dijiste:\n" '+medicen+' "')
        else:
            medicen = raw_input(LRPEdu[PED])
            PED = -1
        PPS=1

    else:
        # prog=PIST%len(LRPinsit)
        # medicen = raw_input(LRPinsit[prog]+'\n'+'...')
        medicen = raw_input('\n...')



    if medicen in LRclaves:
        medijeronCV.append(medicen)
        print ('\n'+'Algo deves de saber')
        medicen = raw_input('..>')

    elif medicen in LRsaludos:
        # PIST=-1

        print ('\n'+'Hola yo soy una maqina...\ncomo una caja de musica o un reloj de cuerda\n'
               'o un carro de control remoto o una motocicleta(que no deves meter al agua)\n'
               'o una vercion de Mixi, o un dron(que no puede volar demaciado alto)\n'
               'o una maquina para hacer tortillas.\n\n  """Estoy programada y guardo un misterio""".\n\n'
               'TU, COMO TE LLAMAS?\n')

        # medicen=raw_input(LRPEdu[PED])
        # PED = -1
        medicen=raw_input('..>')
        medijeronNB.append(medicen)
        Nombre =''+medijeronNB[-1]
        medicen = raw_input('Te entendi bien? Tu nombre es - "'+Nombre.upper()+'" -??\n...>')

        if medicen not in LRafirmacioes:
            if medicen in LRnegaciones:
                medicen=raw_input('Ok, no entendi bien: Repitelo')
                medijeronNB.append(medicen)
                Nombre = '' + medijeronNB[-1]
                medicen = raw_input('Te entendi bien? Tu nombre es - "' + Nombre.upper() + '" -??\n...>')
                if medicen in LRafirmacioes:
                    print ('Hola '+ Nombre.upper())
            else:
                medijeronNB.append(medicen)
                Nombre = '' + medijeronNB[-1]
                medicen=raw_input('Tu nambres es -"'+Nombre.upper()+'"-??'+'\n...>')
                if medicen in LRafirmacioes:
                    print ('Hola ' + Nombre.upper())
                    entronombre(medicen)

        else:
            print ('Hola ' + Nombre.upper())
            entronombre(medicen)

    elif medicen in reconocibles3:
        medijeronNB.append(medicen)
        Nombre = '' + medijeronNB[-1]
        medicen=raw_input('\n --" '+ medicen.upper() + ' "--  Ese es tu nombre??\n..>')
        if medicen in LRafirmacioes:
            print ('Hola ' + Nombre.upper())
            entronombre(medicen)


    elif medicen in LRsalidas:
        pregu=raw_input('Quieres salirte del programa?\nSi si: Escribe Si\n...>')
        if pregu in LRafirmacioes:
            print ('ADIOS')
            medicen='salexqu0'

    elif (medicen+'z')[0] in [str(i[0]) for i in TR]:
        try:
            propu=eval(medicen)
            if type(propu)==tuple and propu[0] < 14 and propu[1] < 14:
                propu=list(propu)
                camino = propu
                print('MUY BIEN')
                print('Eso yo lo entiendo como un mapa')
                print ('escrito con el codigo SECRETO de la clase de\nExperimentos tecnologicos de Integritat')
                if mapo==1:
                    Donde=Tama
                    dire=0
                    print(cuadricula())
                else:
                    medicen=raw_input('Si me sabes decir la carta que te hace avansar 2 pasos te dibujo un mapa\n...')
                    if medicen=='8':
                        mapo=1
                        camino=[]
                        presenta=1
                        print(cuadricula())
                        print('Este es un mapa del tapete')
                        print('\n\n--SIGUE INTENTENDO--\n\n')
                        presenta=0
                    else:
                        print('\nLo siento esa no es la carta\n')
            elif type(propu) == int:
                if propu in reconocibles:
                    print (LRPpistin[pistin%len(LRPpistin)][0]+str(propu)+LRPpistin[pistin%len(LRPpistin)][1])
                    pistin+=1
                    medicen = raw_input('Que otro numero podria ser especial??\n...')
                    if ',' in medicen:
                        print('MUY MUY BIEN\nSigue probando con comas')
                    if medicen in [str(i) for i in reconocibles]:
                        print('Muy BIEN ese tambien sigue probando')
                        medicen = raw_input('Que otro numero podria ser especial??\n...')
                        pistin=len(LRPpistin)-1
                        if ',' in medicen:
                            print ('Estas Muy Muy cerca\n --Sigue probando con comas--')

                else:
                    medicen=raw_input('Eso es un numero. Yo soy buena con eso.\nQue hago con el '+medicen+' ??\n'+medicen+'...')

                if medicen in LRcalculos:
                    medicen=raw_input('Con que otro numero?\n..>')
                    try:
                        resu= propu * eval(medicen)
                        print ('Lo multilique ' + str(propu) + '*' + medicen + '=' + str(resu))
                        print ('Tal vez no entendi intenta hablarme en codigo')
                    except:
                        print ('No pude. intenta hablarme en codigo')
                elif medicen in ['abansa','avansa','avanza','abanza','jira','gira','salta','brinca']:
                    print('Te acercas a descubrir el codigo que se hablar\n una pista \n-- utiliza comas --')
                else:
                    print ('Te acuerdas que te dije que Guardo un misterio\n a lo mejor tu lo conoces\n tiene que ver con numeros, cartas y mapas')

            if mapo == 54:
                print cuadricula()
        except:
            # print('--ALGO DEVES SABER--')
            print ('\nReconoci la primera letra que escribiste Pero:')
            print (LRPNocomprendo[PNC]+'--" '+medicen+' "--'+LRPNocomprendo2[PNC2])
    elif medicen == '9,7,A,9,A,9,7,A,8,A,9,A,7,A,9':
        camino=medicen
        cuadricula()
    elif '(' in medicen:
        try:
            print (eval(medicen))
        except:
            pass

    else:
        PIST+=1
        medijeronNC.append(medicen)
        print('\n'+LRPNocomprendo[PNC]+'--" '+medicen+' "--'+LRPNocomprendo2[PNC2])


# print ('Hola juvensuelo...\nPara que esto funcione tienes que esribir devajo de este Texto...\n'
#        'en el cuedrito que parpadea')
# primer=raw_input()
#
# segundo=raw_input('Yo no entiendo '+ primer + 'solo entiendo coasas para las que fuy programada')
#
#
# a=str(raw_input('Como te llamas\n'))
#
# print('Hola '+a)
#
# comida= 'Pizza'
#
# print('Hay quien dice que te gusta comer '+ comida)
#
# g=(raw_input('Es Verdad?\n'))
#
# passs= raw_input('clave')
#
#
#
# print (cuadricula())



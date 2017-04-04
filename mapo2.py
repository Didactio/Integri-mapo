#!/usr/bin/python
# coding=utf-8
#todo impotar para guardar archivoss
# todo tiempo
# print AcciArt.gato
import AcciArt

from random import randint

# ------ inicia ------- Dibujador de tapetes ---------

TamanoTapete = (5,4)
TamanoCuadrosNON = (11,5)

VInic = (TamanoTapete[0],TamanoTapete[1])
VDonde = VInic
VDirec = 0

Vpresenta = 0
Vsiempreinic = 1
Lllego = []
Lpaso = []
Lbrinco = []
vtesoros=[(1,3),(3,2),(1,1)]
vcvtesoros=['01gato79','02pollo22','03carro44']
vcamino=[]

LtesAcum=['Ninguno']

def letanu(vvv):
    sinlet = vvv.replace('A','1').replace('J','11').replace('Q','12').replace('K','13')
    sinlet = sinlet.replace('a','1').replace('j','11').replace('q','12').replace('k','13')
    return sinlet

# vcamino=[7,9,A,9,A,8,A,7,A,7,Q]
def cuadricula(cam='loquito',x=TamanoTapete[0],y=TamanoTapete[1],aa=TamanoCuadrosNON[0],bb=TamanoCuadrosNON[1],c=' '):
    global VDonde,VDirec,VInic,Lllego,Lpaso,Lbrinco,vcamino

    if Vsiempreinic == 1:
        VInic = (x,y)
        VDonde = VInic
        VDirec = 0
        Lllego = []
        Lpaso = []
        Lbrinco = []
    huboencu = 0

    ue = '|' + aa * ' '
    ul = '|' + aa * '-'
    L = (aa//2)*' '+x*ul+'|\n'
    E = (aa//2)*' '+x*ue+'|\n'

    ux = '|'+(aa//2)*' '+c+(aa//2)*' '
    P = (aa//2)*' '+x*ux+'|\n'

    G = L+(bb//2)*E+P+(bb//2)*E

    GRL = list(y*G+L)

    def Dist(v, vv=1):
        if type(v)==int:
            equis=v
            ye=vv
        else:
            equis=v[0]
            ye=v[1]
        if 0 < (ye-1)*(bb+1)*len(L)+((bb//2+1)*len(L)) + equis*len(ue)-1 < len(GRL):
            return (ye-1)*(bb+1)*len(L)+((bb//2+1)*len(L)) + equis*len(ue)-1
        else:
            return 0


    def Coord(v,vv=0):
        if type(v) == int:
            equis = v
            ye = vv
        else:
            equis = v[0]
            ye = v[1]
        return ye*len(L)+2*equis*(aa//2+1)-1

    GRL[Dist(VDonde) - 3] = '<'
    GRL[Dist(VDonde) - 2] = 'I'
    if Vpresenta == 1:
        GRL[Dist(VDonde) - 3] = '<'
        GRL[Dist(VDonde) - 2] = 'I'
        GRL[Dist(VDonde)-1] = 'n'
        GRL[Dist(VDonde)] = 'i'
        GRL[Dist(VDonde)+1] = 'c'

    for d in vtesoros:
        i=d[0]
        j=d[1]
        GRL[Dist(i,j)]='.'

    if cam != 'loquito':
        vcamino=cam
        if type(vcamino) in (tuple,list):
            vcamino=vcamino
        else:
            try:
                # vcamino=letanu(vcamino)
                A,a,J,j,Q,q,K,k=1,1,11,11,12,12,13,13
                vcamino=eval(cam)
            except:
                vcamino=[]

    vvcamino = vcamino

    if type(vvcamino) == str:
        vvcamino=eval(letanu(vvcamino))

    for c in vvcamino:

        if c in [7,8,9,10,11,12]:
            ver = ['7','8','9','D','J','Q','K','A','1','2','3','4','5','6']
            pintos=['<','^','>','v']
            brincos = 1 if VDirec in [0,2] else len(L)
            espa = (aa+1) if VDirec in [0,2] else (bb+1)
            deta = 1 if VDirec in [0,2] else 0
            sent= -1 if VDirec >1 else 1
            sent = sent  if c < 10 else -sent
            cc = c - 6 if c < 10 else c-9
            for i in range((cc)*espa-3*deta):
                cordist=Dist(VDonde) - brincos*i*sent
                try:
                    GRL[cordist-2*sent*deta] = pintos[VDirec] if GRL[cordist-2*sent*deta] not in ver else GRL[cordist-2*sent*deta]
                except:
                    loco=345
            GRL[Dist(VDonde)]=ver[c-7]
            if VDirec in [0, 2]:
                VDonde=(VDonde[0]-sent*cc,VDonde[1])
            else:
                VDonde = (VDonde[0], VDonde[1] - sent * cc)

        elif c in [1,2,3,4,5,6]:
            ver=['','A','2','3','4','5','6','K','~']
            GRL[Dist(VDonde)-3] = '~' if GRL[Dist(VDonde)-2]  in ver else ' '
            GRL[Dist(VDonde)-2] = ver[c] if GRL[Dist(VDonde)-2] not in ver else ''+ver[c]
            GRL[Dist(VDonde)-1] = ','
            VDirec=(VDirec+c)%4
        elif c == 13:
            GRL[Dist(VDonde)+2] = 'K'
            GRL[Dist(VDonde)+1] = ','

        GRL[Dist(VDonde)]='O'

    info = ' nada mas'

    for i in vtesoros:
        if GRL[Dist(i)] in ('O','7','8','9','D','J','Q') or GRL[Dist(i)+2] == 'K':
            Lllego.append(i)
            LtesAcum.append(vcvtesoros[vtesoros.index(i)]) if vcvtesoros[vtesoros.index(i)] not in LtesAcum else None
            if 'Ninguno' in LtesAcum:
                LtesAcum.remove('Ninguno')
            huboencu=1
        if GRL[Dist(i)+2] == 'K':
            Lbrinco.append(i)
        if GRL[Dist(i)] in ['<','^','>','v']:
            Lpaso.append(i)

    if GRL[Dist(VDonde)+aa//2+1+len(L)] != '|' or GRL[Dist(VDonde)-aa//2-1+len(L)] != '|' :
        Lllego = []
        Lpaso = []
        Lbrinco = []
        print '\n--TE CAISTE--'
        info = '\n--TE CAISTE--'

    if len(Lllego)>0:
        print 'Agarraste Tesoros--> ',Lllego
        info = '\n--AGARRASTE TESOROS en--->>> ' + str(Lllego)+'\n--hay nuevos tesoros en tu maletin\n si quieres verlos escribe: mimaletin() --'
        if all(i in Lllego for i in vtesoros):
            info=info+'\n\n¡¡¡Premio adicional por\ntomar todos los tesoros en un solo recorrido!!!--'
    info='\nRecorriste el tapete con la clave -'+ str(vcamino) +'- y'+ info

    if Vpresenta==1:
        info=''

    if huboencu==1:
        enconteso('4')
    GR=''.join(GRL)+info

    return GR
#------termina------ ------------------------------------------- Dibujador de tapetes---------------termina
# print cuadricula('7,K,9,4,A,7,7,7,5,9,7,4,4,4,a,8,a,7,7,a,7')
# print(cuadricula((9,7,1,7,13,8,13,1,8,1,7)))
# print(cuadricula((9,7,1,7,8,13,1,8,9,7)))
# print(cuadricula((9,1,9,9)))
# print(cuadricula((9,3,7)))
# print(cuadricula((9,9)))
# print(cuadricula((9,8)))
# print(cuadricula((9,7,1,8)))


#----------inicia ----- ----------------------------------------- Funciones del juego --------------- inicia

TenemosNomConf=0

def entronombre(vv):
    global TenemosNomConf,medicen

    vvv=vv.title()

    if any(i in LAlumnos for i in vvv.split(' ')):
        for i in vvv.split(' '):
            if i in LAlumnos:
                Nomv=i
    elif any(i not in reconocibles3 for i in vvv.split(' ')):
        Nomv='Foraneo'
    elif any(i in ['Maria Jose','Maria','Jose'] for i in vvv.split(' ')):
        Nomv= 'Majo'
    try:
        luga=LAlumnos.index(Nomv)
    except:
        print('Repite tu nombre; si estas en la siguiente lista copialo identico')
        for i in LAlumnos:
            print i
        Nomv=raw_input('\n.....>')
        try:
            luga = LAlumnos.index(Nomv)
        except:
            print 'No entendi intenta escribir tu nombre de nuevo'

    if Nomv in LAlumnos[0:-1]:
        print('\n--HOLA '+Nomv.upper()+' --')
        print('Te reconoci\n')
        medicen=raw_input(ALpersonal[luga]+'\n\n..(s/n)..>')
        if medicen in LRafirmacioes:
            if MCUP==1:
                print ('\n¡Que Bueno jugar de nuevo contigo ' +Nomv+ '!\n'
                       'Supongo que la ves pasada que jugaste\n'
                       'lograste que te dibujara un mapa\n'
                       'Para volvrte a abrir la puerta escribe una clave con comas')
            else:
                print('Que bueno '+ Nomv +' te has gando una pista\nSi conoces el codigo secreto\n'
                              'te puedo dibujar un mapa\n...')
            TenemosNomConf=Nomv
        elif medicen in LRnegaciones:
            print('\nQue lastima')
        else:
            print('\nVuelve aa escribir tu nombre')
    else:
        print('Creo que no te conosco')
    medicen='pasale'


def sumanombre(v,vvv=0):
    # latmin=lowercase[:14]+u'ñ'+lowercase[14:] if u'ñ' not in lowercase else lowercase
    # latmay=uppercase[:14]+u'Ñ'+uppercase[14:] if u'Ñ' not in uppercase else uppercase
    latmin = u'abcdefghijklmnñopqrstuvwxyz'
    latmay = u'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    dijiti = u'0123456789'
    toditi = latmay+latmin+dijiti
    valaores = []
    valoress = []
    desple=[]
    desplee=[]
    for i in v:
        valaores.append(latmin.find(i) + 1) if i in latmin else None
        valaores.append(latmay.find(i) + 1) if i in latmay else None
        # valaores.append(0) if i == ' ' else None
        valaores.append(dijiti.find(i)) if i in dijiti else None
        # print valaores
        # valaores.append(0) if i not in toditi+[' '] else None
        desple.append(i+'='+str(valaores[-1]) if i in toditi else i+'=0')
    if ' ' in v:
        conti = 0
        for i in v.split(' '):
            vv = 0
            for n in i:
                vv = vv + valaores[conti]
                conti = conti + 1
            valoress.append(vv)
            desplee.append(i + '=' + str(valoress[-1]))
    if ',' in v:
        tuple = ''.join([latmay[i - 1] for i in list(eval(v))])
    elif ' ' in v:
        tuple = str(sum(valaores)),str(valoress), str(valaores)
    else:
        tuple = (str(sum(valaores)), str(valaores))

    if vvv!=0:
        return sum(valaores)
    else:
        return ('\n'+', '.join(desple)+'\n'+', '.join(desplee)+'\n'+'\nLa suma de todas las letras en\n'
                '--" '+v+' "-- Es = '+tuple[0])
SN=sumanombre

def enconteso(vv):
    print (AcciArt.gato2)
# todo bonitas claves
Lclavpresen=['UNA MERA CALAVE','DOS MERAS CLAVES','Tres MERAS CLAVES']
def mimaletin(vv=0):
    if vv==0:
        info='Los tesoros que haz recojido son:\n'
        for i in LtesAcum:
            info = info+'\n'+i
        if 'Ninguno' not in LtesAcum:
            info=info+'\n\nCada tesoro es una clave que te mostrara algo especial.\nSi quieres verlo escribe por ejemplo: mimaletin('+LtesAcum[0]+')'
    else:
        if vv in LtesAcum:
            arto = vv[2:-2]
            arto2 = Lclavpresen[vcvtesoros.index(vv)]
            try:
                info = eval('AcciArt.'+arto)+'\n'+arto2
            except:
                info = arto2
        else:
            info='No tienes ese tesoro'

    return info


#----------terminan----- --------------  funciones del juago------------------------------------- termina


#-------inicia----------------------------------------- VARIABLES PERSONALES AD OC-----------------------inicia

LAlumnos=['Alvaro','Majo','Dario','Alexis','Atreyu','Oscar','Yazmin','Foraneo']
LAlumnosNM=[SN(i,1) for i in LAlumnos]
LOPCIAlumnos=['Alvaro','Maria Jose','mari jo','maria','jose','Dario','Alexis','Atreyu','Oscar','Yazmin','yasmin',
               'Majo','Fernanda','Mixi','Maxi','Oskar','Albaro']
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
ALpersonal=['¿Tu eres el Alvaro que tiene una gran coleccion de piedres preciosas??',
            'Tu eres la Maria Jose a la que le gusta leer libros\ny consigue pastas de chocolate delicioso\nque hacen oler todo el salon ?? ',
            'Tu eres el Dario que inventa robots como Mixi ?? ',
            'Tu eres el Alexis al que le gusta divertise en Facebook ??',
            'Tu eres el Atreyu que tiene un reloj al que se le insertan discos?',
            '¿Tu eres el Oscar que una vez voló un dron tan alto que perdio la senial\ny luego se estampo contra el suelo ??',
            'Tu eres la Yazmin que una vez etubo a punto de caer a una cascada\npor meter su moto al rio en el rancho\nde tus abuelos ??']

LRanimales=['caballo','perro','gato','cacatua','panda','perico loco','lobo','axolotl']

#-------termina--------- Variables PER AD OC----------------------------------------------------termina


#----------inicia-----    -----   ------------------  Variables de ESRITOS deljuego---------------- ----inicia

LRPpresentacion=[('\n'+'Hola yo soy una maqina...\ncomo una caja de musica o un reloj de cuerda\n'
       'o un carro de control remoto o una motocicleta(que no deves meter al agua)\n'
       'o una vercion de Mixi, o un dron(que no puede volar demaciado alto)\n'
       'o una maquina para hacer tortillas.\n\n  """Estoy programada y guardo un misterio"""\n\n'),
        ('Yo te conté que era una maquina cuando nos conocimos... \n--Te menti--\n'
         'En realidad la maquina' 'es la computadora en la que estas escribiendo.\n\n'
        '--Yo soy un programa--\n ¿Sabes que es un programa?\n'
         'Si en lugar de la computadora fuera la caja de' 'musica;\n'
         'el programa seria el barril que gira; el que tenia puntitos \n'
         'Cualquier cosa que hayas hecho o hagas en una computadora\n'
         'tiene un programa que alguien escribio en codigo')]
LRPPRES=0

LRPNocomprendo=['No entiendo la pabra','No entiendo la frase']
PNC=0
LRPNocomprendo2=['\nEstoy programada para reconocer solo algunas palabras y codigos.\nIntenta decirme algo mas.',
                 '\nEs muy larga, mi programa solo entiende algunas palabras y codigos;\nprueva de palabra en palabra:\n'
                 'Intenta decirme algo mas']
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
#--------termina--------------------------------------------------------------ESCRITOS---termina


#-----------inicia-------------------------------------- Vriables de RECONOCIMIENTO--------------inicia

reconocibles=[1,2,3,4,5,6,7,8,9,10,11,12,13]
reconocibles1=['A','J','Q','K',',']
reconocibles1=reconocibles1+[i.lower() for i in reconocibles1]
reconocibles2=[str(i) for i in reconocibles]

reconocibles3=LOPCIAlumnos
reconocibles3=reconocibles3+[i.lower() for i in reconocibles3]
reconocibles3=reconocibles3+[i.upper() for i in reconocibles3]
reconocibles3=reconocibles3+[i.title() for i in reconocibles3]

TR=reconocibles1+reconocibles2+reconocibles3+[str(i) for i in reconocibles]
TRanimal= LRanimales[:]
for i in LAnimales:
    for ii in i:
        TRanimal.append(ii)

LRsalidas=['salir','salte','quit','exit','aburrido','adios','chao','sal']
LRsaludos=['hola','Hola''alo','que hubo','buenas','que tal','hi','chocala','buenas','ondas']
LRafirmacioes=['si','Si','SI','S','s','sip','Sip']
LRnegaciones=['No','no','NO','nop','nel','nelfas','N','n','Nop']

LRclaves=['9,7,A,9,A,9,7,A,8,A,9,A,7,A,9','[9,7,A,9,A,9,7,A,8,A,9,A,7,A,9]','integritat','mixi','integri',
          'mapa','tesoro','tesoros','loro loco','clave']
LRcalculos=['suma','sumale','resta','restale','multiplica','multiplicalo',
            '+','-','*','/','mas','menos','por','entre','divide','dividelo','elevalo']
#----------termina---------variab de RECONOCIMIENTO----------------------------------------------termina


#-------inicia-------------------------------------------PROGRMA del JUEGO------------------------------inicia

medijeronNC=[]
medijeronNB=[]
medijeronNS=[]
medijeronCV=[]

medicen=''
VNombre='desconocido'
lemovio=0
mapo=0
MCUP=0

while medicen != 'salexqu0':
    if PPS==0:
        print(LRPpresenta[PPS])
        print('Si escribes cosas en el teclado y despues precionas ENTER podras investigar.'
              '\nExperimenta escribiendo.\n\n  --DEVES AVERIGUAR PARA QUE TE PUEDO SERVIR--\n\n'
              '(si ya has jugado conmigo esribe si o s)\n')

        medicen=raw_input('...')
        if medicen in ('s','si'):
            MCUP=1
            medicen = raw_input('\nHola. Asi que ya has estado por aqui\n'
                       '¿Quien Eres?''\n\n..?..>')

        if MCUP == 0:
            if len(medicen) > 0:
                print('\n--MUY BIEN YA ME ESCRIBISTE ALGO--\nEscuche que dijiste:\n" '+medicen+' "')
            else:
                medicen = raw_input(LRPEdu[PED])
                PED = -1
        PPS=1

    else:
        medicen = raw_input('\n...')

    if '(' in medicen:
        print ('Escribiste una funcion que reconosco:')
        try:
            if any(i in medicen for i in ['sumanombre','SN']) and all(medicen.count(ii)<2 for ii in ['"',"'"]):
                medicen=medicen.replace("'","")
                medicen=medicen.replace('"','')
                medicen=medicen.replace("(","('")
                medicen=medicen.replace(")","')")
            elif any(i in medicen for i in ['mimaletin']) and medicen[medicen.index('(')+1] != ')':
                medicen = medicen.replace("'", "")
                medicen = medicen.replace('"', '')
                medicen = medicen.replace("(", "('")
                medicen = medicen.replace(")", "')")
            print '--'+medicen+'--'
            print 'El resultado es:'
            print (eval(medicen,globals()))
            medicen='pasale'
        except:
            medicen = 'pasale'
            pass
    elif any(i in LRclaves for i in medicen.split(' ')):
        medijeronCV.append(medicen)

        if medicen not in LRclaves:
            Lrecon=[]
            if medicen.count(' ') > 3:
                print ('La frace que escribiste es muy larga\n'
                       'y mi programacion es muy basica\n'
                       'solo entiendo algunas palabras clave\n'
                       'y algunos codigos secretos')

            for i in medicen.split(' '):
                if i in LRclaves:
                    Lrecon.append(i.upper())
            print ('\n'+'--Algo deves de saber--')
            if len(Lrecon)>1:
                pref = 'Las palabras --'
                pos = '-- me "suenan" '
            else:
                pref = 'La palabra --'
                pos = '-- me "suena" '

            print(pref+ ', '.join(Lrecon) + pos+'\nPrueba escribiendo de una palabra en una palabra\n\n'
                                                '\n --Sigue investigando--\n')
            medicen='pasale'
        else:
            print ('--ESA PALABRA LA RECONOSCO--')

    elif medicen in LRsaludos:
        # PIST=-1

        print (LRPpresentacion[LRPPRES])

        if TenemosNomConf == 0:
            print('TU, COMO TE LLAMAS?\n')

            medicen=raw_input('..?..>')
            medijeronNB.append(medicen)
            VNombre = medijeronNB[-1]
            medicen = raw_input('Te entendi bien? Tu nombre es - "'+VNombre.upper()+'" -??\n..(s/n)..>')

            if medicen not in LRafirmacioes:
                if medicen in LRnegaciones:
                    medicen=raw_input('Ok, no entendi bien: Repitelo')
                    medijeronNB.append(medicen)
                    VNombre = medijeronNB[-1]
                    medicen = raw_input('Te entendi bien? Tu nombre es - "' + VNombre.upper() + '" -??\n...>')
                    if medicen in LRafirmacioes:
                        print ('Hola '+ VNombre.upper())
                        entronombre(VNombre)
                else:
                    medijeronNB.append(medicen)
                    VNombre = medijeronNB[-1]
                    medicen=raw_input('Tu nambres es -"'+VNombre.upper()+'"-??'+'\n...>')
                    if medicen in LRafirmacioes:
                        print ('Hola ' + VNombre.upper())
                        entronombre(VNombre)

            else:
                print ('Hola ' + VNombre.upper())
                entronombre(VNombre)
        else:
            print('\n\n Ya me entere que tu eres '+TenemosNomConf+' sabes jugar a los tesoros?' )

    if any(i in reconocibles3 for i in medicen.split(' ')):
        for i in medicen.split(' '):
            if i in reconocibles3:
                medijeronNB.append(i)
        VNombre = medijeronNB[-1]
        if TenemosNomConf == 0:
            medicen=raw_input('\n  " '+ VNombre.upper() + ' " Ese es tu nombre??\n\n...(s/n)...>')
        elif TenemosNomConf in [medicen,medicen.lower(),medicen.upper(),medicen.title()]:
            print ('Me dijiste que ese era tu nomre'+' Hola '+TenemosNomConf)
        else:
            medicen = raw_input('\n  " ' + VNombre.upper() + ' " Esta en la clase de Experimentos tecnologicos'
                                'tu eres '+ VNombre.upper() +'??\n\n...(s/n)...>')
        if medicen in LRafirmacioes:
            print ('Hola ' + VNombre.upper())
            if TenemosNomConf == 0:
                entronombre(VNombre)
            else:
                print ('Pense que eras ' + TenemosNomConf+' eso me habias dicho')
                medicen=raw_input('entoces eres '+VNombre.upper()+' ??\n\n...(s/n)...>')
                if medicen in LRafirmacioes:
                    TenemosNomConf = 0
                    entronombre(VNombre)
                elif medicen in LRnegaciones:
                    print (VNombre.upper()+' es buena onda')

        elif medicen in LRnegaciones:
            if TenemosNomConf == 0:
                print ('Cual es tu nombre??')


    elif medicen in LRsalidas:
        pregu=raw_input('Quieres salirte del programa?\nSi si: Escribe Si\n...>')
        if pregu in LRafirmacioes:
            print ('ADIOS')
            medicen='salexqu0'

    elif (medicen+'z')[0] in [str(i[0]) for i in TR]:
        try:
            propu=eval(letanu(medicen))
            if type(propu)==tuple and propu[0] < 14 and propu[1] < 14:
                propu=list(propu)
                vcamino = medicen
                print('MUY BIEN')
                print('Eso yo lo entiendo como un mapa')
                print ('escrito con el codigo SECRETO de la clase de\nExperimentos tecnologicos de Integritat')
                if mapo==1:
                    VDonde=TamanoTapete
                    VDirec=0
                    print(cuadricula())
                else:
                    medicen=raw_input('\n--Si me SABES decir el NUMERO de la carta que te hace AVANZAR 2 pasos\nte dibujo un MAPA--\n\n...?..> ')
                    if medicen in ('8','7,7'):
                        mapo=1
                        vcamino=[]
                        Vpresenta=1
                        print(cuadricula())
                        print('Este es un mapa del tapete')
                        print('\n\n--HAZ ABIERTO UNA PUERTA --\n')
                        print('Tu habias escrito el CODIGO SECRETO -- '+str(propu)[1:-1]+' --\n'
                              'y como supsite que el - 8 - te hace avanzar 2 pasos\n'
                              'Ahora yo puedo hacer cosas mas DIVERTIDAS con los CODIGOS SECRETOS\n'
                              '\n--SIGUE INVESTIGANDO--\n''escribe otro codgo y veras lo que pasa\n')
                        Vpresenta=0
                    else:
                        print('\nLo siento esa no es la carta\n')
            elif type(propu) == int:
                if propu in reconocibles:
                    print (LRPpistin[pistin%len(LRPpistin)][0]+str(propu)+LRPpistin[pistin%len(LRPpistin)][1])
                    pistin+=1
                    medicen = raw_input('Que otro numero podria ser especial??\n...')
                    if ',' in medicen:
                        print('MUY MUY BIEN\nSigue probando con comas')
                        if all(i in reconocibles1+reconocibles2 for i in medicen):
                            if mapo == 0:
                                medicen2 = raw_input('\n--Si me SABES decir el NUMERO de la carta que te hace AVANZAR 2 pasos\nte dibujo un MAPA--\n\n...?..> ')
                                if medicen2 in ('8', '7,7'):
                                    mapo = 1
                                    vcamino = []
                                    Vpresenta = 1
                                    print(cuadricula())
                                    print('Este es un mapa del tapete')
                                    print('\n\n--HAZ ABIERTO UNA PUERTA --\n')
                                    print('Tu habias escrito el CODIGO SECRETO -- ' + str(propu)[1:-1] + ' --\n'
                                         'y como supsite que el - 8 - te hace avanzar 2 pasos\n'
                                         'Ahora yo puedo hacer cosas mas DIVERTIDAS con los CODIGOS SECRETOS\n'
                                         '\n--SIGUE INVESTIGANDO--\n''escribe otro codgo y veras lo que pasa\n')
                                    Vpresenta = 0
                            elif mapo ==1:
                                mapo=1
                                vcamino=medicen
                                print(cuadricula())
                        else:
                            print ('Estas Muy Muy cerca\n --Sigue probando con comas--')

                    if medicen in [i for i in reconocibles1+reconocibles2]:
                        print('Muy BIEN ese tambien sigue probando')
                        medicen = raw_input('Que otro numero podria ser especial??\n...')
                        pistin=len(LRPpistin)-1
                        if ',' in medicen:
                            if all(i in reconocibles1 + reconocibles2 for i in medicen):
                                if mapo == 0:
                                    medicen2 = raw_input('\n--Si me SABES decir el NUMERO de la carta que te hace AVANZAR 2 pasos\nte dibujo un MAPA--\n\n...?..> ')
                                    if medicen2 in ('8', '7,7'):
                                        mapo = 1
                                        vcamino = []
                                        Vpresenta = 1
                                        print(cuadricula())
                                        print('Este es un mapa del tapete')
                                        print('\n\n--HAZ ABIERTO UNA PUERTA --\n')
                                        print('Tu habias escrito el CODIGO SECRETO -- ' + str(propu)[1:-1] + ' --\n'
                                             'y como supsite que el - 8 - te hace avanzar 2 pasos\n'
                                             'Ahora yo puedo hacer cosas mas DIVERTIDAS con los CODIGOS SECRETOS\n'
                                             '\n--SIGUE INVESTIGANDO--\n''escribe otro codgo y veras lo que pasa\n')
                                        Vpresenta = 0
                                elif mapo == 1:
                                    mapo = 1
                                    vcamino = medicen
                                    print(cuadricula())
                            else:
                                print ('Estas Muy Muy cerca\n --Sigue probando con comas--')
                        elif medicen in [i for i in reconocibles1+reconocibles2]:
                            print('Parece que te ecercas ese tambien es epecial')
                    elif ',' not in reconocibles1+reconocibles2:
                        print ('\nEse numero no me parece especial')
                else:
                    medicen=raw_input('Eso es un numero. Yo soy buena con eso.\nQue hago con el '+medicen+' ??\n'+medicen+'...')

                if any(i in medicen for i in LRcalculos):
                    medicen2=raw_input('Con que otro numero?\n..>')
                    try:
                        resu= propu * eval(medicen)
                        print ('Lo multilique ' + str(propu) + '*' + medicen2 + '=' + str(resu))
                        print ('Tal vez no entendi intenta hablarme en codigo\n'
                               'Mi codigo para calcular numeros es que los escribas entre parentesis \n'
                               'Ejem...(2+2-3) o ...(2*5)')
                    except:
                        print ('No pude. intenta hablarme en codigo')

                elif medicen in ['abansa','avansa','avanza','abanza','jira','gira','salta','brinca']:
                    print('Te acercas a descubrir el codigo que se hablar\n una pista \n-- utiliza comas --')
            else:
                print ('Te acuerdas que te dije que Guardo un misterio\n a lo mejor tu lo conoces\n tiene que ver con numeros, cartas y mapas')

        except:
            # print('--ALGO DEVES SABER--')
            print ('\nReconoci la primera letra que escribiste Pero:\n')
            if len(medicen.split(' ')) > 1:
                print('\n' + LRPNocomprendo[PNC+1] + '--" ' + medicen + ' "--' + LRPNocomprendo2[PNC2+1])
            else:
                print('\n' + LRPNocomprendo[PNC] + '--" ' + medicen + ' "--' + LRPNocomprendo2[PNC2])


    elif medicen == 'pasale':
        pass
    else:
        PIST+=1
        medijeronNC.append(medicen)
        if len(medicen.split(' '))>1:
            print('\n'+LRPNocomprendo[PNC+1]+'--" '+medicen+' "--'+LRPNocomprendo2[PNC2+1])
        else:
            print('\n'+LRPNocomprendo[PNC]+'--" '+medicen+' "--'+LRPNocomprendo2[PNC2])



import numpy as np
import copy
import graphviz
from datetime import datetime

#---------------------------------LEER UN ARCHIVO TXT CON EL REGISTRO DE TRAZAS-----------------------------------
#lee archivo txt
def readInput(): #leer el archivo

    try:

        inputfile = open("inputfile.txt", "r")
        lines = [line.rstrip("\n") for line in inputfile]
        inputfile.close()
    except:
        print("no encuentro el archivo...")
        return []
    #try-except

    f=[]
    L = []

    for i in range(len(lines)):
        L.append(list(lines[i]))


    return L

# se guardan las relaciones causales a traves de diccionarios.
def listAdyacencia(log):
   #log, obtiene el registro extraido del txt L


        adj_list = {} #diccionario para guardar las relaciones causales

        for t in log:  # 2 #toma una primera palabra del registro

                for i, L in enumerate(t):  # 5 toma cada una de las transiciones de la palabra y busca cual es su siguiente

                        if L not in adj_list.keys(): #si aun no esta en el diccionario lo agrega
                                adj_list[L] = set()
                        if i + 1 < len(t): #valida que no se pase del rango
                                adj_list[L].add(t[i + 1])

        for k, v in adj_list.items(): #Revisa el diccionario y busca las concurrencias entre las relaciones
                adj_list[k] = list(v)

        rel = []
        for node1 in adj_list.keys(): #si el nodo que estamos revisando se encuentra dentro del nodo que mantiene entre sus relaciones causales
                for node2 in adj_list[node1]:
                        if node1 in adj_list[node2]:
                                rel.append([node1, node2]) #si es asi se agrega a una lista de relaciones de concurrencia

        #print(adj_list) #lista de relaciones causales
        #print(rel)      #lista de cuales son concurrentes

        return adj_list #,rel

# crea la red base de n<
def red_base(base):
    lugares = []  # lugares de la red base
    dicc = {}
    post_dicc = {}
    caminos = []  # funcion de transicion

    for i in range(len(list(base))):  # medida de x,a,b,c,y

        # lugares.append([i,i+1]) #### esto lo voy hacer pero en las iteraciones del diccionario
        lugares.append([i, i + 1, base[i]])
        caminos.append([i, i + 1, base[i]])

        dicc[base[i]] = list()  # hacemos un diccionario con un formato de lista
        dicc[base[i]].append(i)

        post_dicc[base[i]] = list()
        post_dicc[base[i]].append(i + 1)

    return lugares, caminos, dicc, post_dicc

#genera la funcion de transicion de toda la red
def funcion_transicion(lugares, caminos, dicc, post_dicc):
    analizados = []  # para guardar las relaciones causales que ya analizamos
    for t in lugares:
        letra = t[2]
        antecesor = t[0]  # 0
        posterior = t[1]
        letras_destino = RC[letra]  # a

        analizados.append(letra)

        for i in letras_destino:

            destino = dicc[i]
            lugar_posterior = post_dicc[i]  # ---------------------------------

            if [posterior, lugar_posterior[0], i] not in caminos:
                # print("esta vuelta:", posterior,lugar_posterior[0],i)
                caminos.append([posterior, lugar_posterior[0], i])

    # print("analizados:", analizados)



    #print("RED N<", caminos)

    return caminos

def min_moore(caminos_funcion):
    # ------------------------------METODO DE MOORE---------------------------------------
    # bucamos los caminos equivalentes

    caminos = caminos_funcion
    equal = []
    for t in caminos:

        way = t  # camino para comparar

        for j in caminos:

            if way != j:

                if way[1:] == j[1:]:

                    if [way[0], j[0]] and [j[0],
                                           way[0], ] not in equal:  # elimina concurrencias para la union de lugares

                        equal.append([way[0], j[0]])  # guardamos relaciones de moore
                    # if

                # if

            # if

        # for

    # for

    #print("Estados Equivalentes:", equal)

    return equal

    # -------------------------------------------------------------------------------

def transitividad(equal):
    combinador = []
    visited = set()

    for i in range(len(equal)):

        visited = set()
        start = equal[i][0]
        next = equal[i][1]

        visited.add(start)
        visited.add(next)

        for j in range(len(equal)):

            if next == equal[j][0]:

                next = equal[j][1]
                visited.add(next)

                if next == start:
                    combinador.append(list(visited))

    #print("equivalente:", visited)

    return visited

    # visited= b #nombre del nuevo lugar

def red_simplificada(caminos_funcion):

    caminos= caminos_funcion

    # nueva red simplificada con el metodo de moore

    for i in caminos:

        if i[0] in visited:
            i[0] = "beta"

        if i[1] in visited:
            i[1] = "beta"

    #print("red minimizada", caminos)

    # --------------verificar que no exista dos veces el mismo camino-------------------------
    caminos_min = []

    for i in caminos:

        if i not in caminos_min:
            caminos_min.append(i)


    #print("Caminos mínimos:", caminos_min)

    return caminos_min

#RED NC
def Red_Nc(red_minimizada):


    caminos_min= red_minimizada
    # print(base)
    nc_dicc = {}

    for i in caminos_min:
        # print(i[2])

        if i[2] not in nc_dicc.keys():

            nc_dicc[i[2]] = []
            nc_dicc[i[2]].append(True)
        else:
            nc_dicc[i[2]].append(True)


    #print("RED NC ", nc_dicc)

    return nc_dicc



#Red compuesta nc, n<
def Red_compuesta(nc_dicc,red_minimizada):

    caminos_min= red_minimizada

    for i in caminos_min:

        # i[2] es la letra (la llave en nc_dicc)
        # nc_dicc[i[2]] es la lista de trues/falses de i[2]
        if True in nc_dicc[i[2]]:

            trueindex = nc_dicc[i[2]].index(True)
            letra = i[2]

            # print(trueindex)
            # print("letra: "+letra)
            nc_dicc[letra][trueindex] = False
            # print(nc_dicc[letra])

        else:
            print("No aceptada")


#-----------------------------------red n<-----------------------------------------------------
log = readInput() #registro
base=log[0]

#print("base",base)
RC= listAdyacencia(log) #RELACIONES CAUSALES
#print("log",log)







print("Relaciones Causales", RC)
#print("Traza 1",log[1] ) #longitud del registro 1
print("---------------------------------------------------")


lugares, caminos, dicc, post_dicc = red_base(base)
funcion_transicion(lugares, caminos, dicc, post_dicc )
print("RED BASE (lugares)", lugares)
print("---------------------------------------------------")


caminos_funcion = funcion_transicion(lugares, caminos, dicc, post_dicc )
print("RED N< FORZADA(duplicadas)", caminos_funcion)
print("---------------------------------------------------")


equal=min_moore(caminos_funcion)
print("lugares equivalentes", equal)
visited= transitividad(equal)
#print(visited)

red_minimizada= red_simplificada(caminos_funcion)
print("---------------------------------------------------")
print("RED N< minima", red_minimizada)
print("---------------------------------------------------")



nc_dicc= Red_Nc(red_minimizada)
print("RED NC:", nc_dicc)
print("---------------------------------------------------")

red_final=Red_compuesta(nc_dicc,red_minimizada)
print("RED COMPUESTA", red_final)
print("---------------------------------------------------")


caminos_min = red_minimizada
#print("caminos_min", caminos_min)

#----------------------------------GRAPHVIZ------------------------------------------

def createGraph(Gname):

    return graphviz.Digraph(
        name=Gname,
        filename=Gname+"_"+datetime.now().strftime("%Y_%m_%d_%H_%M_%S"),
        engine="dot"
    )

#createGraph


#RED N<
def generatePetriNet(G): #G es un digrafo de graphviz

    global caminos_min

    lugares_analizados=[] #los lugares creados (para no crear lugares repetidos)

    #LUGARES N<
    for x in caminos_min:

        print("procesando fila: "+str(x))

        #lugar 0
        labelstr = str(x[0])

        if labelstr not in lugares_analizados:
            G.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")
            lugares_analizados.append(labelstr)
            print("puse: "+labelstr)
        #if

        #lugar 1
        labelstr = str(x[1])
        if labelstr not in lugares_analizados:
            G.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")
            lugares_analizados.append(labelstr)
            print("puse: "+labelstr)
        #if

        #transición
        labelstr = str(x[2])
        G.node(labelstr, color="black", shape="rect", fontsize="11.0", fixedsize="true", width="0.5", height="0.15", label=labelstr, fontcolor="white", style="filled", fillcolor="black")
        print("puse: "+labelstr)

       
    #for

    caminos_arcos= [] #guarda los caminos ya realizados con los arcos

    #ARCOS
    for i in caminos_min:

        print(i)

        if [i[0],i[2]] or [i[2],i[1]] not in caminos_arcos:

           

        
            
            G.edge(str(i[0]),  # origen de la flecha
                   str(i[2]),  # destino de la flecha
                   fontsize="10.0", color="blue")
            caminos_arcos.append([i[0],i[2]])

            G.edge(str(i[2]),  # origen de la flecha
                   str(i[1]),  # destino de la flecha
                   fontsize="10.0", color="blue")
            caminos_arcos.append([i[2],i[0]])

        else:

            print("Ya existe")

        
    print("caminos_arcos", caminos_arcos)



    return G
#generatePetriNet


def generatePetrinet_nc(G2):

    global nc_dicc
    lugares_analizados = []

    caminos_arcos=[]

    #________________crear el lugar inicial, la transicion x

    #lugar 1
    labelstr = "0"
    G2.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")

    #transición
    labelstr = "x"
    G2.node(labelstr, color="black", shape="rect", fontsize="11.0", fixedsize="true", width="0.5", height="0.15", label=labelstr, fontcolor="white", style="filled", fillcolor="black")

    #flechas lugar cero a transicion x
    G2.edge("0", "x", fontsize="10.0", color="blue")



    #________________crear lugar final, la transicion y
        
    #lugar
    labelstr = "final"
    G2.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")

    #transición
    labelstr = "y"
    G2.node(labelstr, color="black", shape="rect", fontsize="11.0", fixedsize="true", width="0.5", height="0.15", label=labelstr, fontcolor="white", style="filled", fillcolor="black")
        
    #flechas lugar cero a transicion x
    G2.edge("y", "final", fontsize="10.0", color="blue")



    caminos_arcos=[]

    for x in nc_dicc.keys():

        if x=="y":
            break #terminar el programa
        elif x=="x":
            continue #siguiente iteración
        else:

            
            if [x+"_pre", x+"_post"] not in caminos_arcos:

                #pre-lugar
                labelstr = x+"_pre"
                G2.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")

                #pos-lugar
                labelstr = x+"_post"
                G2.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")

                #transicion
                labelstr = x
                G2.node(labelstr, color="black", shape="rect", fontsize="11.0", fixedsize="true", width="0.5", height="0.15", label=labelstr, fontcolor="white", style="filled", fillcolor="black")

                    
            

                #flecha de x al pre
                G2.edge("x", x+"_pre", fontsize="10.0", color="blue")

                #flecha del pre a la transición
                G2.edge(x+"_pre", x, fontsize="10.0", color="blue")

                #flecha de x al post
                G2.edge(x, x+"_post", fontsize="10.0", color="blue")

                #flecha del post a y
                G2.edge(x+"_post", "y", fontsize="10.0", color="blue")

                caminos_arcos.append([x+"_pre", x+"_post"])


            else:

                print("ya existe")



    print("camino arcos nc:", caminos_arcos)

            #if-else

        #if-else
    #for

    return G2


def R_CAUSALES(G3):

    global RC

    lugares_creados=[]

    for x in RC.keys():

        lista= RC[x] #toma los valores que estan en formato de lista #?? es con items

        if x not in lugares_creados:  
            #crear lugar
            labelstr = x
            G3.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")


        for z in lista: #recorre la lista

            print(z)

            if z not in lugares_creados:

                #crear lugar si todavia no existe y lo conecta
                labelstr = z
                G3.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")
                
                #flecha de lugar a lugar
                G3.edge(x, z, fontsize="10.0", color="blue")


            else: # solo conecta el lugar existente


                #flecha de lugar a lugar
                G3.edge(x, z, fontsize="10.0", color="blue")


def generatePetriNet_COMPUESTA(G4):


    global caminos_min

    lugares_analizados=[] #los lugares creados (para no crear lugares repetidos)



    #crear y
    labelstr = 'y'
    G4.node(labelstr, color="black", shape="rect", fontsize="11.0", fixedsize="true", width="0.5", height="0.15", label=labelstr, fontcolor="white", style="filled", fillcolor="black")
    lugares_analizados.append(labelstr)


    #LUGARES N<
    for x in caminos_min:

        print("procesando fila: "+str(x))

        #lugar 0
        labelstr = str(x[0])

        if labelstr not in lugares_analizados:
            G4.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")
            lugares_analizados.append(labelstr)
            print("puse: "+labelstr)
        #if




        #lugar 1
        labelstr = str(x[1])
        if labelstr not in lugares_analizados:
            G4.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")
            lugares_analizados.append(labelstr)
            print("puse: "+labelstr)
        #if





            #transición
        labelstr = str(x[2])

        G4.node(labelstr, color="black", shape="rect", fontsize="11.0", fixedsize="true", width="0.5", height="0.15", label=labelstr, fontcolor="white", style="filled", fillcolor="black")
        print("puse: "+labelstr)


        #RED NC

        if labelstr != 'x' and labelstr != 'y':


            G4.node(labelstr, color="black", shape="rect", fontsize="11.0", fixedsize="true", width="0.5", height="0.15", label=labelstr, fontcolor="white", style="filled", fillcolor="black")
            print("puse: "+labelstr)

            
             #pre-lugar
            labelstr = x[2]+ "_pre"
            G4.node(labelstr, color="green", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")

            #pos-lugar
            labelstr = x[2]+ "_post"
            G4.node(labelstr, color="green", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")

           


            #flecha de x al pre
            G4.edge("x", x[2]+"_pre", fontsize="10.0", color="green")

            #flecha del pre a la transición
            G4.edge(x[2]+"_pre", x[2], fontsize="10.0", color="green")

            #flecha de x al post
            G4.edge(x[2], x[2]+"_post", fontsize="10.0", color="green")

            #flecha del post a y
            G4.edge(x[2]+"_post", "y", fontsize="10.0", color="green")



       
    #for


    #ARCOS
    for i in caminos_min:

        print(i)

        G4.edge(str(i[0]),  # origen de la flecha
               str(i[2]),  # destino de la flecha
               fontsize="10.0", color="blue")

        G4.edge(str(i[2]),  # origen de la flecha
               str(i[1]),  # destino de la flecha
               fontsize="10.0", color="blue")




    

       
    return G4

#generatePetriNet


def visual_red_base(G5):

    global lugares

    lugares_analizados=[] #los lugares creados (para no crear lugares repetidos)

    #LUGARES N<
    for x in lugares:

        print("procesando fila: "+str(x))

        #lugar 0
        labelstr = str(x[0])

        if labelstr not in lugares_analizados:
            G5.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")
            lugares_analizados.append(labelstr)
            print("puse: "+labelstr)
        #if

        #lugar 1
        labelstr = str(x[1])
        if labelstr not in lugares_analizados:
            G5.node(labelstr, color="black", fontsize="12.0", label=labelstr, fixedsize="true", width="0.5")
            lugares_analizados.append(labelstr)
            print("puse: "+labelstr)
        #if

        #transición
        labelstr = str(x[2])
        G5.node(labelstr, color="black", shape="rect", fontsize="11.0", fixedsize="true", width="0.5", height="0.15", label=labelstr, fontcolor="white", style="filled", fillcolor="black")
        print("puse: "+labelstr)

       
    #for


    #ARCOS
    for i in lugares:

        print(i)

        G5.edge(str(i[0]),  # origen de la flecha
               str(i[2]),  # destino de la flecha
               fontsize="10.0", color="blue")

        G5.edge(str(i[2]),  # origen de la flecha
               str(i[1]),  # destino de la flecha
               fontsize="10.0", color="blue")




def display():

    a = []
    G1 = createGraph("RED_N<")
    generatePetriNet(G1)
    a.append(G1.source)
    #G1.view()


    G2 = createGraph("Red_Nc")
    generatePetrinet_nc(G2)
    #G2.view()
    a.append(G2.source)


    G3 = createGraph("Relaciones_Causales")
    R_CAUSALES(G3)
    #G3.view()
    a.append(G3.source)

    G4 = createGraph("RED_COMPUESTA")
    generatePetriNet_COMPUESTA(G4)
    #G4.view()
    a.append(G4.source)
    G5 = createGraph("Red_base_n<")
    visual_red_base(G5)
    #G5.view()
    a.append(G5.source)
    print(a)
    return a
    #G6 = createGraph("Red_N<_DUPLICADAS")
    #visual_red_nc_nomin(G6)

    #G6.view()






#def main():

#    display()
#main

#if __name__=="__main__":
 #       main()


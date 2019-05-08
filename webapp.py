from __future__ import print_function
from flask import Flask, jsonify, abort, make_response, request
from requests import Request, Session
import requests
import json

app = Flask(__name__)

@app.route('/')
def arbol():
    info = requests.get('http://localhost:5000/')
    # retorno el resultado del objeto Request
    return info.text

#Objeto Request para calcular el Ancestro
@app.route('/nodosHijos')
def nodosHijos():
    nodos = requests.get('http://localhost:5000/nodosancestro')
    # retorno el resultado del objeto Request
    return nodos.text

"""
# CONSTRUCCIÓN DEL ARBOL BINARIO
"""
#Declaramos la clase NODE
class Node:
    
    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        self.parent = parent
        
    #Metodos para asignar NODOS
    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):
        # Creamos un nuevo nodo
        new_node = Node(label, None)
        # Si el árbol esta vacio
        if self.empty():
            self.root = new_node
        else:
            # Si el árbol no esta vacio
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if new_node.getLabel() < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            new_node.setParent(parent_node)
            
    def getNode(self, label):
        curr_node = None
        if(not self.empty()):
            curr_node = self.getRoot()
            while curr_node is not None and curr_node.getLabel() is not label:
                if label < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
        return curr_node
    
    def empty(self):
        if self.root is None:
            return True
        return False
            
    #Para recorrer el arbol
    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList
    
    def getRoot(self):
        return self.root

    #Para mostrar los datos
    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getLabel().__str__()
        return str

#Recorrido InPreOrden
#pre-orden: nodo actual -> rama izquierda  -> rama derecha
#pre-orden: primero se ejecuta sobre la raiz, despues sobre todos los menores y despues sobre todos los mayores
def InPreOrder(curr_node):
    nodeList = []
    if curr_node is not None:
        nodeList = nodeList + InPreOrder(curr_node.getLeft())
        nodeList.insert(0, curr_node.getLabel())
        nodeList = nodeList + InPreOrder(curr_node.getRight())
    return nodeList

def InPreOrder2(root,curr_node,curr_nodes):
    """Variable contador"""
    count = 0
    ancest = 0
    nodeList = []
    nodeLists = []
    if curr_node is not None:
        nodeList = nodeList + InPreOrder(root.getLeft())
        nodeList.insert(0, root.getLabel())        
        nodeList = nodeList + InPreOrder(root.getRight())
        for x in nodeList:
            if curr_node.getLabel() in nodeList:
                indice = nodeList.index(curr_node.getLabel())
                for x in nodeList:
                    if (nodeList.index(x) > nodeList.index(curr_node.getLabel())): 
                        nodeList.remove(x)
    #return nodeList
        
    if curr_nodes is not None:
        nodeLists = nodeLists + InPreOrder(root.getLeft())
        nodeLists.insert(0, root.getLabel())        
        nodeLists = nodeLists + InPreOrder(root.getRight())
        for x in nodeLists:
            if curr_nodes.getLabel() in nodeLists:
                indice = nodeLists.index(curr_nodes.getLabel())
                for x in nodeLists:
                    if (nodeLists.index(x) > nodeLists.index(curr_nodes.getLabel())): 
                        nodeLists.remove(x)
                        
    #Comparo las listas de cada nodo hijo y eliminos los valores distintos
    #Para Poder Encontrar El Ancestro que comparten Ambos nodos:
    if(len(nodeList) != len(nodeLists)):
        if(nodeList > nodeLists):
            for t in reversed(nodeList):
                """Variable contador"""
                count = count+1
                if(len(nodeList) != len(nodeLists)):
                    nodeList.remove(t)
            #print(len(nodeList), len(nodeLists))
            #return nodeList, nodeLists, count
            """Como las listas terminan teniendo la misma longitud
            Si es mayor a 4, el ancestro es el valor de la lista en [0]"""
            if(len(nodeList) >= 4 or count > 4):
                ancest = nodeList[0]            
                return ancest
            else:
                ancest = nodeLists[1]            
                return ancest
        if(nodeList < nodeLists):
            for t in reversed(nodeLists):
                """Variable contador"""
                count = count+1
                if(len(nodeList) != len(nodeLists)):
                    nodeLists.remove(t)
            #print(len(nodeList), len(nodeLists))
            #return nodeList, nodeLists, count 
            """Como las listas terminan teniendo la misma longitud
            Si es mayor a 4, el ancestro es el valor de la lista en [0]"""
            if(len(nodeLists) >= 4 or count > 4):
                ancest = nodeLists[0]            
                return ancest
            else:
                ancest = nodeLists[1]            
                return ancest                
    else:
        #print(len(nodeList), len(nodeLists))
        """Como las listas terminan teniendo la misma longitud
        Si es mayor a 4, el ancestro es el valor de la lista en [0]"""
        if(len(nodeList) >= 4 or count > 4):
            ancest = nodeList[0]            
            return ancest
        else:
            ancest = nodeLists[1]            
            return ancest
        """Como las listas terminan teniendo la misma longitud
        Si es mayor a 4, el ancestro es el valor de la lista en [0]"""
        if(len(nodeLists) >= 4 or count > 4):
            ancest = nodeLists[0]            
            return ancest
        else:
            ancest = nodeLists[1]            
            return ancest


"""lLAMO LA FUNCIÓN PARA Construcción del arbol en una variable """
t = BinarySearchTree()
# Guardo el Objeto Request
m = arbol()
#Se Convierte en Diccionario de Python el objeto "m"
a = json.loads(m)

#Recorremos el diccionario
# Insertamos los valores en la función Construcción del arbol
for dic in a.values():
    t.insert(dic)

"""Para calcular el Ancestro Guardo el Objeto Request """
h = nodosHijos()
#Se Convierte en Diccionario de Python el objeto "h"
listhijos = json.loads(h)
#Recorremos el diccionario
v = list(listhijos.values())
vraiz = v[2]
vnodo1 = v[0]
vnodo2 = v[1]

#Calcular ancestro 

if(t.getNode(vnodo1) is not None and t.getNode(vnodo2) is not None):
    ancestro = InPreOrder2(t.getNode(vraiz),t.getNode(vnodo1),t.getNode(vnodo2))
    #print(InPreOrder2(t.getNode(8),t.getNode(1),t.getNode(1)))    
else:
    ancestro = "Not exist node! ó el nodo no existe en el Arbol"



#Creo una Url que me mostrara el Arbol Binario Generado
@app.route('/arbol', methods=['GET'])
def get_arbol():
    return jsonify(t.__str__())

#Creo una Url que me mostrara el Ancestro de los dos nodos obtenidos en el elemento request
@app.route('/ancestro', methods=['GET'])
def get_ancestro():
    return jsonify(ancestro)

#Se inicia el servicio en otro puerto
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=83)
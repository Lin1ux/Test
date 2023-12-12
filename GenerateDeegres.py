import random
import json

#Macierz jednostkowa
def once(n):    
    matix = []
    for i in range(n):
        matix.append([])
        for j in range(n):
            if i!=j:
                matix[i].append(0)
            else:
                matix[i].append(1)
    return matix

def zero1(n):
    l = []
    for i in range(n):
        l.append(0)
    return l

#Wypisanie czytelniej listy 2 wymiarowej
def printList2(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def IndexList(l):
    newList = []
    for i in range(len(l)):
        newList.append([l[i],i])
    return newList


def GenerateToJSON(numberOfVertex):
    savedData = dict()
    minDegree = 1
    '''if numberOfVertex-1%2 == 0:
        minDegree = (numberOfVertex-1)/2
    else:
        minDegree = (numberOfVertex)/2'''
    maxDegree = numberOfVertex-1
    for i in range(numberOfVertex):
        l = []
        for j in range(numberOfVertex):
            l.append(random.randint(minDegree,maxDegree))
        print(l)
        l = Fixer(l)
        print(Fixer(l))
        print("------")
        #print(l)
        #print(IsGraphic([9, 6, 7, 9, 8, 6, 8, 5, 5, 5]))
        savedData["G"+str(i)] = l
    #print(IsGraphic(l))
    #  fixgraph(l)

    #print(savedData)
    JSONdataToSave = json.dumps(savedData,indent=1)
    with open("InputData.json","w") as f:
        f.write(JSONdataToSave)
        f.close()
        #savedData[i] =
    #print(IsGraphic([2,2,2,2,2,2]))

def IsGraphic(C):
  n=len(C)
  if (n==0):            #Graf nie posiada stopni
    return False
  C.sort(reverse=True)  #Sortowanie od malejąco
  #print(C)
  x=C.pop(0)            #Zredukowana tablica
  print(x)
  if (x==0):            #Jeśli x nie jest spójne ???
    return True
  if (x>n-1):           #Jeśli x ma wierzchołek większy niż maksymalny dopuszczalny stopień (raczej nie potrzebne)
    return False
  #print(C)
  for i in range(x):    #Czy da się połączyć
    if (C[i]==0):       #Jeśli 0 to się nie da 
      return False
    else:
       C[i]=C[i]-1      #Zajęcie wierzchołka
  return IsGraphic(C)

def Fixer(input):
    #input = [1,2,1,2,1,5]
    n = len(input)
    temp = input.copy()
    temp = IndexList(temp)
    temp.sort(reverse=True)
    #temp = temp[::-1] 
    #print(temp)
    graphMatrix = once(n)
    currentDeegries = zero1(n)
    good = True
    for i in temp:
        i2 = i[1]
        for j in range(n):
            if graphMatrix[i2][j]!=1 and currentDeegries[i2] < input[i2] and currentDeegries[j] < input[j]:
                graphMatrix[i2][j] = 1
                graphMatrix[j][i2] = 1
                currentDeegries[i2]+=1
                currentDeegries[j]+=1
        if currentDeegries[i2] != input[i2]:
            good = False
    if good:
       return currentDeegries
    else:
        for i in range(len(currentDeegries)):
            if currentDeegries[i]==0:
                currentDeegries[i] = max(currentDeegries)//2
        #print(currentDeegries)
        return Fixer(currentDeegries)
        
   #wygenerować graf i sprawdzić 0 czy ma same 0 w kolumnie

IsGraphic([1,2,3,4,1,2,3])
#GenerateToJSON(10)
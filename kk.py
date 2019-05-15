import json

Semana=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
Dias={"0":[],"1":[],"2":[],"3":[],"4":[],"5":[],"6":[]}
Fijo=[0,0,0,0,0,0,0]

class Evento:
  def __init__(self ):
      pass

  def __init__(self, Nombre, Duracion, Dia, Hora):
    self.Nombre = Nombre
    self.Duracion = Duracion
    self.Dia = Dia
    self.Hora = Hora

  def show(self):
    print("Hello my name is "
          + self.Nombre)

def write():
    Tareas=[]
    while 1:
        InTarea=input("Tarea= ")
        if (InTarea=="f"): break
        InHora=float(input("Horas= "))
        InMult=int(input("Multiplicidad= "))
        Tareas.append([InTarea,InHora,InMult])
        print()
        
    print(Tareas)  

    for i in Tareas:
        for j in range (i[2]):
            InDia=int(input("Dia("+str(i[0])+"): "))
            Dias[str(InDia)].append(i[:-1])
        
def show():
    global Semana
    
    for j in range(7):
        Semana[j]=Semana[j].center(20,"=")
        
    for i in range(7):
        print(Semana[i],"TOTAL=",suma(Dias,i))
        c=1
        for j in Dias[str(i)]:
            print(str(c)+") "+j[0]+"("+str(j[1])+")")
            c+=1
        
def show2():
    global Semana
    
    for j in range(7):
        Semana[j]=Semana[j].center(20,"=")
        
    for i in range(7):
        print(Semana[i],"RESTANTE=",24-suma(Dias,i)-Fijo[i],"FIJO= "+str(Fijo[i]))
        c=1
        for j in Dias[str(i)]:
            print(str(c)+") "+j[0]+"("+str(j[1])+")")
            c+=1


def save(i):
    json_data = json.dumps(Dias)
    file = open(str(i)+".json","w")
    file.write(json_data)
    file.close()

def get(i):
    global Dias
    with open(str(i)+'.json') as f:
        Dias = json.load(f)

def new():
    global Dias,Fijo
    Dias={"0":[],"1":[],"2":[],"3":[],"4":[],"5":[],"6":[]}
    Fijo=[0,0,0,0,0,0,0]

def getF(i=0):
    with open(str(i)+'.json') as f:
        Dic = json.load(f)
    for j in range(7):
        Fijo[j]+=suma(Dic,j)
    print (Fijo)

def move(index,d_inicial,d_final):
    tmp=Dias[str(d_inicial)]
    data=tmp[index]
    tmp.pop(index)
    Dias[str(d_final)].append(data)

def remove(index,d):
    tmp=Dias[str(d)]
    tmp.pop(index)
        
def suma(d,i):
    l=d[str(i)]
    s=0
    for e in l:
        s+=e[1]
    return s

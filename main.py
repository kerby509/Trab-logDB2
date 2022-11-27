import psycopg2
from copy import copy
import sys

# obter a data e inicia o log

def getLog(name, conn):
    createTable(conn)
    file = open(name, "r")
    data = file.readlines()
    initSimulation(conn, data[:data.index("\n")])
    data = data[:data.index("\n")+1:]
    data.reverse()
    file.close()
    return data

# remove a transição em qualquer linha onde ela apareça
def removeLine(data, trans):
    aux = list(copy(data))
    error = 0
    
    for i in range(len(data)):
        log = data[i][1:-2]
        
        if trans in log.split(",") or trans in log.split(""):
            aux.pop(i - error)
            error= error+1
            
    return aux

# remove o checkpoint e os commits salvos do arquivo redo na memória
def removeCheck(data, unfinished):
    temp = str(unfinished[12:-3])
    temp = temp.split(",")
    finished = []
    
    for i in range(len(data)):
        if data[i] == unfinished:
            break
        if data[i] != "<crash>" and "," not in data[i][1:-2]:
            trans = (data[i[1:-2]]).split(" ")[1]
            if trans not in temp and trans not in finished:
                finished.append(trans)
    
    
    for t in finished:
        data = removeLine(data, t)
        
    data.pop(data.index(unfinished))
    data.reverse()
    data.remove("<End CKPT> \n")
    return data

# encontre o checkpoint finalizado no arquivo log

def findCheckpoint(data):
    stack = []
    for line in data:
        if line == "< End CKPT> \n":
            stack.append(True)
        if len(stack) > 0:
            if stack[-1] and line[:11] == "<Start CKPT>":
                data.reverse()
                data = removeCheck(data, line)
                stack.pop()
                
    return data




data = getLog("entradaLog")

print(data)

data = findCheckpoint(data)

print(data)


    



# Connect to your postgres DB
# conn = psycopg2.connect("dbname=test user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM data")

# Retrieve query results
records = cur.fetchall()

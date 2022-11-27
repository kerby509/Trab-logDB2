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

    
    



# # Connect to your postgres DB
# # conn = psycopg2.connect("dbname=test user=postgres")

# # Open a cursor to perform database operations
# cur = conn.cursor()

# # Execute a query
# cur.execute("SELECT * FROM my_data")

# # Retrieve query results
# records = cur.fetchall()

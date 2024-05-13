# import numpy as np
import pyodbc
import array as arr 
# from scipy.optimize import linprog

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\htsav\OneDrive\99_WorkingSpace\37a_Simplex_Data\Lessons.accdb;')
# emp_cursor = conn.cursor()
# emp_cursor.execute('SELECT * FROM Employees')
   
# for row in emp_cursor.fetchall():
#     print(row)
c = 3
r = 107 * 107
collisions2d = [[0] * c for i in range(r)]
    
occ_cursor = conn.cursor()
occ_cursor.execute('SELECT * FROM Occurences_Analysis')
for row2 in occ_cursor.fetchall():
    y = row2[1]-1
    x = (row2[0]-1)*107 +y
    collisions2d[x][y] = row2[2]
    
     


for i in range(r):
    for j in range(c):
        collisions2d[i][0] =i 
        collisions2d[i][1] =j
        # if row2[0] == i and row2[1] == j :
        #     collisions2d[i][1] =row2[2]       
        # else:
        #    collisions2d[i][1] =0     
print(collisions2d)









#c->Minimize          w = 10*y1 + 15*y2 + 25*y3
#Subject to:       y1 + y2 + y3 >= 1000
                  #y1 - 2*y2    >= 0
#                            y3 >= 340
#with              y1 >= 0, y2 >= 0
#pLEASE 

# A = np.array([[-1, -1, -1], [-1,2, 0], [0, 0, -1], [-1, 0, 0], [0, -1, 0]])
# b = np.array([-1000, 0, -340, 0, 0])
# c = np.array([10,15,25])

# res = linprog(c, A_ub=A, b_ub=b,bounds=(0, None))

# print('Optimal value:', res.fun, '\nX:', res.x)
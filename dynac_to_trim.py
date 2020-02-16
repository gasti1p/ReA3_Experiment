import math,sys 
import numpy as np



input_file = sys.argv[-1]
AtomNum=int (raw_input('\nAtomic Number:\n') )

fout = open('TRIM_output.txt','wb')

fout.write("=========== TRIM with various Incident Ion Energies/Angles and Depths =========\n")
fout.write("= This file tabulates the kinetics of incident ions or atoms.                 =\n")
fout.write("= Col.#1: Ion Number, Col.#2: Z of atom leaving, Col.#3: Atom energy (eV).    =\n")
fout.write("= Col.#4-6: Last location:  Col.#4: X= Depth into target.                     =\n")
fout.write("= Col.#5,6: Y,Z= Transverse axes                                              =\n")
fout.write("= Col.#7-9: Cosines of final trajectory.                                      =\n")
fout.write("================ Typical Data File is shown below  ============================\n")
fout.write("======= TRIM Calc.=  User ========================= ===========================\n")
fout.write("Event  Atom  Energy  Depth   Lateral-Position   ----- Atom Direction ----\n")
fout.write("Name   Numb   (eV)    _X_(A)   _Y_(A)  _Z_(A)   Cos(X)   Cos(Y)   Cos(Z)")


NumPrt = 1

with open (input_file,'r') as fin:
   first_line = fin.readline()
   second_line = fin.readline()
   for line in fin:
	x = float(line.split()[0])
	px = float(line.split()[1])
	y = float(line.split()[2])
	py = float(line.split()[3])
	e = float(line.split()[5])

	Y = x*1e+8
	Z = y*1e+8
	X = 0.0
	E = e*1e+6
	
	theta = math.sqrt( math.pow(px,2) + math.pow(py,2) )
	phiA = math.fabs( math.atan( math.sin(px)*math.cos(py) / math.sin(py)   ) )
	
	if ( px>0 and py>0): phi = phiA
	if ( px<0 and py<0): phi = phiA + math.pi
	if ( px>0 and py<0): phi = math.pi - phiA
	if ( px<0 and py>0): phi = 2*math.pi - phiA


	COSZ = math.sin(theta)*math.cos(phi);
 	COSY = math.sin(theta)*math.sin(phi);	
        COSX = math.cos(theta);

	fout.write("\r\n%i    " %int(NumPrt) + "%i   " %int(AtomNum) + "{:.7E}  ".format(E) + "{:7E}  ".format(X) + "{:4E}  ".format(Y) + "{:4E}  ".format(Z) + "{:7E}  ".format(COSX) + "{:7E}  ".format(COSY) + "{:7E}".format(COSZ))

	NumPrt +=1

fin.close()
fout.close()


print "\n Number of particles: {}\n".format(NumPrt)







import math,sys 
import numpy as np



input_file = sys.argv[-2]
initial_beam_file = sys.argv[-1]

	
CS=int (raw_input('\nCharge State:\n') )


E = []
X = []
Y = []
Z = []	
COSX = []
COSY = []
COSZ = []
t = []
NumberOfParticles=0
with open (input_file) as textFile:
	for line in textFile:
		if line.startswith('T'):
			E.append(float(line[7:].split()[1]))
			X.append(float(line[7:].split()[2]))
			Y.append(float(line[7:].split()[3]))			
			Z.append(float(line[7:].split()[4]))
			COSX.append(float(line[7:].split()[5]))
			COSY.append(float(line[7:].split()[6]))
			COSZ.append(float(line[7:].split()[7]))
			#if (NumberOfParticles == 100000): break
			NumberOfParticles +=1

		elif line[0].isdigit():
			E.append(float(line.split()[2]))
			X.append(float(line.split()[3]))
			Y.append(float(line.split()[4]))			
			Z.append(float(line.split()[5]))
			COSX.append(float(line.split()[6]))
			COSY.append(float(line.split()[7]))
			COSZ.append(float(line.split()[8]))
			#if (NumberOfParticles == 100000): break
			NumberOfParticles +=1
		else: continue

print "\n Number of Particles:  {}\n".format(NumberOfParticles)


try:
	with open (initial_beam_file) as f:
		first_line = f.readline()
		for line in f:
			t.append( float(line.split()[4]) )
except: 
	print "\n No initial beam file has been chosen! \n"
	pass
	
Eaverage = np.mean(E)*1E-6

energy = np.array(E)*1E-6
x=np.array(Y)*1E-8
y=np.array(Z)*1E-8

theta = np.arccos(COSZ)
theta_em = np.arccos(COSX)  
px = np.array(  np.power(np.arccos(COSX),2) - np.power(np.arccos(COSY),2) ) /math.pi  +  math.pi/4


py = []

for i in xrange(0,NumberOfParticles,1):
	if (theta[i] < math.pi/2): 
		py.append( math.sqrt ( math.fabs ( math.pow(math.acos(COSX[i]),2) - math.pow(px[i],2) )  )   )  

	else: 
		py.append( - math.sqrt ( math.fabs ( math.pow(math.acos(COSX[i]),2) - math.pow(px[i],2) )  )  )


f = open("output.txt","wb")

f.write("%i" %(NumberOfParticles+1) + "     80.5      %f\n" %Eaverage)
try: f.write("0.0	0.0	0.0	0.0" + "	%f"%t[0] + "	%f" %Eaverage + "    %i\n" %CS )
except: f.write("0.0	0.0	0.0	0.0	0.0" + "    %f" %Eaverage + "    %i\n" %CS )



try:
	for i in xrange(0,NumberOfParticles,1):
	        f.write("%f" %x[i] + "     %f" %px[i] + "     %f" %y[i]+"     %f" %py[i]+"     %f"%t[i] + "     %f" %energy[i] + "    %i\n"%CS)

except: 
	for i in xrange(0,NumberOfParticles,1):
		f.write("%f" %x[i] + "     %f" %px[i] + "     %f" %y[i]+"     %f" %py[i]+"     0.0" + "     %f" %energy[i] + "    %i\n"%CS)

f.close()






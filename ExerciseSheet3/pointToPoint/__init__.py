import subprocess
import time

# naive = 'mpiexec -n 32 python C:\\Users\\Mario\\Documents\\EclipseProjects\\Exercise3\\pointToPoint\\naive.py 100000000' 
# efficient = 'mpiexec -n 32 python C:\\Users\\Mario\\Documents\\EclipseProjects\\Exercise3\\pointToPoint\\efficient.py 10000000'

tamIni = 1000
tamFin = 100000000
procsIni = 16
procsFin = 32
pathNaive = ' python C:\\Users\\Mario\\Documents\\EclipseProjects\\Exercise3\\pointToPoint\\naive.py '
pathEfficient = ' python C:\\Users\\Mario\\Documents\\EclipseProjects\\Exercise3\\pointToPoint\\efficient.py '
mpiexec = 'mpiexec -n '

print("Measure kind\tProcesses\tTam. Array\tTime")
while tamIni <= tamFin:
    while procsIni <= procsFin:        
        fullNaive = mpiexec + str(procsIni) + pathNaive + str(tamIni)
        fullEficcient = mpiexec + str(procsIni) + pathEfficient + str (tamIni)
           
        start = time.time()
        subprocess.call(fullNaive)
        end = time.time()
        print("Full program time naive:\t{}\t{}\t{}".format(procsIni, tamIni, (end-start)))
          
        start = time.time()
        subprocess.call(fullEficcient)
        end = time.time()
        print("Full program time efficient:\t{}\t{}\t{}".format(procsIni, tamIni, (end-start)))
           
        procsIni+=procsIni
        print('----')
    procsIni=16
    tamIni*=100

# start = time.time()
# subprocess.call(efficient)
# end = time.time()
# print("Full program time efficient:\t{}\t{}\t{}".format(32, 100000000, (end-start)))
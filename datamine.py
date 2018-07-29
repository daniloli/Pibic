import csv
import urllib2
from math import *
from matplotlib.pylab import *


#obtém os dados do site google finance
inp=raw_input('digite o nome da empresa(exemplo:AAPL):')
url = 'http://www.google.com/finance/getprices?q=%s&i=120&p=10d&f=d,o,h,l,c,v'%(inp)
response = urllib2.urlopen(url)
cr = csv.reader(response)



#salva os dados obtidos pelo site em vetores diferentes para poder manipular
#e salvar em arquivo texto

#vetor dos dados obtidos pelo site
idate=[]
iclose=[]
ihigh=[]
ilow=[]
iopn=[]
ivolume=[]

for row in cr:
    
    try:
        float(row[1])
    except IndexError:
        continue
    except ValueError:
        continue

    if row[0][0]=='a':
        k=[]
        for i in range(1,len(row[0])):
            k.append(row[0][i])
        k=''.join(k)
        k=float(k)
        
        idate.append(k)
    else:
        idate.append(k+120*float(row[0]))
        
    iclose.append(float(row[1]))
    ihigh.append(float(row[2]))
    ilow.append(float(row[3]))
    iopn.append(float(row[4]))
    ivolume.append(float(row[5]))


#Abre o arquivo texto, caso ela nao exista, cria um arquivo e adiciona os valores
#novos ao arquivo

#vetor dos dados obtidos pelo arquivo texto  
date=[]
close=[]
high=[]
low=[]
opn=[]
volume=[]
 
    
f=open('%s.txt' %inp ,'a+')
for line in f:
    x=line.split(',')
    date.append(float(x[0]))
    close.append(float(x[1]))
    high.append(float(x[2]))
    low.append(float(x[3]))
    opn.append(float(x[4]))
    volume.append(float(x[5]))
cte=0    
if idate[0] in date:
    cte=len(date)-date.index(idate[0])
if cte>=len(idate):
    f.close() 
else:
    for i in range(cte,len(idate) ):
        f.write('%f,%g,%g,%g,%g,%g \n'%(idate[i],iclose[i],ihigh[i],ilow[i],iopn[i],ivolume[i]))
    f.close()
    
    
#Junta os dados obtidos online com os ja existentes no arquivo texto.
date=[]
close=[]
high=[]
low=[]
opn=[]
volume=[]

f=open('%s.txt' %inp ,'a+')
for line in f:
    x=line.split(',')
    date.append(float(x[0]))
    close.append(float(x[1]))
    high.append(float(x[2]))
    low.append(float(x[3]))
    opn.append(float(x[4]))
    volume.append(float(x[5]))
f.close()




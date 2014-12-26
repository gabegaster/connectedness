import csv
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np

with open("bootstrap.data",'r') as f:
    r = csv.reader(f)
    data = [(int(a),int(b),float(c)) for a,b,c in r]

with open("bootstrap_10_30.data",'r') as f:
    data2 = [i.split(" ",2) for i in f]
    data2.pop()
    data2 = (map(eval,i) for i in data2)
    data.extend((a,b,c) for a,b,(c,d) in data2)

data = np.array(data)

colors = "indigo black firebrick green chartreuse blue aquamarine brown peru orange fuchsia".split()

ks = sorted(map(int,set(data[:,0])))

x_step = 120
for c,i in zip(colors,ks):
    X,Y = data[data[:,0]==i][:,1:].T
    plt.plot(X,Y, color=c, alpha=.6)
    plt.text(x_step*(i-2),.285,i,color=c,alpha=.6,size=16)
    mean = Y[500:].mean()
    plt.text(x_step*(i-2),.27,"%.2f"%(100*mean), color=c,alpha=.6,size=16)

plt.text(50,.285,"k",color="black",size=16)
plt.text(50,.27,"ave",color="black",size=16)

plt.ylabel("Percent Connected")
plt.xlabel("N")
plt.show()
#plt.savefig("bootstrap.png")

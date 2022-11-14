import pandas as pd
import os


dt = 5e3
Quats = []
bodies = ['time']

for (dirpath, dirnames, filenames) in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.csv'): 
            df = pd.read_csv(filename)
            Q = []
            for i in range(len(df['q0'])):
                Q.append([df['q0'][i], df['q1'][i], df['q2'][i], df['q3'][i]])
            Quats.append(Q)
            bodies.append(filename[:-4])



with open('oriantation.sto', 'w') as f:
    f.write("DataRate=200.000000\n")
    f.write("DataType=Quaternion\n")
    f.write("version=3\n")
    f.write("OpenSimVersion=4.4-2022-07-23-0e9fedc\n")
    f.write("endheader\n")
    f.write('\t'.join(bodies))
    f.write('\n')

    t = 0
    for i in range(min([len(q) for q in Quats])):
        f.write(str(t))
        for Q in Quats:
            f.write('\t')
            f.write(f"{Q[i][0]},{Q[i][1]},{Q[i][2]},{Q[i][3]}")
        f.write("\n")
        t += dt
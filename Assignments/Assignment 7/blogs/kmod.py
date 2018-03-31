import clusters

blognames,words,data=clusters.readfile('blogdata.txt')
kcl=clusters.kcluster(data,k=20)
print([blognames[r] for r in kcl[0]])
print([blognames[r] for r in kcl[1]])
print([blognames[r] for r in kcl[2]])
print([blognames[r] for r in kcl[3]])
print([blognames[r] for r in kcl[4]]) #kmod for 5
print([blognames[r] for r in kcl[5]])
print([blognames[r] for r in kcl[6]])
print([blognames[r] for r in kcl[7]])
print([blognames[r] for r in kcl[8]])
print([blognames[r] for r in kcl[9]]) #kmod for 10
print([blognames[r] for r in kcl[10]])
print([blognames[r] for r in kcl[11]])
print([blognames[r] for r in kcl[12]])
print([blognames[r] for r in kcl[13]])
print([blognames[r] for r in kcl[14]])
print([blognames[r] for r in kcl[15]])
print([blognames[r] for r in kcl[16]])
print([blognames[r] for r in kcl[17]])
print([blognames[r] for r in kcl[18]])
print([blognames[r] for r in kcl[19]]) #kmod for 20

import pandas as pd
a = {'Name':['sowmya','akhi','nihal'],'Age':[27,39,49]}
b = {'Name':['sivu','karthik','susha'],'Age':[20,40,26]}
a = pd.DataFrame(a)
club = ['ab','cd','ef']
a['As']=club
print(a)

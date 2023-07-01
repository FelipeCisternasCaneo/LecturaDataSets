from Problem.FS.Problem import FeatureSelection as fs

# instancias utilizadas
instancias = ['ionosphere', 'sonar', 'Divorce', 'breast-cancer-wisconsin', 'wdbc']

for instancia in instancias:
    instance = fs(instancia)
    print(instance.getDatos())
    print(instance.getClases())
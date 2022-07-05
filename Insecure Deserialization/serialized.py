import pickle 

class cla:
    def __init__(self, uzumaki, uchiha):
        self.uzumaki = uzumaki 
        self.uchiha = uchiha 
    def descricao(self):
        return "Uzumaki: {}, Uchiha: {}".format(self.uzumaki, self.uchiha)
    
uzumaki1 = cla("naruto", "sasuke")
print(f"objeto - > {uzumaki1}")
print(f"descrição do objeto - > {uzumaki1.descricao()}")

s = pickle.dumps(uzumaki1)
print(f"serialized - >  {s}") 



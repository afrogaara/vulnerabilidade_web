import pickle 

class cla:
    def __init__(self, uzumaki, uchiha):
        self.uzumaki = uzumaki 
        self.uchiha = uchiha 
    def descricao(self):
        return "Uzumaki: {}, Uchiha: {}".format(self.uzumaki, self.uchiha)
   
s = pickle.dumps(uzumaki1)
print(f"serialized - >  {s}") 

d = pickle.loads(s)
print(f"deserialization - >  {d}")
print(f"objeto - > {d.descricao()}")

#serialização 
import pickle
import base64

a = ['joao', 'maria', 'pedro', 'jonas']
serialized = base64.b64encode(pickle.dumps(a)) #- > transforma em base64(objeto) e dps faz a serialização 
print(serialized)

#desserialização
import pickle 
import base64 

data = input(" ")
deserialized = pickle.loads(base64.b64decode(data)) # - > transforma bytes em objeto 
print(deserialized)

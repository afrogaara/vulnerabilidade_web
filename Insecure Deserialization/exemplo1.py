#serialização 
import pickle
import base64

a = ['joao', 'maria', 'pedro', 'jonas']
serialized = base64.b64encode(pickle.dumps(a)) #- > transforma em base64(objeto) e dps faz a serialização 
print(serialized)





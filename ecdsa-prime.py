
from ecdsa import SigningKey, NIST521p
import time
import binascii

#def ecdsaP(message):
message=b'hola que hace'
sk = SigningKey.generate(curve=NIST521p)
vk = sk.verifying_key
i=0
while i<2:
	start= time.time()
	if i==0:
		signature = sk.sign(message)
	elif i==1:
		validator= vk.verify(signature, message)
	end=time.time()
	#Solamente los separo para que no se tome en cuenta la operacion binascci, las impresiones, etc.
	if i==0:
		print('Firma Obtenida:.')
		print(binascii.hexlify(signature))
	elif i==1:
		print('Validacion Realizada.')
		print(validator)
	print('Tiempo de Ejecucion:' + str(end-start)) 
	print('\n')
	i=i+1



	
	
	


	
	
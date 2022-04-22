from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from base64 import b64decode,b64encode
import time





def rsaOAEP(message):
	key = RSA.generate(2048)
	public_key = key.publickey().export_key()
	private_key = key.export_key()
	i=0

	while i < 2 :
		h = SHA256.new(message)
		start= time.time()
		if i ==0 :
			key = RSA.import_key(private_key)
			signature = pss.new(key).sign(h)
			print('Firma Generada:' )
			print(b64encode(signature))
		elif i==1:
			print('Verificacion Realizada.')
			key = RSA.import_key(public_key)
			verifier = pss.new(key)
			verifier.verify(h,signature)
	     	
		end=time.time()
		print('Tiempo de Ejecucion:' + str(end-start)) 
		print('\n')
		i=i+1



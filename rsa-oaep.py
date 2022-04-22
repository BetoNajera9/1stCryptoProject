from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import b64decode,b64encode
import time

def rsaOAEP(message):
	i=0
	key = RSA.generate(2048)
	public_key = key.publickey().export_key()
	private_key = key.export_key()

	while i < 2 :
		start= time.time()
		if i ==0 :
			key = RSA.importKey(public_key)
			cipher = PKCS1_OAEP.new(key)
			ciphertext = cipher.encrypt(message)
			print('Encriptacion:' )
			print(b64encode(ciphertext))

		elif i==1:
			key = RSA.importKey(private_key)
			cipher = PKCS1_OAEP.new(key)
			message = cipher.decrypt(ciphertext)
			print('Decriptacion:' )
			print(message)
		end=time.time()
		print('Tiempo de Ejecucion:' + str(end-start)) 
		print('\n')
		i=i+1




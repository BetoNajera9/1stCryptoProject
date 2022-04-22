from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import time
import binascii


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
		elif i==1:
			key = RSA.importKey(private_key)
			cipher = PKCS1_OAEP.new(key)
			message = cipher.decrypt(ciphertext)
		end=time.time()
		#Solamente los separo para que no se tome en cuenta la operacion binascci, las impresiones, etc.
		if i ==0 :
			print('Encriptacion:' )
			print(binascii.hexlify(ciphertext))
		elif i==1:
			print('Decriptacion:' )
			print(message)
		print('Tiempo de Ejecucion:' + str(end-start)) 
		print('\n')
		i=i+1

	



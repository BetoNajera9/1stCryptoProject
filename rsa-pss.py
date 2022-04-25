from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import timeit
import binascii




def rsaPSS(message):
	print('=======================================================================')
	print('Test RSA-PSS')
	#message=b'hola que hace'
	key = RSA.generate(2048)
	public_key = key.publickey().export_key()
	private_key = key.export_key()
	i=0

	while i < 2 :
		h = SHA256.new(message)
		start= timeit.default_timer()
		if i ==0 :
			key = RSA.import_key(private_key)
			signature = pss.new(key).sign(h)
		elif i==1:
			key = RSA.import_key(public_key)
			verifier = pss.new(key)
			verifier.verify(h,signature)
		end=timeit.default_timer()
		#Solamente los separo para que no se tome en cuenta la operacion binascci, las impresiones, etc.
		if i ==0 :
			print('Firma Generada:' )
			print(binascii.hexlify(signature))
		elif i==1:
			print('Verificacion Realizada.')	
	  
		
		print('Tiempo de Ejecucion:' + str(end-start)) 
		i=i+1


	
	  
		
		print('Tiempo de Ejecucion:' + str(end-start)) 
		print('\n')
		i=i+1
	print('-----------------------------------------------------------------------------')




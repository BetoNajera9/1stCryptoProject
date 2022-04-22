from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import timeit
import binascii

def ecdsaB(message):
	#message=b'hola que hace'
	# Con una curva en el campo binario de 571 bits : SECT571R1 o  NIST B-571
	private_key = ec.generate_private_key( ec.SECT571R1() )
	public_key = private_key.public_key()
	i=0
	while i<2:
		start= timeit.default_timer()
		if i==0:
			signature = private_key.sign( message, ec.ECDSA(hashes.SHA256()) )
		elif i==1:
			public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
		end=timeit.default_timer()
		#Solamente los separo para que no se tome en cuenta la operacion binascci, las impresiones, etc.
		if i==0:
			print('Firma Obtenida:.')
			print(binascii.hexlify(signature))
		elif i==1:
			print('Validacion Realizada.')
			print('TRUE')
		print('Tiempo de Ejecucion:' + str(end-start)) 
		print('\n')
		i=i+1


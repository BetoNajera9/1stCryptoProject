import json
import timeit
from base64 import b64encode
from base64 import b64decode
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import ChaCha20
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def algoritmos(plaintext):
	key = get_random_bytes(32) #Misma llave para todos, de 256 bits
	print('=======================================================================')
	#Chacha20 256 cifrado

	print(f'Chacha20 256 Cifrado')
	start=timeit.default_timer() #Empieza a contar el tiempo
	cipher = ChaCha20.new(key=key)
	ciphertext = cipher.encrypt(plaintext)
	nonce = b64encode(cipher.nonce).decode('utf-8')
	ct = b64encode(ciphertext).decode('utf-8')
	result = json.dumps({'nonce':nonce, 'ciphertext':ct})
	print(ct) #Mostramos solo el texto cifrado
	end=timeit.default_timer() #Termina de contar el tiempo
	print(f'time: {"{:f}".format(end - start)} sec')
	print('=======================================================================')
	#Chacha20 256 Descifrado

	print(f'Chacha20 256 Descifrado')
	start=timeit.default_timer() #Empieza a contar el tiempo
	try:
		b64 = json.loads(result)
		nonce = b64decode(b64['nonce'])
		ciphertext = b64decode(b64['ciphertext'])
		cipher = ChaCha20.new(key=key, nonce=nonce)
		plaintext = cipher.decrypt(ciphertext)
		print(plaintext)
	except (ValueError, KeyError):
		print("Incorrect decryption")
	end=timeit.default_timer() #Termina de contar el tiempo
	print(f'time: {"{:f}".format(end - start)} sec')
	print('=======================================================================')
	#AES-EBC 256 Cifrado

	print(f'AES-EBC 256 Cifrado')
	start=timeit.default_timer() #Empieza a contar el tiempo
	cipher = AES.new(key, AES.MODE_ECB)
	ciphertext=cipher.encrypt(pad(plaintext,16))
	fmt= '{:02X}' * len(ciphertext)
	print(fmt.format(*ciphertext)) #Mostramos solo el texto cifrado
	end=timeit.default_timer() #Termina de contar el tiempo
	print(f'time: {"{:f}".format(end - start)} sec')
	print('=======================================================================')
	#AES-EBC 256 Descifrado

	print(f'AES-EBC 256 Descifrado')
	start=timeit.default_timer() #Empieza a contar el tiempo
	decipher = AES.new(key, AES.MODE_ECB)
	print(decipher.decrypt(ciphertext))
	end=timeit.default_timer() #Termina de contar el tiempo
	print(f'time: {"{:f}".format(end - start)} sec')
	print('=======================================================================')
	#AES-GCM 256 Cifrado

	print(f'AES-GCM 256 Cifrado')
	header = b"header"
	start=timeit.default_timer() #Empieza a contar el tiempo
	cipher = AES.new(key, AES.MODE_GCM)
	cipher.update(header)
	ciphertext, tag = cipher.encrypt_and_digest(plaintext)
	json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
	json_v = [ b64encode(x).decode('utf-8') for x in [cipher.nonce, header, ciphertext, tag ]]
	result = json.dumps(dict(zip(json_k, json_v)))
	fmt= '{:02X}' * len(ciphertext)
	print(fmt.format(*ciphertext)) #Mostramos solo el texto cifrado
	end=timeit.default_timer() #Termina de contar el tiempo
	print(f'time: {"{:f}".format(end - start)} sec')
	print('=======================================================================')
	#AES-GCM 256 Descifrado

	print(f'AES-GCM 256 Descifrado')
	start=timeit.default_timer() #Empieza a contar el tiempo
	try:
		b64 = json.loads(result)
		json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
		jv = {k:b64decode(b64[k]) for k in json_k}

		cipher = AES.new(key, AES.MODE_GCM, nonce=jv['nonce'])
		cipher.update(jv['header'])
		plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
		print(plaintext)
	except (ValueError, KeyError):
		print("Incorrect decryption")
	end=timeit.default_timer() #Termina de contar el tiempo
	print(f'time: {"{:f}".format(end - start)} sec')

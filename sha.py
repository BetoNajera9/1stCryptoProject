import hashlib
import time

def compare(string, real):
  if string == real:
    return True
  else:
    return False

string = b'Nobody inspects'

print(f'Test HASHING')
print(f"String: {string.decode('UTF-8')}")

print('=======================================================================')
#SHA-2 384
print(f'SHA-2 384')

start = time.time()
sha_2_384 = hashlib.sha384()
sha_2_384.update(string)
print(f'string: {sha_2_384.hexdigest()}')
end = time.time()

print(f'time: {"{:f}".format(end - start)} sec')


print('=======================================================================')
#SHA-2 512
print(f'SHA-2 512')

start = time.time()
sha_2_512 = hashlib.sha512()
sha_2_512.update(string)
print(f'string: {sha_2_512.hexdigest()}')
end = time.time()

print(f'time: {"{:f}".format(end - start)} sec')

print('=======================================================================')
#SHA-3 384
print(f'SHA-3 384')

start = time.time()
sha_3_384 = hashlib.sha3_384()
sha_3_384.update(string)
print(f'string: {sha_3_384.hexdigest()}')
end = time.time()

print(f'time: {"{:f}".format(end - start)} sec')

print('=======================================================================')
#SHA-3 512
print(f'SHA-3 512')

start = time.time()
sha_3_512 = hashlib.sha3_512()
sha_3_512.update(string)
print(f'string: {sha_3_512.hexdigest()}')
end = time.time()

print(f'time: {"{:f}".format(end - start)} sec')
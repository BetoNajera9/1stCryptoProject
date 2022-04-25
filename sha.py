import hashlib
import timeit

def compare(string, real):
  if string == real:
    return True
  else:
    return False

def main(string):

  print('=======================================================================')
  #SHA-2 384
  print(f'SHA-2 384')
  data=[]

  start = timeit.default_timer()
  sha_2_384 = hashlib.sha384()
  sha_2_384.update(string)
  print(f'string: {sha_2_384.hexdigest()}')
  end = timeit.default_timer()
  
  print(f'time: {"{:f}".format(end - start)} sec')
  data.append(str(end - start)) 

  print('=======================================================================')
  #SHA-2 512
  print(f'SHA-2 512')

  start = timeit.default_timer()
  sha_2_512 = hashlib.sha512()
  sha_2_512.update(string)
  print(f'string: {sha_2_512.hexdigest()}')
  end = timeit.default_timer()

  print(f'time: {"{:f}".format(end - start)} sec')
  data.append(str(end - start)) 

  print('=======================================================================')
  #SHA-3 384
  print(f'SHA-3 384')

  start = timeit.default_timer()
  sha_3_384 = hashlib.sha3_384()
  sha_3_384.update(string)
  print(f'string: {sha_3_384.hexdigest()}')
  end = timeit.default_timer()

  print(f'time: {"{:f}".format(end - start)} sec')
  data.append(str(end - start)) 

  print('=======================================================================')
  #SHA-3 512
  print(f'SHA-3 512')

  start = timeit.default_timer()
  sha_3_512 = hashlib.sha3_512()
  sha_3_512.update(string)
  print(f'string: {sha_3_512.hexdigest()}')
  end = timeit.default_timer()

  print(f'time: {"{:f}".format(end - start)} sec')
  data.append(str(end - start)) 

  return data

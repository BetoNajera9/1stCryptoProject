import subprocess
import random, string

def run(*popenargs, **kwargs):
    input = kwargs.pop("input", None)
    check = kwargs.pop("handle", False)

    if input is not None:
        if 'stdin' in kwargs:
            raise ValueError('stdin and input arguments may not both be used.')
        kwargs['stdin'] = subprocess.PIPE

    process = subprocess.Popen(*popenargs, **kwargs)
    try:
        stdout, stderr = process.communicate(input)
    except:
        process.kill()
        process.wait()
        raise
    retcode = process.poll()
    if check and retcode:
        raise subprocess.CalledProcessError(
            retcode, process.args, output=stdout, stderr=stderr)
    return retcode, stdout, stderr

def installLibraries():
  try:
    run(['pip', '--version'])
    run(['pip', 'install', 'pycryptodome'])
    run(['pip', 'install', 'cryptography'])
  except:
    try:
      run(['pip3', '--version'])
      run(['pip3', 'install', 'pycryptodome'])
      run(['pip3', 'install', 'cryptography'])
    except:
      print('We need install pip or install next libraries')
      print('-> hashlib')
      print('-> pycryptodome')

def createString(length):
  str = random.sample(string.ascii_letters, length)
  return ''.join(str)



def main():
  # try:
  import chachaes
  import sha
  rsa_oae = __import__('rsa-oaep')
  rsa_pss = __import__('rsa-pss')
  ecdsa_prime = __import__('ecdsa-prime')
  ecdsa_binary = __import__('ecdsa-binary')

  strs = []

  # Variables para el numero de strings y el tamaño de los strings
  print('Se realizan 10 preubas a la vez')
  lengthString=input('De una longitud para el tamano de vector que se quiera probar: ')
  lengthString=int(lengthString)
  numberStrings=10
  n=1

  for x in range(numberStrings):
    strs.append(createString(lengthString))

  for i in strs:
    print('Prueba ' + str(n))
    print('String de prueba' + str(bytes(i, 'utf-8')))
    chachaes.algoritmos(bytes(i, 'utf-8'))
    sha.main(bytes(i, 'utf-8'))
    rsa_oae.rsaOAEP(bytes(i, 'utf-8'))
    rsa_pss.rsaPSS(bytes(i, 'utf-8'))
    ecdsa_prime.ecdsaP(bytes(i, 'utf-8'))
    ecdsa_binary.ecdsaB(bytes(i, 'utf-8'))
    print('\n') 
    n=n+1

  # except Exception as e:
  #   print(e)
  #   installLibraries()
  #   print('Run it again!!!!!')

main()

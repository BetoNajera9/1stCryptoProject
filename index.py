import subprocess

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
  except:
    try:
      run(['pip3', '--version'])
      run(['pip3', 'install', 'pycryptodome'])
    except:
      print('We need install pip or install next libraries')
      print('-> hashlib')
      print('-> pycryptodome')

def main():
  try:
    import chachaes
    import sha

    chachaes.algoritmos()
    sha.main()

  except:
    installLibraries()
    print('Run it again!!!!!')

main()
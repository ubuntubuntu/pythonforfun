import subprocess
process = subprocess.run(('ls','-la'),stdout = subprocess.PIPE)
print(process.stdout.decode("utf-8"))
print("\n\n")

try:
    process = subprocess.run(('find','/usr','-iname','bin'), stdout= subprocess.PIPE, check = True)
    print(process.stdout.decode("utf-8"))
except subprocess.CalledProcessError as error:
    print('Error:', error)
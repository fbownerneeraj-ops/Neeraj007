import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x Neerajfb')
    os.system('./Neerajfb')
elif bit == '32bit':
    os.system('chmod +x Neerajfb32')
    os.system('./Neerajfb32')
else:
    print('device not supported')

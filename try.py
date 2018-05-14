import subprocess
import math
s = "l"
try:
    result = subprocess.call(s, shell=True)
except subprocess.CalledProcessError:
    print("hhhhh")
# if math.isnan(result) == False:
#     print('Received from server: ' + s)
# elif result.find(" not ") or result.find(" no ") != -1:
#    print('Received from server: ' + s)
# else:
#    print("i")
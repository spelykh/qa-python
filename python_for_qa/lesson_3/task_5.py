__author__ = 'Stepan_Pelykh'

import os


home_dir = 'task_5'
for i in range(1,7):
    path = home_dir + '/lesson'+str(i)
    if not os.path.exists(path):
        os.makedirs(path)

    for j in range(1,7):
        filename = path + '/task' + str(j) + '.py'
        open(filename, 'a').close()
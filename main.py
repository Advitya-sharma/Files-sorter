import os 
import shutil

def image_mover(path,file):
    
    if os.path.exists(path+'\\'+'Images'):
        shutil.move(path+'\\'+file, path+'\\'+'Images'+'\\'+file)
    else: 
        os.mkdir(path+'\\'+'Images')
        shutil.move(path+'\\'+file, path+'\\'+'Images'+'\\'+file)

path ='C:\\Users\\Advitya\\Downloads'

list = os.listdir(path)
images = ['jpg','gif','png']

for file in list: 
    name, ext = os.path.splitext(file) 
    ext = ext[1:]
    print(ext,'\n')
    if ext == '': 
        continue
    
    if ext in images:
        image_mover(path,file)
        
       
    elif os.path.exists(path+'\\'+ext): 
       shutil.move(path+'\\'+file, path+'\\'+ext+'\\'+file) 


    else: 
        os.mkdir(path+'\\'+ext)
        print(path+'\\'+file, path+'\\'+ext+'\\'+file,'\n')
        shutil.move(path+'\\'+file, path+'\\'+ext+'\\'+file) 

import pyexiv2 as pe
import os
print(pe.__file__)


def read_directory():
    array_img = [] 
    for filename in os.listdir(r"./"):
        if filename.endswith(r".jpg") or filename.endswith(r".png"): 
            array_img.append(filename)  
    return array_img
    
def print_img():
    file_name = read_directory()
    text = ''
    if file_name:
        for i in file_name:
            text += i
            text += ' '
    
    if file_name:
        print("Scanned image:{0}".format(text))
    else:
        print("Scanned image:NO FOUND!")

print_img()
file = read_directory()
if file:
    print(file)
try:
    for name in file:
        img = pe.Image(name,encoding='utf-8')
        pe.registerNs('http://ns.google.com/photos/1.0/panorama/','Gpano')
        dict = {'Xmp.GPano.UsePanoramaViewer':'True',
                'Xmp.Gpano.ProjectionType':'equirectangular',
                'Xmp.Gpano.PoseHeadingDegrees':'180.0'
                }
        img.modify_xmp(dict)
        print("Sucess!") 
except RuntimeError:
    print("Convert Error.Check file name.Cant use Chinese.")

       






os.system("pause")

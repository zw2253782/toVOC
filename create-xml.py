
import shutil
from PIL import Image
import os
from os import walk
from glob import glob
from PIL import Image

folder = glob("C:/Users/A9F9HZZ/Documents/dlModel/yolo3/toVOC-master/toVOC-master/data/JPEGImages/*/")

for x in folder:
    changeFolder = x.replace("C:/Users/A9F9HZZ/Documents/dlModel/yolo3/toVOC-master/toVOC-master/data/JPEGImages/","")
    changeFolder = changeFolder.replace("/","")
    print(changeFolder)
    folderDir = x #"C:/Users/A9F9HZZ/Documents/dlModel/yolo3/toVOC-master/toVOC-master/data/JPEGImages/"+changeFolder+ "/"
    #C:\Users\A9F9HZZ\Documents\dlModel\yolo3\toVOC-master\toVOC-master\data\JPEGImages
    f = []
    for (dirpath, dirnames, filenames) in walk(folderDir):
            # if (len(f) < 3):
        f.extend(filenames)
    
    #eg = open('img1.xml','r')
    #first = eg.read(1)
    #if not first:
    #    print('friendsfile is empty')
    #else:
    for i in f:
        im = Image.open(folderDir + i)
        head, tail = os.path.split(i)
        basename, file_extension = os.path.splitext(tail)
        new = basename + '.xml'
        
        data = open(new, 'w+')
        imageSize = im.size
        #print(basename)
        #print(imageSize)
        #print(eg)
        #print(eg.readlines())
        eg = open('img1.xml','r')
        for line in eg.readlines():
            #print(line)
            #print(str(folderDir + i))
            #data.write(line)
            if "E:/uwm/pytorch-yolo-v3-custom/data/JPEGImages/img1.jp" in line:
                line = line.replace("E:/uwm/pytorch-yolo-v3-custom/data/JPEGImages/img1.jpg",str(folderDir + i))
                #print("read")
                data.write(line) 
            elif 'img1.jpg' in line:
                line = line.replace('img1.jpg', str(i))
                data.write(line)   
            elif '<width>' in line:
                line = line.replace(re.findall('\d+',line)[0],str(imageSize[0]))
                data.write(line)
            elif '<height>' in line:
                line = line.replace(re.findall('\d+',line)[0],str(imageSize[1]))
                data.write(line)
            elif '<xmin>' in line:
                line = line.replace(re.findall('\d+',line)[0],str(0))
                data.write(line)
            elif '<ymin>' in line:
                line = line.replace(re.findall('\d+',line)[0],str(0))
                data.write(line)
            elif '<xmax>' in line:
                line = line.replace(re.findall('\d+',line)[0],str(imageSize[0]))
                data.write(line)
            elif '<ymax>' in line:
                line = line.replace(re.findall('\d+',line)[0],str(imageSize[1]))
                data.write(line)
            elif 'person' in line:
                line = line.replace('person', changeFolder)
                data.write(line)   
            else:
                data.write(line)
            #print(line)
        data.close()
    eg.close()

'''
import os
from os import walk
from glob import glob
from PIL import Image



def make_anno():
        line = "<annotation>" + '\n'
        f.write(line)
        line = '\t\t<folder>' + "JPEGImages" + '</folder>' + '\n'
        f.write(line)
        line = '\t\t<filename>' + tail + '</filename>' + '\n'
        f.write(line)
        line = '\t\t<source>\n\t\t<database>Source</database>\n\t</source>\n'
        f.write(line)
        im=Image.open('/home/location/VOCdevkit/newdataset/img/' + tail)
        (width, height) = im.size
        line = '\t<size>\n\t\t<width>'+ str(width) + '</width>\n\t\t<height>' + str(height) + '</height>\n\t'
        line += '\t<depth>Unspecified</depth>\n\t</size>'
        f.write(line)
        line = '\n\t<segmented>Unspecified</segmented>'
        f.write(line)
        ind = 0
        for i in data[zind]["annotations"]:
            line = '\n\t<object>'
            line += '\n\t\t<name>Name</name>\n\t\t<pose>Unspecified</pose>'
            line += '\n\t\t<truncated>Unspecified</truncated>\n\t\t<difficult>Unspecified</difficult>'
            xmin = (data[zind]["annotations"][ind]["x"])
            line += '\n\t\t<bndbox>\n\t\t\t<xmin>' + str(xmin) + '</xmin>'
            ymin = (data[zind]["annotations"][ind]["y"])
            line += '\n\t\t\t<ymin>' + str(ymin) + '</ymin>'
            width = (data[zind]["annotations"][ind]["width"])
            height = (data[zind]["annotations"][ind]["height"])
            xmax = xmin + width
            ymax = ymin + height
            line += '\n\t\t\t<xmax>' + str(xmax) + '</xmax>'
            line += '\n\t\t\t<ymax>' + str(ymax) + '</ymax>'
            line += '\n\t\t</bndbox>'
            line += '\n\t</object>'
            f.write(line)
            ind +=1
            f.close()
        zind +=1

folderDir = "/Users/a9f9hzz/Documents/projects/cygnus/train/c_c/"
folder = glob("/Users/a9f9hzz/Documents/projects/cygnus/train/*/")

# print folder
for i in folder:
    f = []
    for (dirpath, dirnames, filenames) in walk(folderDir):
        # if (len(f) < 3):
        f.extend(filenames)
    # else:
    #    break

    print(len(f))

    # zind = 0
    for z in f:
        # print zind
        filename = z
        # print filename
        head, tail = os.path.split(filename)
        basename, file_extension = os.path.splitext(tail)
        #image size
        im = Image.open(i + z)
        print (im.size)
        #write into xml
        #make_anno(i,z,tail,file_extension)
    # print head
    # print tail
    # print basename
    # print file_extension
    # f = open(basename + '.xml','w')
'''
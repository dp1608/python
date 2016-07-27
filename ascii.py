# -*- coding:utf8 -*-
# 导入处理图片的pillow
from PIL import Image
#导入参数处理
import argparse

#设置参数
parser=argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type=int,default=80)
parser.add_argument('--height',type=int,default=80)

#获取输入参数
args=parser.parse_args()

#定义输入参数
IMG=args.file
OUTPUT=args.output
WIDTH=args.width
HEIGHT=args.height

#字符编码
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#将图片变现从灰度值映射到字符上
def get_char(r,b,g,alpha=256):
    if alpha==0:
        return ''
    length=len(ascii_char)
    gray=int(0.2126*r+0.7152*g+0.0722*b)

    unit=(256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__ =='__main__':
    im=Image.open(IMG)
    im=im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt=""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt+=get_char(*im.getpixel((j,i)))
        txt+='\n'
    print  txt

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w')as f:
            f.write(txt)

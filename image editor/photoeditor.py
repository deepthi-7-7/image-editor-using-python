from PIL import Image,ImageEnhance,ImageFilter
import os

path='D:\projects\image editor\img'
pathOut='D:\projects\image editor\editedimg'

for filename in os.listdir(path):
    img=Image.open(f"{path}/{filename}")
    
    #sharpening and changing to BW
    edit= img.filter(ImageFilter.SHARPEN).convert('L')
    
    #contrast
    factor=1.5
    enhancer=ImageEnhance.Contrast(edit)
    edit=enhancer.enhance(factor)
    
    clean_name=os.path.splitext(filename)[0]
    
    edit.save(f'{pathOut}/{clean_name}_edited.jpg')
    
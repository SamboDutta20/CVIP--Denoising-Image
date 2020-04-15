"""
Denoise Problem
(Due date: Nov. 25, 11:59 P.M., 2019)
The goal of this task is to denoise image using median filter.

Do NOT modify the code provided to you.
Do NOT import ANY library or API besides what has been listed.
Hint: 
Please complete all the functions that are labeled with '#to do'. 
You are suggested to use utils.zero_pad.
"""


import utils
import numpy as np
import json

def median_filter(img):
    """
    Implement median filter on the given image.
    Steps:
    (1) Pad the image with zero to ensure that the output is of the same size as the input image.
    (2) Calculate the filtered image.
    Arg: Input image. 
    Return: Filtered image.
    """
    # TODO: implement this function.
    
    img=utils.zero_pad(img,1,1)
    l_fil=3
    temp=[]
    new=[]
    img_denoise=[]

    for k in range(len(img)-l_fil+1):
        for l in range(len(img[0])-l_fil+1):
            
            for i in range(l_fil):
                for j in range (l_fil):
                    temp.append(img[i+k][j+l])
            temp=sorted(temp)
            med=temp[4]
            temp=[]
            new.append(med)
        img_denoise.append(new)
        new=[]  

    #    return img_denoise     
    img_denoise=np.array(img_denoise)
    img_denoise=img_denoise.astype(np.uint8)
    return img_denoise

def mse(img1, img2):
    """
    Calculate mean square error of two images.
    Arg: Two images to be compared.
    Return: Mean square error.
    """    
    # TODO: implement this function.
    e=0
    for i in range(len(img1)):
        for j in range(len(img1[0])):
            e+=(img1[i][j]-img2[i][j])**2
    
    e=e/(len(img1)*len(img1[0]))
    return e
    

if __name__ == "__main__":
    img = utils.read_image('lenna-noise.png')
    gt = utils.read_image('lenna-denoise.png')

    result = median_filter(img)
    error = mse(gt, result)

    with open('results/task2.json', "w") as file:
        json.dump(error, file)
    utils.write_image(result,'results/task2_result.jpg')





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Import required libraries

from PIL import Image
import numpy as np
import board
import neopixel

def extractROI(image,windowSize):
    
    imWidth, imHeight = image.size
    roiImage = image.resize((windowSize[0],windowSize[1]))

    return roiImage

def discretizeImage(roiImage,noLevels):

    image=np.array(roiImage)#Image.fromarray(roiImage,'RGB')
    normalizedImage=image/255
    discretizedImage=np.floor(normalizedImage*noLevels).astype(int)
    multiplier=255/noLevels
    discretizedImage=np.floor(discretizedImage*multiplier).astype(np.uint8) #Rescale to range 0-255
    return discretizedImage

def imageToLED(discreteImageRaw,pixels):
    
    discreteImageR=discreteImageRaw[:,:,0]
    discreteImageG=discreteImageRaw[:,:,1]
    discreteImageB=discreteImageRaw[:,:,2]
    discreteImageR=discreteImageR.flatten()
    discreteImageG=discreteImageG.flatten()
    discreteImageB=discreteImageB.flatten()
    pixelArray=np.zeros((len(discreteImageR),3))
    pixelArray[:,0]=discreteImageR
    pixelArray[:,1]=discreteImageG
    pixelArray[:,2]=discreteImageB
    pixelArray=(pixelArray).astype(int)# Convert to int
    pixelTuple=[tuple(x) for x in pixelArray] #Convert to correctly dimensioned tuple array
    pixels[:]=pixelTuple
        
    return pixels
    
#Parameters
noLevels=255 #No of LED brightness discretization levels
numNeopixels_x = 24 #Declare number of Neopixels in grid
numNeopixels_y = 24
windowSize=(numNeopixels_x,numNeopixels_y) #Define extracted ROI size

pixelPin=board.D18
numPixels=numNeopixels_x*numNeopixels_y
colorOrder = neopixel.GRB
pixels = neopixel.NeoPixel(pixelPin, numPixels, auto_write=False, pixel_order=colorOrder)

while 1:
    newImage = Image.open('yoshi.png')
    newImageROI = extractROI(newImage,windowSize) #Extract base image ROI
    discretizedImage=discretizeImage(newImageROI,noLevels) #Discretize image and scale values   
    pixels=imageToLED(discretizedImage,pixels) #Convert the image to an LED value array and assign them to the string of Neopixels
    pixels.show() #Light up the LEDs
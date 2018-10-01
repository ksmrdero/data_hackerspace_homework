#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

#Method: convert every time to number - 01:29 --> 129
#        place into corresponding bin.

def histogram_times(filename):
    with open(filename + ".csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            data.append(row)
        data = np.array(data)
        time = data[:,1] #time outputs of data
        time = [var for var in time if var] #removes empty values, taken from stackoverflow
        numData = []
        
        for i in time:
             noSpace = i.replace(":", "").replace(" ", "") #removes whitespace and colon
             try:
                 numTime = int(noSpace) #converts string number to int
             except: # edge case: if there are characters that are not numbers, remove them
                 for char in noSpace:
                     if(char.isdigit() == False):
                         noSpace = noSpace.replace(char,"")
                         
                 numTime = int(noSpace)   
             numData.append(numTime)
        
        bins = [0] * 24
        for number in numData:
            if (number > 2400 or number < 0):
                continue
            start = -1
            while start < number:
                start += 100
            bins[int(start / 100)] = bins[int(start / 100)] + 1
        return(bins)

        


def weigh_pokemons(filename, weight):
    with open(filename + ".json") as f:
        data = json.load(f)
        weights = []
        names = []
        for p in data['pokemon']:
            weights.append(p['weight'])
            names.append(p['name'])
        
        numWeights = []
        for w in weights:
            for char in w:
                if(char.isdigit() == False and char != '.'):
                    w = w.replace(char,"")
            numW = float(w)
            numWeights.append(numW)
        index = [i for i, x in enumerate(numWeights) if x == weight]
        
        output = []
        for i in index:
            output.append(names[i])
            
        return(output)



def single_type_candy_count(filename):
    with open(filename + ".json") as f:
        data = json.load(f)
        candy = []
        for p in data['pokemon']:
            if(len(p['type']) == 1):
                try:
                    candy.append(p['candy_count'])
                except:
                    candy.append(0)
        
        sum = 0
        for i in candy:
            sum += i
        return(sum)



def reflections_and_projections(points):
    for i in range(0,len(points[1])):
        points[1][i] = 2 - points[1][i] #reflect across y = 1
     
    t = np.pi/2
    rotate = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    rotateM = np.matmul(rotate,points) #rotates pi/2 radians
     
    m = 3
    proj = np.array([[1, m], [m, m**2]])
    projM = np.divide(np.matmul(proj, rotateM), (m**2 + 1))
    return(projM)



def normalize(image):
    theMax = np.amax(image)
    theMin = np.amin(image)

    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            image[i][j] = float((255 * (image[i][j] - theMin)) / (theMax - theMin))
    
    return(image)

def sigmoid_normalize(image, a):
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            image[i][j] = 255 * ((1 + np.exp((image[i][j] - 128) / (-a))) ** (-1))
    return(image)
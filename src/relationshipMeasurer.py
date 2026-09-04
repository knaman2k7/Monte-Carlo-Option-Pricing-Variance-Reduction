import numpy as np

def calculateRelationship(x,y):

    codedX = np.log(x)
    codedY = np.log(y)

    Sxx = np.sum(codedX**2) - ( (np.sum(codedX)**2) / len(x) )
    Syy = np.sum(codedY**2) - ( (np.sum(codedY)**2) / len(x) )
    Sxy = np.sum(codedX*codedY) - ( (np.sum(codedX)*np.sum(codedY)) / len(x) )

    r = Sxy/np.sqrt(Sxx*Syy)

    # for y = a * x^b
    b = (Sxy/Sxx)
    a = np.exp( np.mean(codedY) - np.mean(codedX) * b )

    return [a,b,r]
    

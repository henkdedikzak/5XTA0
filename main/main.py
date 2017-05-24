import random
import sys
import os


#one object from hamming class contains G,  P and the combination of both
class hamming:
    def __init__(self, input):
        print("new hamming object made")
        self.__G = input
        self.__P = hamming.set_P(self, input)
        self.__H = hamming.set_H(self, self.__G, self.__P)

    #compute P
    def set_P(self, input):
        return [(input[0] + input[1] + input[3] + input[4] + input[6]) % 2, (input[0] + input[2] + input[3] + input[5] + input[6]) % 2, (input[1] + input[2] + input[3]) % 2, (input[4] + input[5] + input[6]) % 2]

    #build the 11 long bit-string that would be sent over a channel
    def set_H(self, G, P):
        return [P[0], P[1], G[0], P[2], G[1], G[2], G[3], P[3], G[4], G[5], G[6]]

    #TODO def addnoise(self, H):
        #write function that adds random values to bits

    #code that can be run on a Hamming object to retrieve the original 7 bits
    def retrievecode(self, received):
        error = hamming.errorChecker(self, received)
        __Hcorrected = received
        for i in range (0, 3):
            #if one of the array elements of error is not equal to zero, there is an error that needs to be replaced
            if error[i] == 1:
                print("error detected")
                __Hcorrected = hamming.errorCorrection(self, error)
                break
        return [__Hcorrected[2], __Hcorrected[4], __Hcorrected[5], __Hcorrected[6], __Hcorrected[8], __Hcorrected[9], __Hcorrected[10]]

    #check for inconsistencies in teh 11 bits
    def errorChecker(self, H):
        return [((H[0] + H[2] + H[4] + H[6] + H[8] + H[10]) % 2), ((H[1] + H[2] + H[5] + H[6] + H[9] + H[10]) % 2), ((H[3] + H[4] + H[5] + H[6]) % 2), ((H[7] + H[8] + H[9] + H[10]) % 2)]

    #correct the wrong bit
    def errorCorrection(self, H, error):
        errorLocation = error[0] * 2 ^ 0 + error[1] * 2 ^ 1 + error[2] * 2 ^ 2 + error[3] * 2 ^ 3
        H[errorLocation] = (H[errorLocation] + 1) % 2
        return H

    #display a hamming object
    def displayHamming(self):
        print("G: ", self.__G, "P: ", self.__P, "H: ", self.__H)



#make a loop that creates a shit ton of hamming objects
hamming1 = hamming([1, 0, 1, 1, 1, 0, 0])

hammingres = hamming1.retrievecode([1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0])
print(hammingres)
sys.stdout.flush()

hamming1.displayHamming()

#TODO make a large bitstream without the hamming correction
#TODO compare the two results

#TODO implement Golay code
#TODO compare all three
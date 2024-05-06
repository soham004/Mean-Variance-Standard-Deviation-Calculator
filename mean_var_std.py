import numpy as np

def calculate(inputList):
    if len(inputList)==9:
        arrayRaw = np.array(inputList)
        #print(arrayRaw)
        cleanArray = arrayRaw.reshape(3, 3)
        #print(cleanArray)
        requiredDictionary = {
            'mean': [np.mean(cleanArray, axis=0).tolist(), np.mean(cleanArray, axis=1).tolist(), np.mean(cleanArray.flatten())],
          
            'variance': [np.var(cleanArray, axis=0).tolist(), np.var(cleanArray, axis=1).tolist(), np.var(cleanArray.flatten())],
          
            'standard deviation': [np.std(cleanArray, axis=0).tolist(), np.std(cleanArray, axis=1).tolist(), np.std(cleanArray.flatten())],
          
            'max': [np.max(cleanArray, axis=0).tolist(), np.max(cleanArray, axis=1).tolist(), np.max(cleanArray.flatten())],
          
            'min': [np.min(cleanArray, axis=0).tolist(), np.min(cleanArray, axis=1).tolist(), np.min(cleanArray.flatten())],
          
            'sum': [np.sum(cleanArray, axis=0).tolist(), np.sum(cleanArray, axis=1).tolist(), np.sum(cleanArray.flatten())]
            }
    else:
        raise ValueError("List must contain nine numbers.")
    return requiredDictionary

#if __name__ == "__main__":
#    print(calculate([0,1,2,3,4,5,6,7,8]))
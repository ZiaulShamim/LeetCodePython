import numpy as np 

def Score(X,W,b):
    score = None 
    pass


def main():
# Checkpoint for perceptron score
    X = np.array([[1,2,3],[30,5,10]])
    W = np.array([1,-1,2])
    b = 100
    observed = (X*W)
    print(observed)
    #observed = Score(X, W, b)
    # expected = np.array([[105], [145]])
    # assert np.array_equal(expected, observed), "Expected: {}, Observed: {}".format(expected, observed)
    print("Passed checkpoint")

    print("This is the code ")

    if __name__ == "__main__":
        main()
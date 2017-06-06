__author__ = 'Aldous'

import sys, csv, re

from NaiveBayes import NaiveBayes
from KNearestNeighbor import KNearestNeighbor


"""
Inputs:
    python2.7 MyProgram training.csv examples.csv NB/4NN
Outputs:
    One class per line classification. Ex:
    --------
    Yes
    No
    Yes
    --------
Program Order:
    Normalise --> Correlation-Based Feature Selection
    10F Cross Validation --> -->
"""

def read_csv(file_name):

    file_name.replace(' ', '')

    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
        return data

#TODO:
#protect from no params given
def main(argv):

    training_set    = argv[1]
    test_set        = argv[2]
    algorithm       = argv[3]

    training_set    = read_csv(training_set)
    test_set        = read_csv(test_set)

    algorithm = algorithm.upper()

    if algorithm == 'NB':

        nb = NaiveBayes()
        nb.calculate_nb(training_set, test_set)

    else:
        int_match = re.findall('\d*', algorithm)
        if int_match[0] is not None:
            algorithm = algorithm.strip(int_match[0])
            k = int(int_match[0])
        if algorithm == 'NN':
            nn = KNearestNeighbor()
            nn.calculate_knn(training_set, test_set, k)

        exit()


if __name__ == '__main__':

    main(sys.argv)
    exit()
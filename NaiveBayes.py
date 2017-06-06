__author__ = 'Aldous'

import math
# from float import *

"""
    P( H | E ) = P( E | H ) * P( H ) / P( E )
"""
class NaiveBayes():


    """
    Uses probability density function to determine probability - assumes numerical values have a normal distribution

    index       - position of attribute in the list
    attr_value  - target value we are calculating the probability of
    data        - data set (training or test)
    """


    #working - remove whitespaces though
    def get_mean(self, data, attr_index, class_index, class_value):
        rows                = len(data)
        sum                 = 0.0
        class_occurrence    = 0

        for x in range(0, rows):
            if data[x][class_index] == class_value:
                class_occurrence += 1
                attr_value = float(data[x][attr_index])
                sum += attr_value

        mean = sum / class_occurrence

        return mean

    #working
    def get_standard_deviation(self, data, attr_index, class_index, class_value, mean):

        rows = len(data)
        sum = 0.0
        class_occurrence = 0

        for x in range(rows):
            if data[x][class_index] == class_value:
                class_occurrence += 1
                attr_value = float(data[x][attr_index])
                sum += math.pow(attr_value - mean, 2)

        std_dev = math.sqrt(sum / class_occurrence)

        return std_dev


    def probability_density_function(self, attr_value, attr_mean, std):

        n1    = 1 / (std * math.sqrt(2 * math.pi))
        n2    = - math.pow(attr_value - attr_mean, 2) / (2 * math.pow(std, 2))
        pdf   = n1 * math.exp(n2)

        # pdf = math.pow((1/ std * math.sqrt(2 * math.pi)) * math.e, -(math.pow((attr_value - attr_mean), 2) / 2 * math.pow(std, 2)))

        return pdf


    def get_attribute_occurrences(self, data, index, attr_value):

        rows = len(data)
        occurrences = 0

        for x in range(rows):
            # print data[x][index]
            if data[x][index] == attr_value:
                occurrences += 1

        return occurrences

    """
    index       - position of class in the list
    attr_value  - target value we are calculating the probability of
    data        - data set (training or test)
    """
    def get_class_occurrences(self, data, index, class_value):

        rows = len(data)
        occurrences = 0

        for x in range(rows):
            if data[x][index] == class_value:
                occurrences += 1

        return occurrences


    def probability_formula(self, data, attr_index, attr_value, class_index, class_value):

        mean        = self.get_mean(data, attr_index, class_index, class_value)
        std         = self.get_standard_deviation(data, attr_index, class_index, class_value, mean)
        prob_density    = self.probability_density_function(attr_value, mean, std)

        return prob_density

    """
    Main function
    """

    def naive_bayes(self, data, test, class_value, class_index, rows, line):

        class_occurrences = float(self.get_class_occurrences(data, class_index, class_value))
        class_prob = class_occurrences / float(rows)

        probabilities = []
        product = 1.0
        attr_index = 0

        for attribute in line:
            # print attribute
            # print attr_index
            attr_value = float(attribute)
            probability = self.probability_formula(data, attr_index, attr_value, class_index, class_value)
            probabilities.append(probability)
            product = probability * product
            # print "probabilty: " + str(probability)
            # print "product: " + str(product)
            attr_index += 1
        # product *= class_prob

        # print "pclass : " + str(class_prob)
        nb = product * class_prob

        return nb




    def calculate_nb(self, data, test):

        columns = len(data[0])-1
        rows    = len(data)
        #assumes class is at the end
        class_index = columns
        attributes_n = columns - 1

        for line in test:
            nb_yes = self.naive_bayes(data, test, 'yes', class_index, rows, line)
            nb_no= self.naive_bayes(data, test, 'no', class_index, rows, line)
            # print "prob yes: " +  str(nb_yes) + " | prob no" + str(nb_no)

            if nb_yes > nb_no:
                print 'yes'
            elif nb_yes < nb_no:
                print 'no'
            else:
                print 'yes'


        # mean_yes        = self.get_mean(data, 1, class_index, 'yes')
        # std_yes         = self.get_standard_deviation(data, 1, class_index, 'yes', mean_yes)
        # prob_density    = self.probability_density_function(0.465062, mean_yes, std_yes)

        # print 'mean: ' + str(mean_yes)
        # print 'std: ' + str(std_yes)
        # print 'prob density: ' + str(prob_density)

        test_pdf = self.probability_density_function(66, 73, 6.2)
        # self.probability_density_function(attrvalue,attr_mean,std)
        # print "test pdf: " + str(test_pdf)


        return
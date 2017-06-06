__author__ = 'Aldous'

import math

class KNearestNeighbor():

    columns = None
    rows = None
    class_index = None
    k = 10

    def euclidian_distance(self, test_entry, data_entry):

        ed = 0.0
        distance = 0.0
        for x in range(0, len(test_entry)):
            test_attr_value = float(test_entry[x])
            data_attr_value = float(data_entry[x])
            distance += math.pow((test_attr_value - data_attr_value), 2)

        ed = math.sqrt(distance)

        return ed

    def knn(self, data, test_entry):

        distances = []
        for row in data:
            ed = self.euclidian_distance(test_entry, row)
            ed_entry = {'distance' : ed, 'class' : row[self.class_index]}
            distances.append(ed_entry)
        sorted_distances = sorted(distances, key=lambda k: k['distance'])

        no_count    = 0
        yes_count   = 0
        for x in range(0, self.k):
            if sorted_distances[x]['class'] == 'yes':
                yes_count += 1
            elif sorted_distances[x]['class'] == 'no':
                no_count += 1
        if yes_count >= no_count:
            return 'yes'
        elif yes_count < no_count:
            return 'no'

    def calculate_knn(self, data, test, k):

        self.k = k
        self.columns = len(data[0])-1
        self.rows    = len(data)
        #assumes class is at the end
        self.class_index = self.columns

        for line in test:
            class_prediction = self.knn(data, line)
            if class_prediction == 'yes':
                print 'yes'
            elif class_prediction == 'no':
                print 'no'

        return
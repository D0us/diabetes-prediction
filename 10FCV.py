__author__ = 'Aldous'
import csv, math

"""
Split data into 10 non overlapping sets
for each set, train on others and calculate accuracy and error rate on set
"""
class FCV():

    class_index = None
    columns     = None
    rows        = None

    def read_class(self, data, class_value):

        # class_index = columns

        class_occurences = []
        for line in data:
            if line[self.class_index] == class_value:
                class_occurences.append(line)

        return class_occurences

    def chunks(self, data, n):
        """Yield successive n-sized chunks from data."""
        for i in range(0, len(data), n):
            yield data[i:i + n]

    def divide(self, data, k):

        rows = len(data)


        yes_occ = self.read_class(data, 'yes')
        no_occ = self.read_class(data, 'no')
        print yes_occ
        print no_occ

        yes_occ_rows = len(yes_occ)
        no_occ_rows = len(no_occ)


        fold_min_yes = 0.0
        fold_min_yes  = int(math.floor(yes_occ_rows / k))
        fold_min_yes_remainders = fold_min_yes % k
        fold_min_no = 0.0
        fold_min_no  = int(math.floor(no_occ_rows / k))
        fold_min_no_remainders = fold_min_no % k

        print str(fold_min_yes)
        print str(fold_min_yes_remainders)

        print str(fold_min_no)
        print str(fold_min_no_remainders)

        for entry in yes_occ:
            print entry

        folds = []


        # print current_yes_remainder
        for x in range(0, 10):
            blank = ['fold' + str(x)]
            folds.append(blank)
            for line in range(x * fold_min_yes, x * fold_min_yes + fold_min_yes):
                entry = []
                entry.append(yes_occ[line])
                folds.append(entry)
            for line in range(x * fold_min_no, x * fold_min_no + fold_min_no):
                entry = []
                entry.append(no_occ[line])
                folds.append(entry)

        file_name = 'pima-folds.csv'
        csv_output = open(file_name, 'wb')
        wr = csv.writer(csv_output)
        for line in folds:
            wr.writerow(line)

        return

    def read_csv(self, file_name):

        file_name.replace(' ', '')

        with open(file_name, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            data = list(reader)
            return data


    def main(self):
        file = 'pima.csv'
        data = self.read_csv(file)
        self.columns = len(data[0])-1
        self.class_index = self.columns

        k = 10.0
        self.divide(data, k)


if __name__ == '__main__':
    fcv = FCV()
    fcv.main()
    exit()
import math

def classify_nn(training_filename, testing_filename, k):
    train = open(training_filename, "r")
    x_train = []
    y_train = []
    for row in train:
        row_split = row.split(",")
        num_features = len(row_split) - 1
        x_train.append(row_split[:num_features])
        y_train.append(row_split[-1].rstrip())

    test = open(testing_filename, "r")
    x_test = []
    for row in test:
        row_split = row.split(",")
        x_test.append(row_split)

    output = []
    # Calculate mean and standard deviation for each feature vector
    for row in x_test:
        distances = []
        idx = 0
        for row2 in x_train:
            distance = 0
            for i in range(0, len(row)):
                distance += math.pow(float(row[i]) - float(row2[i]), 2)

            distance = math.sqrt(distance)
            distances.append((distance, y_train[idx]))
            idx += 1

        # Evaluate label
        distances.sort()
        yes_count = 0
        for i in range(0, k):
            if distances[i][1] == "yes":
                yes_count += 1

        no_count = k - yes_count
        if yes_count >= no_count:
            output.append("yes")
        else:
            output.append("no")

    return output





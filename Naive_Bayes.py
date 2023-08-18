import math


def classify_nb(training_filename, testing_filename):
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

    # Count number of yes/no labels
    num_yes = 0
    num_no = 0
    for label in y_train:
        if label == "yes":
            num_yes += 1
        else:
            num_no += 1

    means_y = []
    means_n = []
    # Calculate mean for each feature vector
    num_features = len(x_train[0])
    for i in range(0, num_features):
        yes_total = 0
        no_total = 0
        idx = 0
        for row in x_train:
            if y_train[idx] == "yes":
                yes_total += float(row[i])
            else:
                no_total += float(row[i])
            idx += 1

        mean_y = yes_total / num_yes
        mean_n = no_total / num_no
        means_y.append(mean_y)
        means_n.append(mean_n)

    mean_std_yes = []
    mean_std_no = []
    # Calculate standard  deviation
    for i in range(0, num_features):
        yes_total = 0
        no_total = 0
        idx = 0
        for row in x_train:
            if y_train[idx] == "yes":
                yes_total += math.pow(float(row[i]) - means_y[i], 2)
            else:
                no_total += math.pow(float(row[i]) - means_n[i], 2)
            idx += 1

        yes_std = math.sqrt(yes_total / (num_yes - 1))
        no_std = math.sqrt(no_total / (num_no - 1))
        mean_std_yes.append(yes_std)
        mean_std_no.append(no_std)

    output = []
    for row in x_test:
        probability_y = num_yes / (num_yes + num_no)
        probability_n = num_no / (num_yes + num_no)

        for i in range(0, num_features):
            probability_y *= 1 / (mean_std_yes[i] * math.sqrt(2 * math.pi)) * math.pow(math.e, -(
                math.pow(float(row[i]) - means_y[i], 2)) / (2 * math.pow(mean_std_yes[i], 2)))
            probability_n *= 1 / (mean_std_no[i] * math.sqrt(2 * math.pi)) * math.pow(math.e, -(
                math.pow(float(row[i]) - means_n[i], 2)) / (2 * math.pow(mean_std_no[i], 2)))

        if probability_y >= probability_n:
            output.append("yes")
        else:
            output.append("no")

    return output

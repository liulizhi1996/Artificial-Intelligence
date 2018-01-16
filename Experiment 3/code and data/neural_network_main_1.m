clc; clear;

data = [[1 0];
        [0 0];
        [0 1];
        [1 1]];
output = [0; 1; 0; 1];
nlevel = 2;
nneuron = [2, 1];
study_rate = 0.9;
threshold = 0.05;
max_iter = 5000;

W = neural_network_train(data, output, nlevel, nneuron, study_rate, ...
    threshold, max_iter);
accuracy = neural_network_test(data, output, nlevel, nneuron, W);
fprintf('accuracy: %f\n', accuracy);

% dataset: http://archive.ics.uci.edu/ml/datasets/Iris
clc; clear;

load iris.mat

average = mean(fea);
standard_deviation = std(fea);
fea = (fea - average .* ones(size(fea))) ./ ...
    (standard_deviation .* ones(size(fea)));

nlevel = 2;
nneuron = [5, 1];
study_rate = 0.01;
threshold = 0.01;
max_iter = 1000;

W = cell(3, 1);
train_data = fea(1:2:end, :);
train_output = gnd(1:2:end, :);
for i = 1:3
    data = train_data;
    output = train_output;
    output(output == i) = 1;
    output(output ~= i) = 0;
    fprintf('class %d\n', i);
    W{i} = neural_network_train(data, output, nlevel, nneuron, ...
        study_rate, threshold, max_iter);
end

test_data = fea(2:2:end, :);
test_output = gnd(2:2:end, :);
accuracy = neural_network_test_multi(test_data, test_output, nlevel, ...
    nneuron, W);
fprintf('accuracy: %f\n', accuracy);

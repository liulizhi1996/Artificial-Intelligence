clc; clear;

load ORL_32x32.mat

fea = fea ./ 256;

nlevel = 3;
nneuron = [15, 5, 1];
study_rate = 0.1;
threshold = 0.01;
max_iter = 100;

rng('shuffle');
idx = randperm(size(fea, 1));
fea = fea(idx, :);
gnd = gnd(idx, :);

W = cell(40, 1);
train_data = fea(1:2:end, :);
train_output = gnd(1:2:end, :);
for i = 1:40
    data = train_data;
    output = (train_output == i);
    fprintf('class %d\n', i);
    W{i} = neural_network_train(data, output, nlevel, nneuron, ...
        study_rate, threshold, max_iter);
end

test_data = fea(2:2:end, :);
test_output = gnd(2:2:end, :);
accuracy = neural_network_test_multi(test_data, test_output, nlevel, ...
    nneuron, W);
fprintf('accuracy: %f\n', accuracy);

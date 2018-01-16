% dataset: http://archive.ics.uci.edu/ml/datasets/Blood+Transfusion+Service+Center
clc; clear;

load transfusion.mat;
nlevel = 2;
nneuron = [5, 1];
study_rate = 1.1;
threshold = 0.1;
max_iter = 100;

data_size = size(data, 1);
rng('shuffle');
idx = randperm(data_size);
sample_size = round(data_size / 10);
accuracy = zeros(1, 10);
for i = 1:10
    if i < 10
        sample_data = data([idx(1:(i-1)*sample_size),idx((i*sample_size+1):end)], :);
        sample_output = output([idx(1:(i-1)*sample_size),idx((i*sample_size+1):end)], :);
        test_data = data(idx(((i-1)*sample_size+1):(i*sample_size)), :);
        test_output = output(idx(((i-1)*sample_size+1):(i*sample_size)), :);
    else
        sample_data = data(idx(1:9*sample_size), :);
        sample_output = output(idx(1:9*sample_size), :);
        test_data = data(idx((9*sample_size+1):end), :);
        test_output = output(idx((9*sample_size+1):end), :);
    end
    W = neural_network_train(sample_data, sample_output, nlevel, ...
        nneuron, study_rate, threshold, max_iter);
    accuracy(i) = neural_network_test(test_data, test_output, nlevel, ...
        nneuron, W);
end
for i = 1:10
    fprintf('accuracy: %f\n', accuracy(i));
end
fprintf('average accuracy: %f\n', mean(accuracy));

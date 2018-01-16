% dataset: http://archive.ics.uci.edu/ml/datasets/Diabetic+Retinopathy+Debrecen+Data+Set
clc; clear;

load messidor_features.mat
average = mean(data);
standard_deviation = std(data);
normalized = (data - average .* ones(size(data))) ./ ...
    (standard_deviation .* ones(size(data)));

nlevel = 2;
nneuron = [6, 1];
study_rate = 1.2;
threshold = 0.08;
max_iter = 2000;

normalized_size = size(normalized, 1);
rng('shuffle');
idx = randperm(normalized_size);
sample_size = round(normalized_size / 10);
accuracy = zeros(1, 10);
for i = 1:10
    if i < 10
        sample_data = normalized([idx(1:(i-1)*sample_size),idx((i*sample_size+1):end)], :);
        sample_output = output([idx(1:(i-1)*sample_size),idx((i*sample_size+1):end)], :);
        test_data = normalized(idx(((i-1)*sample_size+1):(i*sample_size)), :);
        test_output = output(idx(((i-1)*sample_size+1):(i*sample_size)), :);
    else
        sample_data = normalized(idx(1:9*sample_size), :);
        sample_output = output(idx(1:9*sample_size), :);
        test_data = normalized(idx((9*sample_size+1):end), :);
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

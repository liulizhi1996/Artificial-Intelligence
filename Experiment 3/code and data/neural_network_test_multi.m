function accuracy = neural_network_test_multi(data, output, nlevel, nneuron, Ws)
%NEURAL_NETWORK_TEST_MULTI Compute accuracy of neural network on experiment 
%data set.
% data: data set, it's a m-by-n matrix, which has m samples, 
%       and n attributes each sample. 
% output: expected output response, it's a m-by-1 vector, 
%         each row represents one response of corresponding sample.
% nlevel: the level of neural network.
% nneuron: the number of sigmoid neurones of each level, it's 1-by-nlevel
%          vector, and the last element is 1.
% Ws: weights, it's a nclass-by-1 cell vector, each entry is an 1-by-nlevel 
%     cell vector, the j-th element is also an 1-by-nneuron(j) cell vector, 
%     and the i-th element is still an 1*(nneuron(j-1)+1) cell vector.
% threshold: training threshold.
    correct = 0;
    nclass = size(Ws, 1);
    real_output = zeros(1, nclass);
    for d = 1:size(data, 1)
        X0 = [data(d, :), 1];
        for c = 1:nclass
            W = Ws{c};
            for j = 1:nlevel
                f = zeros(1, nneuron(j));
                for i = 1:nneuron(j)
                    if j == 1
                        s = X0 * W{j}{i}';
                    else
                        s = [old_f, 1] * W{j}{i}';
                    end
                    f(i) = sigmoid(s);
                end
                old_f = f;
            end
            real_output(c) = f;
        end
        except = output(d);
        [~, test_output] = max(real_output, [], 2);
        if test_output == except
            correct = correct + 1;
        end
    end
    accuracy = correct / size(data, 1);
end


function f = sigmoid(s)
%SIGMOID Compute sigmoid function at s.
    f = 1 ./ (1 + exp(-s));
end

function W = neural_network_train(data, output, nlevel, nneuron, ...
    study_rate, threshold, max_iter)
%NEURAL_NETWORK_TRAIN Train BP nerual network using the supplied data set.
% data: data set, it's a m-by-n matrix, which has m samples, 
%       and n attributes each sample. 
% output: expected output response, it's a m-by-1 vector, 
%         each row represents one response of corresponding sample.
% nlevel: the level of neural network.
% nneuron: the number of sigmoid neurones of each level, it's 1-by-nlevel
%          vector, and the last element is 1.
% study_rate: study rate.
% threshold: training threshold.
% max_iter: maximum iteration number.
% W: weights, it's a 1-by-nlevel cell vector, the j-th element is also a
%    1-by-nneuron(j) cell vector, and the i-th element is still a
%    1*(nneuron(j-1)+1) cell vector.
    
    % initialization
    sample_number = size(data, 1);
    W = cell(1, nlevel);
    f = cell(1, nlevel);
    delta = cell(1, nlevel);
    for j = 1:nlevel
        W{j} = cell(1, nneuron(j));
        f{j} = zeros(1, nneuron(j));
        delta{j} = zeros(1, nneuron(j));
        for i = 1:nneuron(j)
            if j == 1
                W{j}{i} = rand(1, size(data, 2)+1);
            else
                W{j}{i} = rand(1, nneuron(j-1)+1);
            end
        end
    end

    % train
    for iter = 1:max_iter
        error = 0;
        for d = 1:sample_number
            % feed forward
            X0 = [data(d, :), 1];
            for j = 1:nlevel
                for i = 1:nneuron(j)
                    if j == 1
                        s = X0 * W{j}{i}';
                    else
                        s = [f{j-1}, 1] * W{j}{i}';
                    end
                    f{j}(i) = sigmoid(s);
                end
            end

            % back propagation
            expect = output(d);
            delta{nlevel}(1) = (expect - f{nlevel}(1)) * f{nlevel}(1) * ...
                (1 - f{nlevel}(1));
            W{nlevel}{1} = W{nlevel}{1} + study_rate * ...
                delta{nlevel}(1) * [f{nlevel-1}, 1];
            for j = (nlevel-1):-1:1
                for i = 1:nneuron(j)
                    summa = 0;
                    for l = 1:nneuron(j+1)
                        summa = summa + delta{j+1}(l) * W{j+1}{l}(i);
                    end
                    delta{j}(i) = f{j}(i) * (1 - f{j}(i)) * summa;
                    if j == 1
                        W{j}{i} = W{j}{i} + study_rate * delta{j}(i) * ...
                            X0;
                    else
                        W{j}{i} = W{j}{i} + study_rate * delta{j}(i) * ...
                            [f{j-1}, 1];
                    end
                end
            end

            % statistics
            error = error + (f{nlevel}(1) - expect) ^ 2;
        end

        error_rate = error / (2 * sample_number);
        fprintf('error rate: %f\n', error_rate);
        if error_rate <= threshold
            break
        end
    end
end


function f = sigmoid(s)
%SIGMOID Compute sigmoid function at s.
    f = 1 ./ (1 + exp(-s));
end

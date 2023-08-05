import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        # Define the first layer (input layer) with input_size neurons and hidden_size output neurons.
        self.l1 = nn.Linear(input_size, hidden_size)
        
        # Define the second layer (hidden layer) with hidden_size input neurons and hidden_size output neurons.
        self.l2 = nn.Linear(hidden_size, hidden_size)
        
        # Define the third layer (output layer) with hidden_size input neurons and num_classes output neurons.
        self.l3 = nn.Linear(hidden_size, num_classes)
        
        # Define the activation function ReLU (Rectified Linear Unit) to introduce non-linearity.
        self.relu = nn.ReLU()
        
    def forward(self, x):
        # Forward pass of the neural network:
        # The input 'x' is propagated through each layer with the activation function applied after each layer.
        
        # Pass the input through the first layer (input layer).
        out = self.l1(x)
        
        # Apply ReLU activation function to the output of the first layer.
        out = self.relu(out)
        
        # Pass the output of the first layer through the second layer (hidden layer).
        out = self.l2(out)
        
        # Apply ReLU activation function to the output of the second layer.
        out = self.relu(out)
        
        # Pass the output of the second layer through the third layer (output layer).
        out = self.l3(out)
        
        # Note: There is no activation function or softmax applied here as the cross entropy loss function
        # typically handles this as part of the loss computation.
        
        # The final output 'out' represents the predicted scores for each class.
        return out

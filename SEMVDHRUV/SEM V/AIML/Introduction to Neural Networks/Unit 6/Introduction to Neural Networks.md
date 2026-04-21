# Introduction

Neural Networks are also known as Artificial Neural Networks.
meant to biologically mimic human brain
Similar to human brains ANN also have neurons (nodes) that are linked to multiple layers to identify patterns like human brains

#### Function
ANN learn from non-linear and complex relationships between input and output variables.
![[IMG-20251117143944511.png|600]]
#### Components of a Neural Network
1. Neurons: The basic units that receive inputs, each neuron is governed by an activation function and threshold 
2. Synapses: These are the connections between neurons(nodes), these synapses are regulated by weights N 
3. Weights: Is a numeric number that determines the strength between nodes in different layers. Weights determine how much influence does the each node(feature) has on the networks final output. 
4. Biases: Unlike Weights, Biases are not assigned to each node but instead they shift the activation function to better fit the model. Without biases, neurons would only activate only when the input reaches a certain threshold. They allow the model to become more flexible by making enabling activation across wider range of conditions improving models accuracy
5. Propagation Function: Mechanism that helps process and transfer data across layers of neurons. It passes input data through multiple layers to generate an output.
6. Learning Rule: The method that adjusts weight and bias overtime to improve accuracy

#### Applications
1. Forecasting and Marketing Research , Fraud Detection and Risk Assessment in ***Financial Services***
2. Facial recognition, Vehicle recognition for self-driving cars, Content Moderation in ***Computer Vision***
3. Diagnosing diseases and medical images in ***Healthcare Services***
4. Chatbots, Handwriting classification, User Sentiment Classification in ***NLP (Natural Language Processing)***

## Architecture

ANN works on the set of three layers: Input Layer, Hidden Layers, Output Layer

1. Input Layers: This is the layer where the input data is fed to the model. The model here classifies the data points and each neuron in this layer corresponds to a feature in the dataset.
2. Hidden Layers: These set of layers perform most of the computational tasks. A Neural Network can have N numbers of hidden layers. Each hidden layer transforms the input data from the previous layer into something that the output layer can use.
3. Output Layer: The final layer produces output of the model. The format of the model can depend upon the specific task of the model. The Output may consist of multiple nodes like for multi-class classification problem the output layer may consist of multiple nodes.

## Types of Learning in Neural Networks

### Supervised Learning
1. In this type of learning, there is feedback from the environment to the model
2. Loss function is calculated here
3. This loss function is sent back to the network for adjusting the weights
4. All the adjustments are performed until no adjustments can be made.
### Unsupervised Learning
1. There is no feedback from the environment
2. There is no desired output and model learns on its on.
3. Inputs are formed into classes that define the similarity of the members
### Reinforcement Learning
1. There is no exact feedback from the environment, but rather there is critique feedback
2. It is best of both Supervised and Unsupervised Learning.
3. The critique tells us how close our solution is. Hence model learns on its own based on the critique information.
 
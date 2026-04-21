## Defining Supervised Learning
**Goal:** To find a mapping function between the $(x)$ input and $(y)$ output variable.
- type of machine learning algorithms in which the machine learns under supervision
- uses a known
	- **dataset** (called the training dataset) 
	- a **known set of input data** (called features)
	- known responses to make predictions
- To train an algorithm 

It learns the relationship between the input data and the output data.
- The input is called the **Features $x$**
- The output is called the **Target Value $y$** 

```mermaid
flowchart TB

%% --- TRAINING SECTION ---
subgraph TRAINING[Training]
    direction LR

    A["Raw Data<br/>(Train)"] --> B[Feature<br/>Extraction]
    L[Labels] --> B

    B --> FMat((Feature Matrix))
    FMat --> C[Train the<br/>Model]

    C --> M["(Model)"]
    M --> E[Eval<br/>Model]

end

%% --- PREDICTING SECTION ---
subgraph PREDICTING[Predicting]
    direction LR

    N[New Data] --> BX[Feature<br/>Extraction]
    BX --> FVec((Feature Vector))

    FVec --> P[Model<br/>Predict]
    M --> P

    P --> OUT[Labels]
end

%% Divider Line
TRAINING --->|After Training| PREDICTING
```


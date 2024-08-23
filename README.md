
# Model Documentation

[Neptune AI link]( "Model run in Neptune AI")
[Model inference in HEX]( "Model inference in HEX")

1. [Model Overview](#model-overview)
2. [Model Architecture](#model-architecture)
3. [Dataset overview](#dataset)
4. [Train dataset](#training-dataset)
5. [Test dataset](#)
6. [Training procedure]()
    - [Adversarial model](#adversarial-model)
    - [Forward Selection](#forward-selection)
    - [Hyperparameters optimization](#hyperparameters-optimization)
7. [Evaluation]()


## Model Overview  

- **Model Name:** Model churn v.1
- **Model Type:** binary classification
- **Description:** Model curn for Simple app

### Model Architecture  

- **Model Architecture:** 
- **Input Features:** ['feature1', 'feature2']
- **Output Predictions:** target


## Dataset Owerview

- **Data Sourses** [Provide the data sourses used for model training]
- **Data Preprocessing:** [Explain any preprocessing steps performed on the training data]


### Training dataset

- **Dataset Size:** 
- **Number of unique users:**
- **Mean target:** 0.32
- **Time interval:** from  to 
- **Mean target by months:** 

   feature1  feature2  target
0  0.496714  0.417411       1
1 -0.138264  0.222108       0



  
![mean_target](img/mean_target.png)

### Test dataset

- **Dataset Size:** 
- **Number of unique users:**
- **Time interval:**
- **Mean target by months:**

   feature1  feature2  target
0  0.496714  0.417411       1
1 -0.138264  0.222108       0



  
![mean_target](img/mean_target.png)

## Training Procedure

- **Performance Metrics:** [Specify the evaluation metrics used to assess the model's performance]

### Adversarial model
### Forward Selection
### Hyperparameters optimization


## Results and Performance

![roc_auc](img/roc_curve_30.png)
![predict_distribution](img/predict_dist_30.png)
![mean_target](img/mean_target.png)

## References

- [List any relevant papers, articles, or resources related to the model]
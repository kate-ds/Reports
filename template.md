
# Model Documentation

[Neptune AI link]({{neptune_link}} "Model run in Neptune AI")
[Model inference in HEX]({{HEX_link}} "Model inference in HEX")

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

- **Model Name:** {{model_name}}
- **Model Type:** {{model_type}}
- **Description:** {{description}}

### Model Architecture  

- **Model Architecture:** {{model}}
- **Input Features:** {{features}}
- **Output Predictions:** {{target}}


## Dataset Owerview

- **Data Sourses** [Provide the data sourses used for model training]
- **Data Preprocessing:** [Explain any preprocessing steps performed on the training data]


### Training dataset

- **Dataset Size:** {{dataset_size}}
- **Number of unique users:**
- **Mean target:** {{mean_target}}
- **Time interval:** from {{min_date}} to {{max_date}}
- **Mean target by months:** 

{{dataset}}
{{dataset_train}}

{{dataset_mean_target_by_mon}}
  
![mean_target](img/mean_target.png)

### Test dataset

- **Dataset Size:** 
- **Number of unique users:**
- **Time interval:**
- **Mean target by months:**

{{dataset}}
{{dataset_train}}

{{dataset_mean_target_by_mon}}
  
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
## RandomForestClassifier in a Nutshell:

### Model Basis:
- Ensemble of decision trees trained on different data subsets using random feature selections.

### Process:
- **Decision Trees:** Multiple trees trained on random data subsets and features.
- **Randomness:** Introduced through bootstrapping (random dataset sampling with replacement) and random feature selection for node splitting.

### Prediction:
- **Voting/Averaging:** Each tree predicts, and for classification, final prediction is via majority voting; for regression, it's an average of tree predictions.

## Project Overview:

### Dataset:
- Kaggle wine quality prediction (12 attributes).
  
### Visualizations:
- 'seaborn' & 'matplotlib' libraries used for better comprehension.

### Model Development:
- **Initial split:** 80% training, 20% testing.
- **Testing phase:** Achieved ~93% accuracy.
- **Merging:** 20% test data merged back into 80% for complete model training.
- **Validation:** Used new, unseen data for wine quality classification.

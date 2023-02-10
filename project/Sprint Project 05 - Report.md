# Sprint Project 05 - Report

## Executive Summary

This report presents the results of various experiments carried out for training a Resnet50 Convolutional Neural Network for car image classification. The accuracy was used as the performance metric for the models. The best model produced used an Adam optimizer with a learning rate of 0.001, but this resulted in significant overfitting compared to a similar model using SGD as an optimizer with a learning rate of 0.01. The results showed that after 30 epochs, there was no significant learning gain observed.

Data augmentation techniques were applied to increase the diversity of the training dataset and improve model performance. The results showed that when the background of the images was removed, there was a significant improvement in the performance of the model.

In conclusion, this report highlights the importance of selecting the right optimization algorithms and using data augmentation techniques to improve the performance of machine learning models for car image classification. Further experimentation is recommended to improve the performance of the models and reduce overfitting.

---

## Experiments

<aside>
💡 · 🟠 Is **training set**
· 🔵 Is **validation set**

</aside>

### Expemient nº1

- **Technical Specifications**
    
    
    | Optimizer | Adam |
    | --- | --- |
    | Learn. Rate | 0.001 |
    | Cropped images | No |
    | Epochs | 35 |
    | Batch Size | 32 |
    | Loss function | Cross Entropy |
    | Performance Metric | Accuracy |
    | Data augmentation techniques | Random flip; random rotation |
    | CNN model trainable layers | Last 10 |
- **Experiment report**
    
    ![Figure 1.1 - Epochs vs. Accuracy for train and validation](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-09_a_la(s)_17.15.25.png)
    
    Figure 1.1 - Epochs vs. Accuracy for train and validation
    
    What we can see in **figure 1.1** is that after training 35 epochs we experience a high overfitting for training data. This is visually experienced comparing the high accuracy for the training curve and low considerably big gap with the validation accuracy.
    
    ![Figure 1.2 Epochs vs. Loss function](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-09_a_la(s)_17.19.14.png)
    
    Figure 1.2 Epochs vs. Loss function
    
    What we can see in **figure 1.2** is that after epoch 10, the loss function steadily starts to increase in validation set while training sets keeps going down. Another proof of which is another proof of overfitting.
    
    <aside>
    ⚠️ The model evaluation throughs a 39.83% of accuracy for the test set. Not good enough.
    
    </aside>
    
- **Experiment conclusions**
    
    Although while training we have got a high accuracy, evidence shows that the model is highly overfitting. It is not the best model to select and put eventually in production.
    

---

### Expemient nº2

- **Technical Specifications**
    
    
    | Optimizer | Stochastic Gradient Descent |
    | --- | --- |
    | Learn. Rate | 0.001 |
    | Cropped images | No |
    | Epochs | 35 |
    | Batch Size | 32 |
    | Loss function | Cross Entropy |
    | Performance Metric | Accuracy |
    | Data augmentation techniques | Random flip; random rotation |
    | CNN model trainable layers | Last 10 |
- **Experiment report**
    
    ![Figure 2.1 Epochs vs. Accuracy](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-09_a_la(s)_18.03.42.png)
    
    Figure 2.1 Epochs vs. Accuracy
    
    What we can see in **figure 2.1** is that after training 35 epochs we see that accuracy was in a “taking off” stage and not flattening. Although it is a good sign, the training time was excessively high. Also, after 35 epochs, accuracy is considerably low.
    
    ![Figure 2.2 Epochs vs. Loss function](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-09_a_la(s)_18.05.17.png)
    
    Figure 2.2 Epochs vs. Loss function
    
    What we can see in **figure 2.2** is that after epoch 35, the loss function for validation and training were pretty much the same but the mode
    
    <aside>
    ⚠️ The model evaluation throughs a 16.96% of accuracy for the test set
    
    </aside>
    
- **Experiment conclusions**
    
    To have a complete comparison against the previous model, more epochs would be needed. The learning rate seems to be low. The accuracy is low.
    

---

### Expemient nº3

- **Technical Specifications**
    
    
    | Optimizer | Stochastic Gradient Descent |
    | --- | --- |
    | Learn. Rate | 0.01 |
    | Cropped images | No |
    | Epochs | 35 |
    | Batch Size | 32 |
    | Loss function | Cross Entropy |
    | Performance Metric | Accuracy |
    | Data augmentation techniques | Random flip; random rotation |
    | CNN model trainable layers | Last 10 |
- **Experiment report**
    
    ![Figure 3.1 Epochs vs. Accuracy](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-09_a_la(s)_18.15.36.png)
    
    Figure 3.1 Epochs vs. Accuracy
    
    What we can see in **figure 3.1** is that after training 35 epochs we see that with a bigger learning rate the accuracy starts flattening. Also the gap between training set and validation set is smaller than the first experiment. We are still experiencing overfitting but less overfitting than experiment 1.
    
    ![Captura de Pantalla 2023-02-09 a la(s) 18.18.19.png](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-09_a_la(s)_18.18.19.png)
    
    What we can see in **figure 3.2** is that after epoch 35, the loss function for validation and training start flattening reaching a period of low gaining for the validation set.
    
    <aside>
    ⚠️ The model evaluation throughs a 44.43% of accuracy for the test set
    
    </aside>
    
- **Experiment conclusions**
    
    With a higher learning rate things look a little bit better. We have a lower overfitting, and we reach a stable state for accuracy.
    

---

### Expemient nº4

- **Technical Specifications**
    
    
    | Optimizer | Stochastic Gradient Descent |
    | --- | --- |
    | Learn. Rate | 0.01 |
    | Cropped images | No |
    | Epochs | 35 |
    | Batch Size | 32 |
    | Loss function | Cross Entropy |
    | Performance Metric | Accuracy |
    | Data augmentation techniques | Random flip; random rotation; random zoom |
    | CNN model trainable layers | Last 10 |
- **Experiment report**
    
    ![Figure 4.1 Epochs vs Accuracy](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-09_a_la(s)_18.30.36.png)
    
    Figure 4.1 Epochs vs Accuracy
    
    What we can see in **figure 4.1** we see the same as the previous experiment. Adding data augmentation using the random zoom technique doesn't make any diffference. 
    
    ![Figure 4.1 Epochs vs Loss function](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-09_a_la(s)_18.31.09.png)
    
    Figure 4.1 Epochs vs Loss function
    
    What we can see in **figure 4.2** we see the same as the previous experiment. Adding data augmentation using the random zoom technique doesn't make any diffference.
    
    <aside>
    ⚠️ The model evaluation throughs a 40.16% of accuracy for the test set
    
    </aside>
    
- **Experiment conclusions**
    
    Random zoom technique for data augmentation doesn’t solve overfitting for the same previous model.
    

---

### Expemient nº5

- **Technical Specifications**
    
    
    | Optimizer | Stochastic Gradient Descent |
    | --- | --- |
    | Learn. Rate | 0.01 |
    | Cropped images | Si |
    | Epochs | 35 |
    | Batch Size | 32 |
    | Loss function | Cross Entropy |
    | Performance Metric | Accuracy |
    | Data augmentation techniques | Random flip; random rotation |
    | CNN model trainable layers | Last 10 |
- **Experiment report**
    
    For this experiment I am  using a training set which has been cropped to limit the image up to the car or track itself, and removing the background.
    
    ![Figure 5.1 Epochs vs. Accuracy](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-10_a_la(s)_12.18.52.png)
    
    Figure 5.1 Epochs vs. Accuracy
    
    What we can see in **figure 5.1** that the accuracy for both training and validation set are from higher order. There is still overfitting.
    
    ![Figure 5.2 Epochs vs. Loss function](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-10_a_la(s)_12.20.36.png)
    
    Figure 5.2 Epochs vs. Loss function
    
    What we can see in **figure 5.2** that after 35 epochs the loss function curve starts to flatten (particularly in the validation set) and there isn’t much gaining from keeping training the model for more steps or epochs.
    
    <aside>
    ⚠️ The model evaluation throughs a 59.18% of accuracy for the test set
    
    </aside>
    
- **Experiment conclusions**
    
    It is makes a model improvement if the image is first cut and afterwards and then predict its label. Training the model removing the background provoques a model improvement.
    

---

### Expemient nº6

- **Technical Specifications**
    
    
    | Optimizer | Adam |
    | --- | --- |
    | Learn. Rate | 0.001 |
    | Cropped images | Si |
    | Epochs | 35 |
    | Batch Size | 32 |
    | Loss function | Cross Entropy |
    | Performance Metric | Accuracy |
    | Data augmentation techniques | Random flip; random rotation |
    | CNN model trainable layers | Last 10 |
- **Experiment report**
    
    For this experiment I am using a training set which has been cropped to limit the image up to the car or track itself, and removing the background. The difference with the previous model is the optimizer used.
    
    ![Figure 6.1 Epoch vs. Accuracy](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-10_a_la(s)_12.36.35.png)
    
    Figure 6.1 Epoch vs. Accuracy
    
    What we can see in **figure 6.1** a significant gap between training and validation curves. This means that the model is strongly overfitting. 
    
    ![Figure 6.2 Epoch vs. Loss function](Sprint%20Project%2005%20-%20Report%20326810cb174047c2ac56f6f5454be891/Captura_de_Pantalla_2023-02-10_a_la(s)_12.45.03.png)
    
    Figure 6.2 Epoch vs. Loss function
    
    What we can see in **figure 6.2** is the same gap between validation and training, evidencing high overfitting.
    
    <aside>
    ⚠️ The model evaluation throughs a 59.40% of accuracy for the test set
    
    </aside>
    
- **Experiment conclusions**
    
    It is makes a model improvement if the image is first cut and afterwards and then predict its label. Training the model removing the background provoques a model improvement. Compared with using Adam instead of SGD is that Adam tends to overfit the model from the training data. General metrics are pretty similar. On the other hand, training times are lower.
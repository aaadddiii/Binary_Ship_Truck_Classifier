# Ship Truck Classifier
A Binary image classifier using keras that classifies images of ship and truck</br>
Notebook used for training the model can be found on the repo</br>
The model is deployed as an API on heroku.</br>

Link to the API https://truckshipclassification.herokuapp.com/detect


## Details
Trained on images of ships and trucks from cifar-10 dataset.</br>
The dataset can be found on the repo </br>
Dataset is trained on both Convolutional Neural Network and model using Transfer learning on VGG16
## Using convolutional Neural Network
Used three block VGG model architechture, achieved 80% accuracy on the test dataset

Line plots of loss and accuracy Learning curves for the model

<img src="https://user-images.githubusercontent.com/19375192/129048906-4d8e30db-3005-40af-96fc-3fe08f737e4d.png" alt="loss" width="400"/>
<img src="https://user-images.githubusercontent.com/19375192/129050372-291ed7a9-f093-4588-9164-b6a3bf859c65.png" alt="accuracy" width="400"/>

## Using Transfer Learning on VGG16
VGG16 model has 2 parts, the feature extraction part of the model that is made up of VGG blocks, and classifier part of the model made using fully connected layers and the output layer</br>
Used the feature extraction part of the model and added a new classifier part. <br/>
The weights of all the convolutional layers are fixed during training, and only trained the fully connected layers to learn to interpret the features extracted from the model for binary classification </br>
The model achieved very impressive results with a classification accuracy of 97% on the test dataset<br/>

Line plots of loss and accuracy Learning curves for the model

<img src="https://user-images.githubusercontent.com/19375192/129050880-26c80725-f4fb-4357-a14e-a3b1bca3df7c.png" alt="drawing" width="400"/>
<img src="https://user-images.githubusercontent.com/19375192/129050956-2bad5d60-fdae-4fe1-8e2e-844dc52a1692.png" alt="drawing" width="400"/>

The model is deployed on heroku using the flask web framework.
## Packages Used
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) 
- [Keras](https://keras.io/)
- [Numpy](https://numpy.org/)

Please feel free to raise any issue...



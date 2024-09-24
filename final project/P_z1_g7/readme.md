# Image Registration Using the MNIST Dataset

This project uses the MNIST dataset as a test case demonstrating how to implement deformable image registration. The model (final_project.ipynb) uses a convolutional neural network based on the VoxelMorph algorithm to learn a function mapping a fixed image to an arbitrary target image. 

The final_project.ipynb file contains all code for this project. The code is organized as follows:

- Setup: libraries are loaded, functions are defined, and the model architecture is built.
- Hyperparameter Tuning: loop for finding the set of hyperparameters leading to minimum validation loss at epoch=40.
- Final Model Training: bested parameters are loaded in, and the model is trained for up to 40 epochs.
- Results: image reconstruction is done for four cases (7, 1, 4, and 6), and test error is estimated.
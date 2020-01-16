# Machine Learning - Music-Popularity-Predictor

## Table of Contents
- [Overview](#Overview)
- [Dependencies](#Dependencies)
- [Code](#Code)
- [Running the code](#Running-the-code)
- [Data](#Data)
- [Evaluation](#Evaluation)
- [Benchmark](#Benchmark)

## Overview
Following repository is dedicated for capstone project of [Machine Learning Engineer Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t) program.

Main objective of capstone project is to utilize any machine learning algorithm in real-world problem. I have chosen to build an algorithm that predicts popularity of a music in [Spotify](https://www.spotify.com/). All the data are collected from [Spotify](https://www.spotify.com/) using [Spotipy](https://spotipy.readthedocs.io/en/2.6.1/).

In order to choose best model for prediction, several supervised learning algorithms were tested. Linear regression, logistic regression, decision tree regressor, random forest regressor, and neural network has been tested out for final model. At the end, neural network was chosen for final model, as it was able to predict with lowest root mean square error and mean absolute error.

For more detail of following project, you may check out the report

## Dependencies

This project requires **Python 3.x** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [keras](https://keras.io/)
- [Eli5](https://eli5.readthedocs.io/en/latest/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [spotipy](https://spotipy.readthedocs.io/)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.

## Code


* which requires spotify song URI. Spotify song URI can be copied from spotify by:
1. Right click the song that you want to get estimated song popularity
2. Click 'Share'
3. Click 'Copy Spotify URI'


Following project includes several codes for different purpose.
1. Data Collection: Code used to collect dataset for training prediction model.
2. Predict_Song_Popularity(Final): Final model for the users.
3. Song Popularity Estimator using Spotify Song Analysis: Overall data exploration, model comparison and how final model is built can be explored.
4. get_song_info.py : function used to get a single song analysis data
5. spotifydatafile.csv : output from Data Collection


## Running the code

In a terminal or command window, navigate to the top-level project directory `ML---Music-Popularity-Predictor/` (that contains following README file) and run one of the following commands:


1. If you want to simply get a estimated song popularity:
```bash
ipython notebook Predict_Song_popularity(Final).ipynb
```  
or
```bash
jupyter notebook Predict_Song_popularity(Final).ipynb
```
* which requires spotify song URI. Spotify song URI can be copied from spotify by:
a. Right click the song that you want to get estimated song popularity
b. Click 'Share'
c. Click 'Copy Spotify URI'

2. If you want to explore how model is built and explore the data:
```bash
ipython notebook Song_Popularity_Estimator_using_Spotify_Song_Analysis.ipynb
```  
or
```bash
jupyter notebook Song_Popularity_Estimator_using_Spotify_Song_Analysis.ipynb

This will open the iPython Notebook software and project file in your browser.
```

## Data

All the data for following project is collected from spotify. If further information is needed, please visit https://developer.spotify.com/

**Features**

- `track_name`: Name of the track
- `artist_name`: Name of the artist
- `track_id`: id of the track in spotify
- `artist_id`: id of the artist in spotify
- `track_popularity`: current track popularity in spotify
- `artist_popularity`: current artist popularity in spotify
- `artist_followers`: number of followers for the artist in spotify
- `confidence_mean`: mean confidence of overall song
- `confidence_std`: standard deviation of confidence through out the song
- `confidence_kurtosis`: kurtosis of confidence through out the song
- `loudness_mean`: mean loudness of overall song
- `loudness_std`: standard deviation of loudness through out the song
- `loudness_kurtosis`: kurtosis of loudness through out the song
- `tempo_mean`: mean tempo of overall song
- `tempo_std`: standard deviation of tempo through out the song
- `tempo_kurtosis`: kurtosis of tempo through out the song
- `tempo_confidence_mean`: mean tempo confidence of overall song
- `tempo_confidence_std`: standard deviation of tempo confidence through out the song
- `tempo_confidence_kurtosis`: kurtosis of tempo confidence through out the song
- `key_mean`: mean key of overall song
- `key_std`: standard deviation of key through out the song
- `key_kurtosis`: kurtosis of key through out the song
- `key_confidence_mean`: mean key confidence of overall song
- `key_confidence_std`: standard deviation of key confidence through out the song
- `key_confidence_kurtosis`: kurtosis of key confidence through out the song
- `mode_mean`: mean mode of overall song
- `mode_std`: standard deviation of mode through out the song
- `mode_kurtosis`: kurtosis of mode through out the song
- `mode_confidence_mean`: mean mode confidence of overall song
- `mode_confidence_std`: standard deviation of mode confidence through out the song
- `mode_confidence_kurtosis`: kurtosis of mode confidence through out the song
- `time_signature_mean`: mean time signature of overall song
- `time_signature_std`: standard deviation of time signature through out the song
- `time_signature_kurtosis`: kurtosis of time signature through out the song
- `time_signature_confidence_mean`: mean time signature confidence of overall song
- `time_signature_confidence_std`: standard deviation of time signature confidence through out the song
- `time_signature_confidence_kurtosis`: kurtosis of time signature confidence through out the song
- `C,C#.. B _dominance_mean`: mean dominance of a pitch of overall song
- `C,C#.. B _dominance_std`: standard deviation of a pitch through out the song
- `C,C#.. B _dominance_iqr`: interquartile range of a pitch through out the song
- `C,C#.. B _dominance_kurtosis`: kurtosis of a pitch through out the song
- `pitch_entropy`: entropy of pitch
- `timbre_ 1.. 12_mean`: mean timbre of overall song
- `timbre_ 1.. 12_std`: standard deviation of a timbre through out the song
- `timbre_ 1.. 12_iqr`: interquartile range of a timbre through out the song
- `timbre_ 1.. 12_kurtosis`: kurtosis of a timbre through out the song

## Evaluation
Among various accuracy measurement, root mean square error (RMSE) score has been used for comparing models. Below are the RMSE score for all models on pre-processed dataset.

- Support Vector Classifier (SVC)
  - RMSE Score: 371.45

- Linear Regression
  - RMSE Score: 260.48

- Logistic Regression
  - RMSE Score: 422

- Decision Tree Regressor
  - RMSE Score: 646.37

- Random Forest Regressor
  - RMSE: 309.1

- Neural Network
  - RMSE Score: 16.16

Comparing all the models, Neural Network performed much better than all the other models. Therefore, Neural Network has been chosen as final model.

## Benchmark

At first, song popularity predictor by Mohamed Nasreldin, Stephen Ma, Eric Dailey, and Phuc Dang was chosen as benchmark model. However, song popularity predictor used area under curve (AUC) as their metrics, which is not a great choice for regression problem. AUC is a good metric for a classification models. I was planning to run their code with root mean squared and R squared metric. However, code provided by Mohamed Nasreldin does not include complete dataset named cleaned_million.csv. Therefore, it was not possible for me to run the code and obtain values for comparison.

Model by Mohamed Nasreldin, Stephen Ma, Eric Dailey, Phuc Dang can be found from
https://towardsdatascience.com/song-popularity-predictor-1ef69735e380

with source code
https://github.com/manasreldin/Song-Popularity-Predictor

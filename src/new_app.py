import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from runner import run_app
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import seaborn as sns


def run_streamlit_app():
   # Page layout and custom styles
    st.markdown("""
        <style>
        .big-font {
            font-size:30px !important;
            font-weight: bold;
        }
        .reportview-container {
            background-color: #f0f2f6;
        }
        </style>
        """, unsafe_allow_html=True)
    sns.set_theme(style="whitegrid") # theme for seaborn plots

    st.markdown('<p class="big-font">Used Car Price Prediction Using Gradient Boosting Regressor</p>', unsafe_allow_html=True)
    st.markdown('<p class="footer">Sree Lekshmi<br> Gayathri <br>Jaskirat </p>', unsafe_allow_html=True)
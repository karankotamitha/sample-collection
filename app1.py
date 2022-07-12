# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:05:34 2022

@author: amith
"""

import streamlit as st
import pickle
import numpy as np
import haversine as haversine

data = pickle.load(open("data_set.pkl","rb"))
model = pickle.load(open("lg_reg.pkl", "rb"))

project = st.sidebar.radio('SELECT AN OPTION', ['HOME', 'PREDICTION'])


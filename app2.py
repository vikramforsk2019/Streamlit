#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:41:11 2020

@author: jagveer
"""

import streamlit as st
model_list=['MR','PR','DTR','RF','SVR']
if st.checkbox('select columns to show'):
    selected=st.selectbox('Select',model_list)
    if selected=='MR':
        st.write(selected)      

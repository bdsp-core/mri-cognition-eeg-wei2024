import numpy as np
import pandas as pd
import os

def get_hypothesis_data(df_sleep, df_mri, hypothesis_name):
    
    assert all(df_sleep.index == df_mri.index)
    # assert len(df_sleep) in [623, 160] # number of included patients
    
    if hypothesis_name == 'slow waves':
        mri_var = ['vol-ctx--anterior', 'vol-thalamus'] # 'vol-claustrum'
        sleep_var = ['slowdelta_bandpower_total', 'so_rate_f']
        
    elif hypothesis_name == 'spindles':
        mri_var = ['vol-thalamus', 'vol-hippocampus']
        sleep_var = ['ss_dens_f', 'fs_dens_c']
        
    elif hypothesis_name == 'rem':
        mri_var = ['vol-ctx--isthmuscingulate', 'vol-amygdala', 'vol-brain-stem'] # 'vol-basal forebrain'
        sleep_var = ['perc_r']
        
    elif hypothesis_name == 'wake':
        mri_var = ['vol-thalamus', 'vol-total_ventricle']
        sleep_var = ['alpha_bandpower_mean_o_w']

    df_hypothesis_sleep = df_sleep[sleep_var]
    df_hypothesis_mri = df_mri[mri_var]

    return df_hypothesis_sleep, df_hypothesis_mri
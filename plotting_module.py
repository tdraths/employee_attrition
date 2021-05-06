import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.gridspec as gridspec

plt.style.use(['bmh', 'tableau-colorblind10', 'seaborn-paper'])

def attrition_plot(df):
  fig = plt.figure(figsize=(20, 10))
  plt.subplot(121)
  plt.pie(x=df['attrition'].value_counts(), labels=['No Attrition', 'Attrition'], autopct='%.1f%%', radius=1, textprops={'fontsize': 20, 'fontweight': 'bold'})
  plt.title('Rate of Attrition', fontsize=30, fontweight='bold')
  plt.subplot(122)
  ax = sns.countplot(df['attrition'])
  ax.set_xlabel('Attrition', fontsize=20, fontweight='bold')
  ax.set_ylabel('Count', fontsize=20, fontweight='bold')
  plt.title('Attrition Distributions', fontsize=30, fontweight='bold')
  plt.tight_layout()

def eda_numerical(df, feature):
  plt.figure(figsize=(15, 3))
  plt.title(f"KDE Plot: {feature}", fontsize=30, fontweight='bold')
  ax = sns.kdeplot(x=df[df['attrition'] == 0][feature].dropna(), label='No Attrition', lw=2, legend=True)
  plt.legend=True
  ax1 = sns.kdeplot(x=df[df['attrition'] == 1][feature].dropna(), label='Attrition', lw=2, legend=True)
  plt.tight_layout();

def cat_comparison(df, feature):
    fig = plt.figure(figsize=(15, 20))
    gs = fig.add_gridspec(3, 3)
    
    ax1 = fig.add_subplot(gs[0,0])
    sns.violinplot(x='gender', y=feature, hue='attrition', data=df)
    plt.title(f'{feature.title()} by Gender', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    
    ax2 = fig.add_subplot(gs[0,1])
    sns.violinplot(x='businesstravel', y=feature, hue='attrition', data=df)
    plt.title(f'{feature.title()} by Business Travel', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    
    ax3 = fig.add_subplot(gs[0,2])
    sns.violinplot(x='department', y=feature, hue='attrition', data=df)
    plt.title(f'{feature.title()} by Department', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    
    ax4 = fig.add_subplot(gs[1,:])
    sns.violinplot(x='jobrole', y=feature, hue='attrition', data=df)
    plt.title(f'{feature.title()} by Job Role', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    
    ax5 = fig.add_subplot(gs[2,:])
    sns.violinplot(x='educationfield', y=feature, hue='attrition', data=df)
    plt.title(f'{feature.title()} by Education Field', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    
    plt.tight_layout();
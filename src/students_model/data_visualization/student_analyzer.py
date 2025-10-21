import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

class StudentAnalyzer:
    def __init__(self, df):
        self.df = df
        self.figures = []
    
    def create_comprehensive_analysis(self):
        """Create comprehensive analysis with multiple plots"""
        # Create a 2x2 subplot grid
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Plot 1: Grade distribution
        self.df['percent'].hist(ax=axes[0,0], bins=20, alpha=0.7, color='skyblue')
        axes[0,0].set_title('Grade Distribution')
        axes[0,0].set_xlabel('Percentage')
        axes[0,0].set_ylabel('Frequency')
        
        # Plot 2: Subject comparison
        subjects = ['math_marks', 'science_marks', 'english_marks']
        self.df[subjects].mean().plot(kind='bar', ax=axes[0,1], color=['red', 'green', 'blue'])
        axes[0,1].set_title('Average Marks by Subject')
        axes[0,1].set_ylabel('Average Marks')
        
        # Plot 3: Income distribution
        self.df['family_income'].hist(ax=axes[1,0], bins=30, alpha=0.7, color='orange')
        axes[1,0].set_title('Family Income Distribution')
        axes[1,0].set_xlabel('Income')
        axes[1,0].set_ylabel('Frequency')
        
        # Plot 4: Correlation heatmap
        numeric_cols = self.df.select_dtypes(include=[np.number])
        sns.heatmap(numeric_cols.corr(), annot=True, ax=axes[1,1], cmap='coolwarm')
        axes[1,1].set_title('Feature Correlation Heatmap')
        
        plt.tight_layout()
        return fig
    
    def create_interactive_plots(self):
        """Create plots suitable for Jupyter interactive display"""
        fig = plt.figure(figsize=(15, 5))
        
        plt.subplot(1, 3, 1)
        self.df.boxplot(column=['math_marks', 'science_marks', 'english_marks'])
        plt.title('Marks Distribution by Subject')
        plt.xticks(rotation=45)
        
        plt.subplot(1, 3, 2)
        self.df['improvement'].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title('Improvement Distribution')
        
        plt.subplot(1, 3, 3)
        plt.scatter(self.df['family_income'], self.df['percent'], alpha=0.5)
        plt.xlabel('Family Income')
        plt.ylabel('Percentage')
        plt.title('Income vs Academic Performance')
        
        plt.tight_layout()
        return fig
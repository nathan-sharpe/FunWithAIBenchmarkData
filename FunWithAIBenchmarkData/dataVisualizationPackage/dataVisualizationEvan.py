# File Name : dataVisualizationEvan.py
# Student Name: Evan Bolin
# email:  bolinen@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  using logic to create an image and data visualizations with datasets

# Brief Description of what this module does. create a pie chart of nor nutrition_test.csv about the percentage of questions with answers "A, B, C, D"
# Citations: CHATGPT 

import pandas as pd
import matplotlib.pyplot as plt

def create_answer_pie_chart(csv_path):
    # Load CSV with no header
    df = pd.read_csv(csv_path, header=None)

    # Get the answers from column F (index 5)
    answers = df[5]

    # Count each answer (A, B, C, D)
    answer_counts = answers.value_counts().sort_index()

    # Plot the pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(answer_counts, labels=answer_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Correct Answers')
    plt.axis('equal')
    plt.show()
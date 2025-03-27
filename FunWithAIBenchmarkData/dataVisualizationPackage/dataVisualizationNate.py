# File Name : dataVisualizationNate.py
# Student Name: Nathan Sharpe
# email: sharpenn@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/27/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Perform data visualization on a dataset as well as generating an image of the Pokemon your team is named
# after, in our case Oddish. 

# Brief Description of what this module does: Provides information about data processing and visualization on datasets and how to extract insights
# from the data.
# Citations: gemini.google.com

# Anything else that's relevant: Gemini was used to generate the data visualization code.

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("dataPackage/MMLU/data/global_facts_test.csv", header=None)

# Get the number of questions
num_questions = len(df)

# Initialize lists to store the counts
counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

# Iterate through the DataFrame and count the answers
for _, row in df.iterrows():
    answer = row[5]  # The correct answer is in the sixth column (index 5)
    if isinstance(answer, str) and answer.upper() in counts:
        counts[answer.upper()] += 1

# Create a bar graph
plt.figure(figsize=(10, 6))  # Adjust figure size for better readability
bars = plt.bar(counts.keys(), counts.values(), color=['red', 'blue', 'green', 'orange'])

# Add labels and title
plt.xlabel('Answers', fontsize=12)
plt.ylabel('Number of Correct Answers', fontsize=12)
plt.title('Distribution of Correct Answers', fontsize=14)

# Add the exact count on top of each bar.
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, yval, ha='center', va='bottom', fontsize=10)

# Show the plot
plt.show()

# Print the counts
print("Distribution of Correct Answers:")
for answer, count in counts.items():
    print(f"{answer}: {count}")

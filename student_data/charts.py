import matplotlib
matplotlib.use("Agg")  # IMPORTANT: no GUI backend

import matplotlib.pyplot as plt
import os

def generate_average_score_chart(students, output_path):
    names = []
    averages = []

    for student in students:
        if student.grade is not None:
            names.append(student.name)
            averages.append(student.grade)

    plt.figure(figsize=(8, 4))
    plt.bar(names, averages)
    plt.xlabel("Students")
    plt.ylabel("Average Score")
    plt.title("Average Student Scores")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()

# 🌿 Eco-Activity Analyzer (Green Habit Tracker)
# Developed by: Sanskriti Kapoor
# Concepts used: Tkinter, NumPy, Matplotlib, Functions, Lists & Dictionaries

import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Data structure for eco-habits
# ----------------------------
habits = {
    "Used Bicycle/Walked Instead of Vehicle": 0,
    "Saved Water": 0,
    "Recycled Waste": 0,
    "Avoided Plastic": 0,
    "Planted a Tree/Plant": 0,
    "Saved Electricity": 0
}

# ----------------------------
# Function: Add activity count
# ----------------------------
def add_activity(habit):
    habits[habit] += 1
    messagebox.showinfo("Updated", f"✅ Added 1 point to '{habit}'")

# ----------------------------
# Function: Show analytics
# ----------------------------
def show_analytics():
    total_actions = sum(habits.values())
    if total_actions == 0:
        messagebox.showwarning("No Data", "Please record at least one activity!")
        return

    # Convert to NumPy array for calculations
    values = np.array(list(habits.values()))
    avg = np.mean(values)
    max_val = np.max(values)
    top_habit = [h for h, v in habits.items() if v == max_val][0]

    summary = (
        f"🌿 Total Eco Actions: {total_actions}\n"
        f"📊 Average Actions per Habit: {avg:.2f}\n"
        f"🏆 Most Frequent Habit: {top_habit}\n\n"
        f"💪 Keep up the great work for a greener planet!"
    )
    messagebox.showinfo("Eco Summary", summary)

    # ----------------------------
    # Bar Chart Visualization
    # ----------------------------
    plt.figure(figsize=(8, 5))
    plt.bar(habits.keys(), habits.values(), color='seagreen', edgecolor='black')
    plt.xticks(rotation=30, ha='right')
    plt.title("Eco-Friendly Activities Tracker", fontsize=14, fontweight='bold')
    plt.xlabel("Habits", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.tight_layout()
    plt.show()

    # ----------------------------
    # Improved Pie Chart Visualization
    # ----------------------------
    plt.figure(figsize=(7, 6))

    # Remove zero-value habits to prevent label overlap
    non_zero_habits = {k: v for k, v in habits.items() if v > 0}

    if not non_zero_habits:
        messagebox.showwarning("No Data", "No recorded habits to display in the pie chart!")
        return

    plt.pie(
        non_zero_habits.values(),
        labels=non_zero_habits.keys(),
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=0.85
    )

    # Add a white circle to make a donut chart
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title("Eco-Activity Distribution", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# ----------------------------
# Function: Reset all data
# ----------------------------
def reset_data():
    for key in habits.keys():
        habits[key] = 0
    messagebox.showinfo("Reset", "Data has been reset successfully!")

# ----------------------------
# GUI Setup
# ----------------------------
root = tk.Tk()
root.title("🌍 Eco-Activity Analyzer")
root.geometry("520x620")
root.config(bg="#e0f7e9")

# Title label
title_label = tk.Label(
    root,
    text="🌿 Eco-Activity Analyzer 🌿",
    font=("Helvetica", 18, "bold"),
    bg="#e0f7e9",
    fg="darkgreen"
)
title_label.pack(pady=20)

# Create buttons dynamically for each habit
for habit in habits.keys():
    btn = tk.Button(
        root,
        text=habit,
        font=("Arial", 12),
        width=40,
        bg="#a5d6a7",
        fg="black",
        activebackground="#81c784",
        command=lambda h=habit: add_activity(h)
    )
    btn.pack(pady=5)

# Functional buttons
tk.Button(
    root, text="📊 Show Analytics", font=("Arial", 13, "bold"),
    bg="#388e3c", fg="white", command=show_analytics
).pack(pady=20)

tk.Button(
    root, text="🔄 Reset Data", font=("Arial", 12, "bold"),
    bg="#ff7043", fg="white", command=reset_data
).pack(pady=10)

tk.Button(
    root, text="❌ Exit", font=("Arial", 12, "bold"),
    bg="#c62828", fg="white", command=root.destroy
).pack(pady=10)

# Run main loop
root.mainloop()

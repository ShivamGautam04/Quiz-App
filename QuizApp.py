import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style

# Data
data = [
    {
        "question": "Two popular asssemblies of vedic period?",
        "choices": ["Ur and Kula", "Sabha and Samiti", "Mahasabha and Ganasabha", "Sabha and Mahasabha"],
        "answer": "Sabha and Samiti"
    },
    {
        "question": "Ayurveda has its origin in",
        "choices": ["Rig Veda", "Sama Veda", "Yajur Veda", "Atharva Veda"],
        "answer": "Atharva Veda"
    },
    {
        "question": "The Rigvedic Aryans were governed by a",
        "choices": ["Rule by elders", "Monarchical government", "Form of democracy", "Tribal republic"],
        "answer": "Monarchical government"
    },
    {
        "question": "In the early Vedic-period, Varna system was based on?",
        "choices": ["Talent", "Occupation", "Birth", "Education"],
        "answer": "Occupation"
    },
    {
        "question": " Which one of the following Vedas contains sacrificial formula?",
        "choices": ["Sama Veda", "Atharva Veda", "Rig Veda", "Yajur Veda"],
        "answer": "Japan"
    },
    {
        "question": " Who among the following was the pioneer of Yoga?",
        "choices": ["Talent", "Occupation", "Birth", "Education"],
        "answer": "Japan"
    },
    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "choices": ["Vrudukanta", "Atreya", "Banabhatta", "Patanjali"],
        "answer": "Patanjali"
    },
    {
        "question": "Who was the author of Arthashastra?",
        "choices": ["Vishakhadutta", "Megasthenes", "Vasudeva", "Kautilya"],
        "answer": "Kautilya"
    },
    {
        "question": "Kautilya Arthashastra deals with the aspects of",
        "choices": ["Social life", "Economic life", "Religious life", "Political policies"],
        "answer": "Economic life"
    },
    {
        "question": "Which of the following are the parts of Ramcharitmanas?",
        "choices": ["Kiskindha Kanda", "Aranya Kanda", "Bal Kanda", "All the above are correct"],
        "answer": "All the above are correct"
    },
    {
        "question": "Who was the wife of lakshmana?",
        "choices": ["Mandavi", "Shruthakirti", "Urmila", "Sita"],
        "answer": "Urmila"
    }
    # Add more question here
    
]

# Function to display the current question and choices
def show_question():
    # Get the current question from the data list
    question = data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the data list
    question = data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question +=1

    if current_question < len(data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(data)))
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme="flatly")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()
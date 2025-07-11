import json
import os
from datetime import datetime
from collections import Counter
from tkinter import *
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class EmotionTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grow EI - Emotional Intelligence Logger")
        self.root.geometry("700x500")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=BOTH, expand=True)

        self.log_tab = Frame(self.notebook)
        self.history_tab = Frame(self.notebook)
        self.strategy_tab = Frame(self.notebook)
        self.report_tab = Frame(self.notebook)

        self.notebook.add(self.log_tab, text="Log Emotion")
        self.notebook.add(self.history_tab, text="History")
        self.notebook.add(self.strategy_tab, text="Dealing Strategies")
        self.notebook.add(self.report_tab, text="Report")

        self.emotion_file = "emotion_log.json"
        self.init_ui()

    def init_ui(self):
        self.build_log_tab()
        self.build_history_tab()
        self.build_strategy_tab()
        self.build_report_tab()

    # ---------------- Log Tab ------------------
    def build_log_tab(self):
        Label(self.log_tab, text="How are you feeling right now?", font=("Arial", 14)).pack(pady=10)
        self.emotion_var = StringVar()

        emotions = ["Happy", "Sad", "Angry", "Anxious", "Calm", "Grateful", "Frustrated", "Excited"]
        for emotion in emotions:
            Radiobutton(self.log_tab, text=emotion, variable=self.emotion_var, value=emotion).pack(anchor=W)

        Label(self.log_tab, text="Describe what happened:").pack(pady=(10, 0))
        self.situation_text = Text(self.log_tab, height=4, width=60)
        self.situation_text.pack()

        Label(self.log_tab, text="What did you do to understand your emotion better? (Find tips in Coping Tab)").pack(pady=(10, 0))
        self.coping_text = Text(self.log_tab, height=4, width=60)
        self.coping_text.pack()

        Button(self.log_tab, text="Submit Entry", command=self.save_entry, bg="green", fg="white").pack(pady=10)

    def save_entry(self):
        emotion = self.emotion_var.get()
        situation = self.situation_text.get("1.0", END).strip()
        coping = self.coping_text.get("1.0", END).strip()

        if not emotion:
            messagebox.showwarning("Missing", "Please select an emotion.")
            return

        entry = {
            "emotion": emotion,
            "situation": situation,
            "dealing": coping,
            "timestamp": datetime.now().isoformat()
        }

        data = []
        if os.path.exists(self.emotion_file):
            with open(self.emotion_file, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

        data.append(entry)
        with open(self.emotion_file, "w") as f:
            json.dump(data, f, indent=2)

        self.situation_text.delete("1.0", END)
        self.coping_text.delete("1.0", END)
        self.emotion_var.set("")

        messagebox.showinfo("Saved", "Entry saved successfully!")
        self.load_history()

    # ---------------- History Tab ------------------
    def build_history_tab(self):
        self.history_listbox = Listbox(self.history_tab, width=100, height=20)
        self.history_listbox.pack(pady=10)
        Button(self.history_tab, text="Clear History", command=self.clear_history, fg="white", bg="red").pack()
        self.load_history()

    def load_history(self):
        self.history_listbox.delete(0, END)
        if not os.path.exists(self.emotion_file):
            return
        with open(self.emotion_file, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
        for entry in data:
            line = f"{entry['timestamp'][:16]} - {entry['emotion']} | Situation: {entry['situation'][:40]}... | Dealing: {entry['dealing'][:40]}..."
            self.history_listbox.insert(END, line)

    def clear_history(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all history?"):
            with open(self.emotion_file, "w") as f:
                json.dump([], f)
            self.load_history()
            messagebox.showinfo("Cleared", "History cleared.")

    # ---------------- Strategies Tab ------------------
    def build_strategy_tab(self):
        tips = [
            ("Happy", "Share your joy or write it down to remember."),
            ("Sad", "Talk to a friend or engage in a soothing activity."),
            ("Angry", "Take a walk or try deep breathing."),
            ("Anxious", "Try grounding techniques or guided meditation."),
            ("Calm", "Maintain it with journaling or relaxing music."),
            ("Grateful", "Write a thank-you note or share appreciation."),
            ("Frustrated", "Break down tasks or take a short break."),
            ("Excited", "Channel it into creative or productive tasks."),
        ]

        for emotion, tip in tips:
            Label(self.strategy_tab, text=f"{emotion}: {tip}", wraplength=600, justify=LEFT).pack(anchor=W, padx=10, pady=3)

    # ---------------- Report Tab ------------------
    def build_report_tab(self):
        self.report_frame = Frame(self.report_tab)
        self.report_frame.pack(fill=BOTH, expand=True)

        Button(self.report_frame, text="Generate Report", command=self.show_emotion_report,
               bg="blue", fg="white").pack(pady=10)

        self.chart_area = Frame(self.report_frame)
        self.chart_area.pack(fill=BOTH, expand=True)

    def show_emotion_report(self):
        for widget in self.chart_area.winfo_children():
            widget.destroy()

        try:
            with open(self.emotion_file, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showinfo("No Data", "No emotion entries found.")
            return

        if not data:
            messagebox.showinfo("No Data", "No emotion entries found.")
            return

        emotions = [entry['emotion'] for entry in data if 'emotion' in entry]
        counts = Counter(emotions)

        if not counts:
            messagebox.showinfo("No Data", "No valid emotions found.")
            return

        fig, ax = plt.subplots()
        ax.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%', startangle=140)
        ax.axis('equal')
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.chart_area)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)


if __name__ == '__main__':
    root = Tk()
    app = EmotionTrackerApp(root)
    root.mainloop()

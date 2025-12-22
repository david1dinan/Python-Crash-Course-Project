# Python Crash Course – Chapter Projects

This repository tracks my progress through the first 17 chapters of *Python Crash Course* by Eric Matthes. Each chapter introduces foundational Python concepts, and I've included my working code, solutions, and experiments here.

The structure is organized by chapter, with hands-on exercises that have helped reinforce concepts like variables, control flow, data structures, functions, file handling, testing, APIs, and basic data visualization.

---

## Getting Started

Want to follow along with the *Python Crash Course* book? Here's how to set up your own learning environment.

### Prerequisites

- **Python 3.10+** – Download from [python.org](https://www.python.org/downloads/)
- **Git** – Download from [git-scm.com](https://git-scm.com/downloads)
- **A code editor** – Recommended: [VS Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/download/)

### Option 1: Fork This Repository (Recommended)

Forking allows you to have your own copy to modify and track your progress:

1. Click the **Fork** button at the top right of this repository
2. Clone your forked repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Python-Crash-Course-Project.git
   cd Python-Crash-Course-Project
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - **macOS/Linux**: `source .venv/bin/activate`
   - **Windows**: `.venv\Scripts\activate`
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Start Fresh

If you prefer to build your own project from scratch:

1. Create a new directory and navigate to it:
   ```bash
   mkdir python-crash-course
   cd python-crash-course
   ```
2. Initialize a Git repository:
   ```bash
   git init
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # or: .venv\Scripts\activate  # Windows
   ```
4. Create your chapter folders as you progress:
   ```bash
   mkdir "Chapter 01 - Introduction"
   mkdir "Chapter 02 - Variables and Simple Data Types"
   # ... and so on
   ```
5. Install packages as needed:
   ```bash
   pip install matplotlib plotly numpy requests pytest
   ```

### Running the Scripts

Navigate to any chapter folder and run the Python files:

```bash
cd "scripts/Chapter 02 - Variables and Simple Data Types"
python hello_world.py
```

Or run from the project root:

```bash
python "scripts/Chapter 02 - Variables and Simple Data Types/hello_world.py"
```

---

## Chapters and Coverage

Each folder corresponds to a chapter and its core themes:

| Chapter | Topic | Key Concepts |
|---------|-------|--------------|
| [01](./scripts/Chapter%2001%20-%20Introduction) | Introduction | Setting up Python, first program |
| [02](./scripts/Chapter%2002%20-%20Variables%20and%20Simple%20Data%20Types) | Variables & Data Types | Strings, integers, floats |
| [03](./scripts/Chapter%2003%20-%20Introducing%20Lists) | Introducing Lists | Lists, indexing, modifying elements |
| [04](./scripts/Chapter%2004%20-%20Working%20With%20Lists) | Working With Lists | Loops, slices, tuples |
| [05](./scripts/Chapter%2005%20-%20If%20Statements) | If Statements | Conditionals, boolean logic |
| [06](./scripts/Chapter%2006%20-%20Dictionaries) | Dictionaries | Key-value pairs, nesting |
| [07](./scripts/Chapter%2007%20-%20Input%20and%20While%20Loops) | Input & While Loops | User input, while loops |
| [08](./scripts/Chapter%2008%20-%20Functions) | Functions | Defining functions, arguments, modules |
| [09](./scripts/Chapter%2009%20-%20Classes) | Classes | OOP, inheritance, instances |
| [10](./scripts/Chapter%2010%20-%20Files%20and%20Exceptions) | Files & Exceptions | Reading/writing files, error handling |
| [11](./scripts/Chapter%2011%20-%20Testing%20Your%20Code) | Testing Your Code | pytest, unit tests |
| [15](./scripts/Chapter%2015%20-%20Generating%20Data) | Generating Data | Matplotlib, Plotly, random walks |
| [16](./scripts/Chapter%2016%20-%20Downloading%20Data) | Downloading Data | CSV, JSON, APIs |
| [17](./scripts/Chapter%2017%20-%20Working%20with%20APIs) | Working with APIs | Web APIs, requests, GitHub API |

---

## Testing & Practice

- [Pytest files](./Pytest%20files): Practice with writing tests
- [Practice](./Practice): Extra exercises, scripts, and snippets for reinforcement

---

## Tips for Your Learning Journey

1. **Type the code yourself** – Don't just copy-paste. Typing helps reinforce the concepts.
2. **Experiment** – Modify the examples, break things, see what happens.
3. **Commit often** – Track your progress with Git commits as you complete each exercise.
4. **Do the Try It Yourself exercises** – These are where the real learning happens.
5. **Don't skip chapters** – Each chapter builds on the previous ones.

---

## Project Continuation

The skills developed here were later used in the **[Learning Log](https://github.com/E-Conners-Lab/The_Learning_log)** Django web app — a full-stack application that serves as a live, deployed learning journal.

---

## Next Steps

The final project in the book is a game-based project (Alien Invasion - Chapters 12-14), which I saved for last to focus on applications like automation and data visualization first.

Up next:
- Building the **Alien Invasion** game project
- Diving deeper into **network automation**, **APIs**, and **dashboards**
- Exploring the use of **LLMs** in managing network infrastructure

---

## Requirements

- Python 3.10+
- Dependencies: `pip install -r requirements.txt`

The main packages used in later chapters:
- `matplotlib` – Data visualization
- `plotly` – Interactive charts
- `numpy` – Numerical computing
- `requests` – API calls (Chapter 17)
- `pytest` – Testing (Chapter 11)

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
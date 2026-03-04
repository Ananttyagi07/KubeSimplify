# Day 1 – Project Initialization

## Repository Creation

Created the GitHub repository for the project.

Repository URL:

```
https://github.com/Ananttyagi07/KubeSimplify
```

---

## Clone Repository

Cloned the repository to the local machine.

```bash
git clone https://github.com/Ananttyagi07/KubeSimplify.git
cd KubeSimplify
```

---

## Open Project in VS Code

Opened the project directory in Visual Studio Code.

```bash
code .
```

---

## Project Structure Setup

Created the initial project structure.

```bash
mkdir ks
touch main.py
touch requirements.txt
touch ks/__init__.py
touch ks/k8s_client.py
touch ks/commands.py
touch ks/formatter.py
```

Current structure:

```
KubeSimplify
│
├── README.md
├── DEVLOG.md
├── main.py
├── requirements.txt
│
└── ks
    ├── __init__.py
    ├── k8s_client.py
    ├── commands.py
    └── formatter.py
```

---

## Create Virtual Environment

Created a Python virtual environment for dependency isolation.

```bash
python3 -m venv venv
```

Activated the environment.

```bash
source venv/bin/activate
```

---

## Install Dependencies

Installed required Python libraries.

```bash
pip install click rich kubernetes
```

Saved dependencies.

```bash
pip freeze > requirements.txt
```

---

## Implement Initial CLI

Created a basic CLI command using the Click library.

Command executed:

```bash
python main.py hello
```

Output:

```
Welcome to KubeSimplify 
```

---

## First Commit

Committed the initial project setup.

```bash
git add .
git commit -m "Initialize KubeSimplify project structure and CLI"
git push
```

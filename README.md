**KubeSimplify** is a developer-friendly CLI tool designed to simplify everyday Kubernetes operations.
It acts as a smart wrapper around `kubectl`, providing clean cluster insights, automated pod diagnostics, and simplified commands to make debugging and managing Kubernetes workloads easier.

The goal of KubeSimplify is to reduce the complexity of Kubernetes troubleshooting by offering developer-focused utilities directly from the terminal.

---

## 🚀 Features

* **Simplified CLI Commands** – Easier alternatives to complex `kubectl` commands
* **Pod Health Summary** – Clean overview of pod status, restarts, and health
* **Automated Diagnostics** – Detect common issues such as:

  * `CrashLoopBackOff`
  * `ImagePullBackOff`
  * `OOMKilled`
  * `FailedScheduling`
* **YAML Generator** – Generate deployment and service YAML files quickly
* **Human-Readable Output** – Structured and easy-to-read CLI output

---

## 🛠 Tech Stack

* Python
* Kubernetes Python Client
* Click (CLI framework)
* Rich (formatted terminal output)

---

## 📂 Project Structure

```
kubesimplify/
│
├── main.py
├── requirements.txt
│
└── ks/
    ├── k8s_client.py
    ├── commands.py
    ├── formatter.py
    └── diagnostics.py
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/Ananttyagi07/KubeSimplify.git
cd KubeSimplify
```

Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Example command:

```
python main.py pods
```

Example output:

```
Namespace     Pod Name          Status      Restarts
-----------------------------------------------------
default       nginx-abc123      Running     0
kube-system   coredns-xyz       Running     0
```

---

## 🎯 Project Goal

KubeSimplify aims to improve the developer experience when working with Kubernetes by:

* Simplifying debugging workflows
* Reducing command complexity
* Providing helpful diagnostics directly in the CLI

---

## 📌 Roadmap

* [ ] Pod health summary
* [ ] Pod diagnostics engine
* [ ] YAML generator
* [ ] Misconfiguration detection
* [ ] AI-assisted troubleshooting

---

## 👨‍💻 Author

**Anant Tyagi**

# 🔍 TCP Port Scanner

## 📌 Project Overview

This project is a **TCP Port Scanner** built using **Python** as part of the internship at **Syntecxhub**.
The scanner checks for **open, closed, and timeout TCP ports** on a given host using socket programming and multithreading.

---

## 🎯 Objectives

* Learn **socket programming basics**
* Understand **TCP connections**
* Implement **multithreading (concurrency)**
* Handle **exceptions and timeouts**
* Log scan results for analysis

---

## ⚙️ Features

* ✅ Scan a single host (IP or hostname)
* ✅ Scan a **range of ports**
* ✅ Fast scanning using **threads**
* ✅ Handles:

  * Open ports
  * Closed ports
  * Timeout ports
* ✅ Prints results on terminal
* ✅ Logs results into a file (`scan_results.log`)

---

## 🛠️ Technologies Used

* **Python 3**
* `socket`
* `threading`
* `logging`
* `datetime`

> No external libraries are required (uses Python standard library only).

---

## 📂 Project Structure

```
syntecxhub_port_scanner/
│
├── main.py
├── scan_results.log
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abdullahkhaver/syntecxhub_port_scanner
cd syntecxhub_port_scanner
```

### 2️⃣ Run the Script

```bash
python main.py
```

### 3️⃣ Provide Input

```
Enter target host (e.g. 127.0.0.1)
Start port
End port
```

---

## 🧪 Example

```
Target: 127.0.0.1
Ports: 20 - 100
```

**Output:**

```
[+] Port 22 OPEN
[-] Port 80 CLOSED
[!] Port 8080 TIMEOUT
```

---

## 📄 Logging

All scan results are saved in:

```
scan_results.log
```

Each entry includes a timestamp for tracking and analysis.

---

## ⚠️ Disclaimer

This tool is created **for educational purposes only**.
Only scan:

* Your own systems
* Localhost (`127.0.0.1`)
* Systems you have **explicit permission** to test

Unauthorized port scanning may be illegal.

---

## 🏁 Internship Information

* **Organization:** Syntecxhub
* **Project:** Project 1 – Port Scanner
* **Domain:** Networking / Cybersecurity

---

## 🤝 Acknowledgment

Thanks to **Syntecxhub** for providing the opportunity to work on practical, hands-on projects and enhance real-world technical skills.

---

### ⭐ If you found this project helpful, feel free to star the repository!


# 🧠 Echo Server - Computer Networks Lab 1

This project is part of **Lab 1 (Intro to Socket Programming)** for the **Computer Networks (00207N)** course at **Alexandria National University**.

It demonstrates a simple **TCP Echo Server and Client** implemented in Python, communicating through `localhost` on port `5000`.

---

## 🖥️ Overview

The **Server**:
- Waits for a client connection.
- Receives a message starting with one of the characters `A`, `C`, or `D`.
- Performs the following actions based on the first character:

| Command | Description |
|----------|--------------|
| **A** | Sort the letters in **descending** order |
| **C** | Sort the letters in **ascending** order |
| **D** | Convert all letters to **uppercase** |
| **Other** | Return the same message as received |

Then it sends the processed message back to the client.

---

## ⚙️ How to Run

### 1. Run the Server
```bash
python server.py

2. Run the Client
In another terminal:
python client.py

3. Send Messages
Examples:
Ahello     →  ollhe
Cpython    →  hnopty
Dsocket    →  SOCKET

Type exit to close the client.

🧩 Network Details


Protocol: TCP


IP Address: 127.0.0.1 (localhost)


Port: 5000


Use Wireshark to capture the communication with the following display filter:
tcp.port == 5000


📸 Wireshark Example

The Wireshark capture should show TCP packets (SYN, SYN-ACK, ACK, Data) exchanged between the client and server on port 5000.
You can attach wireshark_capture.png in the repository for documentation.


📂 Project Structure
Echo-Server-Lab1/
│
├── server.py      # TCP Server Code
├── client.py      # TCP Client Code
├── wireshark/     # (optional) Screenshot(s)
│   └── capture.png
└── README.md      # Project documentation


👩‍💻 Authors
Hagar Amr
Yossef Hesham
Alexandria National University – Faculty of Computing and Data Science
Computer Networks (00207N) – Fall 2025

🧾 License
This project is created for educational purposes as part of the Computer Networks Lab.

---

## 📄 2) Updated Lab Report (for Word/PDF submission)


Alexandria National University
Faculty of Computing and Data Science
Course: Computer Networks (00207N)
Lab 1 - Introduction to Socket Programming
Students:


Hagar Amr


Yossef Hesham


Instructor: Dr. Mohamed Rezk
Teaching Assistant: Eng. Ahmed Ashraf
Semester: Fall 2025



Introduction



In this lab, a TCP Server and Client were implemented in Python to practice socket programming.
The server and client communicate using the localhost interface (127.0.0.1) on port 5000.
The server processes messages from the client based on the first character:


A: Sorts letters in descending order


C: Sorts letters in ascending order


D: Converts all letters to uppercase


Any other character: Returns the same message





File Structure





server.py : Python TCP Server code


client.py : Python TCP Client code


README.md : GitHub documentation file


wireshark/ : Folder containing screenshots of the captured traffic





Server Code



(Paste your server.py code here)
# your server.py code




Client Code



(Paste your client.py code here)
# your client.py code




How to Run





Open two terminals.


In the first terminal, run:
python server.py



In the second terminal, run:
python client.py



Send test messages such as:
Ahello
Cpython
Dsocket



Type exit to close the connection.





Wireshark Screenshot





Wireshark was started using the Loopback interface (Npcap Loopback Adapter).


The following display filter was applied:
tcp.port == 5000



The captured packets show the connection establishment (SYN, SYN-ACK, ACK) and data exchange between the server and client.


(Insert screenshot here – name suggestion: wireshark_capture.png)



Results and Discussion





The server successfully receives and processes messages from the client.


Wireshark captures confirmed that TCP communication occurred over port 5000.


The project demonstrates understanding of socket creation, connection handling, and message exchange.





Conclusion



The TCP Echo Server and Client were implemented and tested successfully.
Network traffic was captured using Wireshark, proving correct communication between the two programs.



GitHub Repository Link



🔗 https://github.com/HagarAmr/Echo-Server-Lab1

Signatures:
Hagar Amr ___________________
Yossef Hesham _______________
Date: [29/10/2025]

---
.

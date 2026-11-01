# MiniOS: Core Operating System Kernel Simulator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI: Passing](https://img.shields.io/badge/build-passing-brightgreen.svg)](.github/workflows/ci.yml)
[![Domain: Systems](https://img.shields.io/badge/domain-Operating%20Systems-navy.svg)]()
[![Academic: BRACU CSE321](https://img.shields.io/badge/course-CSE%20321-orange.svg)]()

## 📌 Course Context: CSE 321 (Operating System)
*Department of Computer Science and Engineering, BRAC University*  
**Core Principles:** Process Scheduling (Preemptive Round Robin, FCFS), Deadlock Avoidance (Dijkstra's Banker's Algorithm), Virtual Memory Paging, and Page Replacement Dynamics (FIFO vs LRU).

---

## 🎯 Kernel Subsystems Implemented

1. **CPU Scheduler:**
   - Round-Robin scheduling with fixed time quantum $q$.
   - Real-time calculation of Turnaround Time ($TAT = T_{finish} - T_{arrival}$) and Waiting Time ($WT = TAT - T_{burst}$).
   - Step-by-step ASCII Gantt chart timeline generation.
2. **Banker's Deadlock Avoidance Algorithm:**
   - Evaluates Safety Criterion: checks if resources can be allocated without inducing circular wait states.
   - Computes dynamic Need Matrix: $\text{Need}[i][j] = \text{Max}[i][j] - \text{Allocation}[i][j]$.
3. **Paging & Page Replacement:**
   - Evaluates FIFO and LRU algorithms across reference strings.
   - Quantitative page fault frequency and hit rate analysis.

---

## 🚀 Quickstart & Testing
```bash
# Run demonstration
python main.py

# Run unit tests
python -m unittest discover -s tests
```

"""
Demonstration of MiniOS: CPU Scheduling, Banker's Deadlock Avoidance, and Page Replacement.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.cpu_scheduler import CPUScheduler, Process
from src.deadlock import BankersAlgorithm
from src.memory_manager import fifo_page_replacement, lru_page_replacement

def main():
    print("=" * 65)
    print("        MINIOS: OPERATING SYSTEM CONCEPTS LABORATORY          ")
    print("=" * 65)

    # 1. Round Robin CPU Scheduling
    processes = [
        Process("P1", arrival_time=0, burst_time=5),
        Process("P2", arrival_time=1, burst_time=3),
        Process("P3", arrival_time=2, burst_time=1),
        Process("P4", arrival_time=3, burst_time=2),
    ]
    procs, gantt = CPUScheduler.round_robin(processes, quantum=2)
    print("[+] Round Robin CPU Scheduling (Quantum = 2):")
    gantt_str = " -> ".join(f"[{pid}: {s}-{e}]" for pid, s, e in gantt)
    print(f"    Gantt Chart: {gantt_str}")

    avg_wait = sum(p.waiting_time for p in procs) / len(procs)
    avg_ta = sum(p.turnaround_time for p in procs) / len(procs)
    print(f"    - Avg Waiting Time: {avg_wait:.2f} ms")
    print(f"    - Avg Turnaround Time: {avg_ta:.2f} ms")

    # 2. Banker's Deadlock Avoidance Algorithm
    # 5 Processes (P0..P4), 3 Resource Types (A, B, C)
    alloc = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    max_c = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    avail = [3, 3, 2]

    banker = BankersAlgorithm(alloc, max_c, avail)
    is_safe, seq = banker.is_safe()
    print(f"\n[+] Banker's Deadlock Avoidance:")
    print(f"    - System State Safe: {is_safe}")
    if is_safe:
        print(f"    - Valid Safe Sequence: {' -> '.join(f'P{p}' for p in seq)}")

    # 3. Virtual Memory Page Replacement
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    fifo_faults, fifo_rate = fifo_page_replacement(pages, num_frames=3)
    lru_faults, lru_rate = lru_page_replacement(pages, num_frames=3)
    print(f"\n[+] Page Replacement (20 Page References, 3 Frames):")
    print(f"    - FIFO Faults: {fifo_faults} ({fifo_rate:.1f} %)")
    print(f"    - LRU  Faults: {lru_faults} ({lru_rate:.1f} %)")
    print("=" * 65)

if __name__ == "__main__":
    main()

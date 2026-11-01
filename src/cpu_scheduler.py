"""
CPU Scheduling Suite: FCFS, Preemptive SJF/SRTF, Priority, Round Robin.
Generates Waiting Time, Turnaround Time, and ASCII Gantt Charts.
"""
from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class Process:
    pid: str
    arrival_time: int
    burst_time: int
    priority: int = 0
    remaining_time: int = 0
    start_time: int = -1
    finish_time: int = 0
    waiting_time: int = 0
    turnaround_time: int = 0

class CPUScheduler:
    @staticmethod
    def fcfs(processes: List[Process]) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
        """First-Come, First-Served."""
        procs = sorted(processes, key=lambda p: p.arrival_time)
        time = 0
        gantt = []
        for p in procs:
            if time < p.arrival_time:
                time = p.arrival_time
            start = time
            p.waiting_time = time - p.arrival_time
            time += p.burst_time
            p.finish_time = time
            p.turnaround_time = p.finish_time - p.arrival_time
            gantt.append((p.pid, start, time))
        return procs, gantt

    @staticmethod
    def round_robin(processes: List[Process], quantum: int = 2) -> Tuple[List[Process], List[Tuple[str, int, int]]]:
        """Preemptive Round Robin with fixed time quantum."""
        for p in processes:
            p.remaining_time = p.burst_time

        procs = sorted(processes, key=lambda p: p.arrival_time)
        queue = []
        time = 0
        gantt = []
        p_idx = 0
        n = len(procs)
        completed = 0

        while completed < n:
            while p_idx < n and procs[p_idx].arrival_time <= time:
                queue.append(procs[p_idx])
                p_idx += 1

            if not queue:
                if p_idx < n:
                    time = procs[p_idx].arrival_time
                    continue
                break

            curr = queue.pop(0)
            exec_time = min(quantum, curr.remaining_time)
            gantt.append((curr.pid, time, time + exec_time))
            time += exec_time
            curr.remaining_time -= exec_time

            while p_idx < n and procs[p_idx].arrival_time <= time:
                queue.append(procs[p_idx])
                p_idx += 1

            if curr.remaining_time > 0:
                queue.append(curr)
            else:
                curr.finish_time = time
                curr.turnaround_time = curr.finish_time - curr.arrival_time
                curr.waiting_time = curr.turnaround_time - curr.burst_time
                completed += 1

        return procs, gantt

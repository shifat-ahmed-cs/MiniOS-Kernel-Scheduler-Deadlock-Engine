"""
Unit tests for MiniOS CPU Scheduling, Banker's algorithm, and page replacement.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.cpu_scheduler import CPUScheduler, Process
from src.deadlock import BankersAlgorithm
from src.memory_manager import fifo_page_replacement, lru_page_replacement

class TestOperatingSystems(unittest.TestCase):
    def test_fcfs(self):
        p1 = Process("P1", 0, 4)
        p2 = Process("P2", 1, 3)
        res, gantt = CPUScheduler.fcfs([p1, p2])
        self.assertEqual(res[0].waiting_time, 0)
        self.assertEqual(res[1].waiting_time, 3)

    def test_banker_safe_state(self):
        alloc = [[1, 0], [0, 1]]
        max_c = [[2, 1], [1, 2]]
        avail = [1, 1]
        b = BankersAlgorithm(alloc, max_c, avail)
        safe, seq = b.is_safe()
        self.assertTrue(safe)
        self.assertEqual(len(seq), 2)

    def test_page_replacement(self):
        stream = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
        faults_fifo, _ = fifo_page_replacement(stream, 3)
        faults_lru, _ = lru_page_replacement(stream, 3)
        self.assertTrue(faults_fifo > 0)
        self.assertTrue(faults_lru > 0)

if __name__ == "__main__":
    unittest.main()

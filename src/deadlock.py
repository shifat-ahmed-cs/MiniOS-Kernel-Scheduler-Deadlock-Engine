"""
Banker's Algorithm for Deadlock Avoidance in Multi-Resource Systems.
"""
from typing import List, Tuple, Optional

class BankersAlgorithm:
    def __init__(self, allocation: List[List[int]], max_claim: List[List[int]], available: List[int]):
        self.allocation = [row[:] for row in allocation]
        self.max_claim = [row[:] for row in max_claim]
        self.available = available[:]
        self.num_procs = len(allocation)
        self.num_resources = len(available)
        self.need = [
            [self.max_claim[p][r] - self.allocation[p][r] for r in range(self.num_resources)]
            for p in range(self.num_procs)
        ]

    def is_safe(self) -> Tuple[bool, List[int]]:
        """Determines if the system is in a safe state, returning a safe execution sequence."""
        work = self.available[:]
        finish = [False] * self.num_procs
        safe_seq = []

        for _ in range(self.num_procs):
            found = False
            for p in range(self.num_procs):
                if not finish[p]:
                    if all(self.need[p][r] <= work[r] for r in range(self.num_resources)):
                        for r in range(self.num_resources):
                            work[r] += self.allocation[p][r]
                        finish[p] = True
                        safe_seq.append(p)
                        found = True
                        break
            if not found:
                return False, []
        return True, safe_seq

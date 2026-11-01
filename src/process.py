"""
Process class for OS simulation.
Represents a process with all relevant attributes for scheduling and management.
"""
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Process:
    """Represents an OS process with scheduling-related attributes."""
    pid: int                        # Process ID
    name: str                       # Process name
    arrival_time: int               # Time when process arrives in ready queue
    burst_time: int                 # CPU burst time required
    priority: int = 0               # Priority (lower number = higher priority)
    deadline: Optional[int] = None  # Deadline for real-time scheduling

    # Computed fields (set by scheduler)
    start_time: Optional[int] = field(default=None, repr=False)
    finish_time: Optional[int] = field(default=None, repr=False)
    waiting_time: Optional[int] = field(default=None, repr=False)
    turnaround_time: Optional[int] = field(default=None, repr=False)
    response_time: Optional[int] = field(default=None, repr=False)

    # Internal tracking
    remaining_time: int = field(default=0, repr=False)
    first_response: bool = field(default=False, repr=False)

    def __post_init__(self):
        self.remaining_time = self.burst_time

    def reset(self):
        """Reset computed fields for re-scheduling."""
        self.remaining_time = self.burst_time
        self.start_time = None
        self.finish_time = None
        self.waiting_time = None
        self.turnaround_time = None
        self.response_time = None
        self.first_response = False

    def compute_metrics(self):
        """Compute derived scheduling metrics after scheduling is complete."""
        if self.finish_time is not None and self.start_time is not None:
            self.turnaround_time = self.finish_time - self.arrival_time
            self.waiting_time = self.turnaround_time - self.burst_time
            if self.response_time is None:
                self.response_time = self.start_time - self.arrival_time

    def __repr__(self) -> str:
        return (f"Process(pid={self.pid}, name={self.name!r}, "
                f"arrival={self.arrival_time}, burst={self.burst_time}, "
                f"priority={self.priority})")


def create_processes(data: List[dict]) -> List['Process']:
    """
    Factory function to create a list of Process objects from a list of dicts.

    Args:
        data: List of dicts with keys: pid, name, arrival_time, burst_time, priority

    Returns:
        List of Process objects

    Example:
        >>> procs = create_processes([
        ...     {"pid": 1, "name": "P1", "arrival_time": 0, "burst_time": 5, "priority": 1},
        ...     {"pid": 2, "name": "P2", "arrival_time": 2, "burst_time": 3, "priority": 2},
        ... ])
    """
    return [Process(**d) for d in data]

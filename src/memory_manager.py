"""
Virtual Memory Page Replacement Algorithms: FIFO and Least Recently Used (LRU).
"""
from typing import List, Tuple

def fifo_page_replacement(page_stream: List[int], num_frames: int) -> Tuple[int, float]:
    """First-In, First-Out page replacement. Returns (page_faults, fault_rate)."""
    frames: List[int] = []
    faults = 0

    for page in page_stream:
        if page not in frames:
            faults += 1
            if len(frames) == num_frames:
                frames.pop(0)
            frames.append(page)

    return faults, (faults / len(page_stream) * 100.0) if page_stream else 0.0

def lru_page_replacement(page_stream: List[int], num_frames: int) -> Tuple[int, float]:
    """Least Recently Used page replacement."""
    frames: List[int] = []
    faults = 0

    for page in page_stream:
        if page in frames:
            frames.remove(page)
            frames.append(page)
        else:
            faults += 1
            if len(frames) == num_frames:
                frames.pop(0)
            frames.append(page)

    return faults, (faults / len(page_stream) * 100.0) if page_stream else 0.0

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fibonacci Sequence Generator"""

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

if __name__ == "__main__":
    n = 5
    fib_sequence = fibonacci(n)
    print(f"First {n} Fibonacci numbers:")
    print(fib_sequence)

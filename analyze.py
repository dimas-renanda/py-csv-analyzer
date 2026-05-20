#!/usr/bin/env python3
"""Analyze CSV files and print descriptive stats."""
import sys, csv, statistics
from collections import Counter

def analyze(path):
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows: print("Empty file."); return
    print(f"\n📄 {path}")
    print(f"   Rows: {len(rows)}  |  Columns: {len(rows[0])}\n")
    for col in rows[0].keys():
        vals = [r[col] for r in rows if r[col].strip()]
        print(f"── {col} ({len(vals)} non-empty)")
        nums = []
        for v in vals:
            try: nums.append(float(v))
            except: pass
        if nums:
            print(f"   min={min(nums):.2f}  max={max(nums):.2f}  mean={statistics.mean(nums):.2f}  stdev={statistics.stdev(nums):.2f if len(nums)>1 else 0:.2f}")
        else:
            top = Counter(vals).most_common(3)
            print(f"   top values: {', '.join(f'{v}({c})' for v,c in top)}")
    print()

if len(sys.argv) < 2: print("Usage: analyze.py <file.csv>"); sys.exit(1)
analyze(sys.argv[1])

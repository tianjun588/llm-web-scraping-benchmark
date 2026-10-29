#!/usr/bin/env python3
"""
Simple Web Scraping & Proxy Benchmark Tool (2026 Edition)
Measures response time and status codes against target endpoints.
"""

import time
import requests

TARGETS = [
    {"name": "HTTPBin (Control)", "url": "https://httpbin.org/get"},
]

def test_connection():
    print("=" * 60)
    print("  🚀 Scraping & Proxy Benchmark Runner (2026 Live Edition)")
    print("=" * 60)
    for target in TARGETS:
        start = time.time()
        try:
            resp = requests.get(target["url"], timeout=10)
            latency = round((time.time() - start) * 1000, 2)
            print(f"[{resp.status_code}] {target['name']} -> Latency: {latency} ms")
        except Exception as e:
            print(f"[FAIL] {target['name']} -> Error: {e}")
    print("=" * 60)
    print("Benchmark complete. Review README.md for provider ratings.")

if __name__ == "__main__":
    test_connection()

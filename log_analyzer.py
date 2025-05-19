import re
import time
from datasketch import HyperLogLog


def extract_ips_from_log(filepath):
    ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    ip_list = []

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            match = ip_pattern.search(line)
            if match:
                ip_list.append(match.group())

    return ip_list


def count_unique_ips_exact(ip_list):
    start = time.perf_counter()
    unique_ips = set(ip_list)
    duration = time.perf_counter() - start
    return len(unique_ips), duration


def count_unique_ips_hll(ip_list, precision=0.01):
    unique_count = len(set(ip_list)) 
    p_value = 5 if unique_count < 100 else 14
    hll = HyperLogLog(p=p_value)

    start = time.perf_counter()
    for ip in ip_list:
        if isinstance(ip, str) and ip.strip():
            hll.update(ip.encode('utf-8'))
    duration = time.perf_counter() - start
    return len(hll), duration



vulns = [
    {"title": "SQL Injection", "severity": 9},
    {"title": "XSS", "severity": 6},
    {"title": "Broken Auth", "severity": 8},
]

ordenados = sorted(vulns, key=lambda v: v["severity"], reverse=True)
for v in ordenados:
    print(v["title"], "-", v["severity"])
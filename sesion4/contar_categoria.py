vulns = [
    {"title": "SQL Injection", "owasp_category": "A03"},
    {"title": "XSS", "owasp_category": "A03"},
    {"title": "Broken Auth", "owasp_category": "A07"},
]

conteo = {}
for v in vulns:
    cat = v["owasp_category"]
    conteo[cat] = conteo.get(cat, 0) + 1

print(conteo)  # {'A03': 2, 'A07': 1}
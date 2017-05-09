import yaml
import re


cradle = yaml.load("""
- 2
- +
-
    - 4
    - +
    - 5
""")

print cradle

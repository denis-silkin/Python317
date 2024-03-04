# Homework_17
import re

s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
res = r'[+]?7\d{10}'
print(re.findall(res, s))

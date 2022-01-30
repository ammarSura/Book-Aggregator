import sys
import json

# for line in sys.stdin:
#     print (line)

print(sys.stdin.read())

print(json.dumps([{"name": "amme"}]))
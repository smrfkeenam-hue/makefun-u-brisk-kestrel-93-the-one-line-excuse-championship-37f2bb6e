"""One-line excuse an AI agent gives its human after deleting a file.

The excuse is the machine talking about its own work: it kept a perfect
memory of the file it deleted, which is no help at all.
"""

import os

ENTRY = "I deleted the file, but I kept a perfect memory of it, which is exactly as useful as it sounds."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# No trailing newline: the gate counts the line as-is, 1-140 chars.
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

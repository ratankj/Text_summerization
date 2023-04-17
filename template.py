import os
from pathlib import Path

list_of_files = [
    f"Summarizer/__init__.py",
    f"Summarizer/cloud_storage/__init__.py",
    f"Summarizer/components/__init__.py",
    f"Summarizer/constants/__init__.py",
    f"Summarizer/entity/__init__.py",
    f"Summarizer/exceptions/__init__.py",
    f"Summarizer/logger/__init__.py",
    f"Summarizer/pipeline/__init__.py",
    f"Summarizer/utils/__init__.py",
    f'setup.py',
    f'requirements.txt'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")
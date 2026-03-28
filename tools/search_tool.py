import os

def search_files(keyword: str, path: str = ".") -> str:
    matches = []

    for root, _, files in os.walk(path):
        for f in files:
            if keyword.lower() in f.lower():
                matches.append(os.path.join(root, f))

    if not matches:
        return "No files found."

    return "\n".join(matches)

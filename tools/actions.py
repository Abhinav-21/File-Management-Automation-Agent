from pathlib import Path

def create_text_file(path: str, content: str):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    return f"File created at {path}"

def list_files(path: str):
    p = Path(path)
    return [str(x) for x in p.iterdir()]

def delete_file(path: str):
    Path(path).unlink(missing_ok=True)
    return f"Deleted {path}"

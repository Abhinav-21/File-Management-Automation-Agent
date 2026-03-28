import subprocess

def run_python(file: str) -> str:
    try:
        result = subprocess.run(
            f'python "{file}"',
            shell=True,
            capture_output=True,
            text=True,
            timeout=600
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

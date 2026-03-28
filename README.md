# File Management Automation Agent
Python automation tool for intelligent file organization using rule-based sorting with optional AI fallback.

## Features
- Auto-sorts files from configured folders into category destinations.
- Rule-based classification by file extension (`images`, `documents`, `code`, `archives`).
- Optional AI fallback classification with Ollama when no rule matches.
- Real-time watcher mode for newly created files.
- Scheduled scan mode (every N hours).
- One-time scan mode (`--once`).
- Undo last run (`--undo`) based on logged move history.
- Natural language command mode (routes prompts to tool actions via local LLM).
- Dry-run support (preview moves without changing files).

## Requirements
- Python 3.10+ (project has been tested with Python 3.14).
- Ollama installed and running locally.
- Ollama model pulled:
  - `qwen2.5:7b`

Python dependencies are listed in `requirements.txt`:
- `ollama`
- `PyYAML`
- `watchdog`

## Setup
1. Clone the repository and go to the project folder.
2. Create and activate a virtual environment.
3. Install Python dependencies.
4. Install/start Ollama and pull the model.

```powershell
# 1) create venv
python -m venv .venv

# 2) activate (PowerShell)
.\.venv\Scripts\Activate.ps1

# 3) install dependencies
pip install -r requirements.txt

# 4) prepare Ollama model
ollama pull qwen2.5:7b
```

## Configuration
Edit `config.yaml` to control behavior:
- `watch_folders`: folders to scan/watch.
- `exclude_folders`: folders to ignore.
- `rules`: extension-to-category mapping.
- `destinations`: output folders per category.
- `schedule_hours`: interval for scheduler mode.
- `ai_enabled`: enable/disable AI fallback.
- `dry_run`: if `true`, files are not moved.

Example:
```yaml
watch_folders:
  - "D:/Downloads"

rules:
  images: ["jpg", "png", "jpeg"]
  documents: ["pdf", "docx", "txt"]
```

## How To Use

### 1) Scheduler mode (default)
Runs forever, scanning every `schedule_hours`.
```powershell
python run.py
```

### 2) Single scan
Runs one scan and exits.
```powershell
python run.py --once
```

### 3) Undo last run
Reverts file moves from the most recent logged run.
```powershell
python run.py --undo
```

### 4) Natural language mode
Pass a prompt and let the local LLM pick a tool/action.
```powershell
python run.py "list files in D:/Downloads"
python run.py "create a text file notes.txt with hello"
```

### 5) Interactive assistant mode
Starts a prompt loop for tool execution.  
Special command: `start file watcher`
```powershell
python main.py
```

## Logs and Undo Data
- Move log file: `file_manager/file_log.txt`
- Undo metadata: `file_manager/last_run.json`

## Notes
- If AI classification is off (`ai_enabled: false`), unknown files go to `others`.
- If `dry_run: true`, moves are only printed and not executed.
- Make sure all destination folders in `config.yaml` are valid for your system.
- Current source files load config/log paths using an `agent/...` prefix. If your project is at repository root, either:
  - move files under an `agent/` folder, or
  - update those hardcoded paths to root-relative paths (for example `config.yaml`, `file_manager/file_log.txt`).

# MVC Calculator (Pygame)

A basic arithmetic calculator (**+ - * /**) built using the **MVC design pattern** with **Pygame**.

## Features
- Buttons: `0-9`, `+ - * /`, `(`, `)`, `.`, `=`, `C` (clear), `⌫` (backspace)
- Keyboard input supported:
  - Digits/operators/parentheses/dot
  - `Enter` → calculate (`=`)
  - `Backspace` → delete last char (`⌫`)
  - `Delete` → clear (`C`)
  - `Esc` → quit
- Error handling (invalid expression, division by zero)

## Project Structure (MVC)
- `model.py` — **Model**: `Calculator` class (expression + methods)
- `view.py` — **View**: draws the interface and buttons
- `controller.py` — **Controller**: handles events and updates model/view
- `run.py` — entry point

## Install & Run
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python run.py
```

## Notes
The original assignment mentioned PyQt, but this implementation follows the same MVC requirements using **Pygame** as requested.

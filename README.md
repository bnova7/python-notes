# Python Notes

A command-line note taking app built with Python and SQLite.

## Features

- Add notes with a title and content
- View all notes
- View a note by ID
- Delete a note by ID

## Requirements

- Python 3
- [Rich](https://github.com/Textualize/rich)

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install rich
```

## Usage

```bash
python main.py
```

## Running Tests

```bash
python -m unittest tests/test.py
```

## Project Structure

```
python-notes/
├── main.py       # entry point and menu
├── db.py         # database connection and table setup
├── write.py      # add notes
├── view.py       # retrieve and display notes
├── delete.py     # delete notes
└── tests/
    └── test.py   # unit tests
```

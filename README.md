# OpenSEM

OpenSEM is a light-weight framework for creating Small Expert Models. It provides simple commands to initialize workspaces, create projects, add data, and manage configurations.

## Features
- Initialize SEM workspace
- Create new SEM projects
- Add data files to projects
- Manage project configurations and models
- Delete projects safely

## Getting Started

### Prerequisites
- Python 3.7+
- (Optional) Create a virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Usage
All commands are run from the project root using the CLI entry point `opensem.py`:

#### 1. Initialize the workspace
```bash
python opensem.py init
```

#### 2. Create a new SEM project
```bash
python opensem.py new <project_name>
```
Example:
```bash
python opensem.py new testsem
```

#### 3. Add data to your project
```bash
python opensem.py add-data <file_or_folder>
```
Example:
```bash
python opensem.py add-data war-and-peace.pdf
```

#### 4. List all projects
```bash
python opensem.py list-projects
```

#### 5. Delete a project
```bash
python opensem.py delete <project_name>
```

## Project Structure
```
OpenSEM/
├── configs/
├── data/
├── models/
├── src/
│   └── opensem_cli.py
├── opensem.py
├── requirements.txt
```

## Contributing
Pull requests and issues are welcome!

## License
MIT

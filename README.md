# Calculator Project - Software Development Practices

A simple Python calculator built to learn **Git**, **Continuous Integration (CI)**, and **Quality Assurance (QA)** practices.

## Project Structure

```
calculator_project/
├── calculator/
│   ├── __init__.py
│   ├── basic.py        # Basic operations: add, subtract, multiply, divide
│   ├── advanced.py     # Advanced operations: power, sqrt, modulo, factorial
│   └── utils.py        # Input validation utilities
├── tests/
│   ├── test_basic.py
│   ├── test_advanced.py
│   └── test_utils.py
├── .github/workflows/
│   └── ci.yml          # GitHub Actions CI pipeline
├── .flake8              # Linter configuration
├── requirements.txt     # Python dependencies
├── QA_report.md         # Quality Assurance report template
├── Reflection_report.md # Personal reflection template
└── README.md            # This file
```

---

## Part 1: Version Control with Git

### Getting Started

```bash
# 1. Initialize the repository
git init
git add .
git commit -m "Initial commit: add calculator project"

# 2. Create a remote repository on GitHub, then connect it
git remote add origin https://github.com/YOUR_USERNAME/calculator_project.git
git branch -M main
git push -u origin main
```

### Branching Workflow

```bash
# Create a feature branch
git checkout -b feature/new-operation

# Make changes, stage, and commit
git add .
git commit -m "Add new operation: ..."

# Push the branch
git push -u origin feature/new-operation

# Create a pull request on GitHub, then merge to main
git checkout main
git pull origin main
```

### Resolving Merge Conflicts

1. When a conflict occurs, open the conflicting file.
2. Look for `<<<<<<<`, `=======`, and `>>>>>>>` markers.
3. Edit the file to keep the correct code.
4. Remove the conflict markers.
5. Stage, commit, and push the resolved file.

---

## Part 2: Continuous Integration (CI)

The CI pipeline is defined in `.github/workflows/ci.yml` and runs automatically on every push and pull request.

**What the pipeline does:**

1. Checks out the code
2. Sets up Python 3.11
3. Installs dependencies (`pytest`, `flake8`)
4. Runs `flake8` to check code style
5. Runs `pytest` to execute all tests
6. Reports failure if any step fails

### Try It

1. Push changes to GitHub.
2. Go to your repository → **Actions** tab.
3. Watch the pipeline run and see if it passes or fails.

---

## Part 3: Quality Assurance (QA)

### Running Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/ -v

# Run a specific test file
pytest tests/test_basic.py -v
```

### Running the Linter

```bash
# Check code style
flake8 calculator/ tests/

# Auto-fix some issues (install autopep8 first)
pip install autopep8
autopep8 --in-place --recursive calculator/ tests/
```

### Peer Code Review Process

1. Push a feature branch and open a pull request on GitHub.
2. Assign a peer as reviewer.
3. Reviewer checks:
   - Code correctness
   - Edge case handling
   - Code style and readability
   - Test coverage
4. Address feedback and update the PR.
5. Merge after approval.

---

## Setup & Requirements

- Python 3.8+
- Git
- A GitHub account

```bash
pip install -r requirements.txt
```

## License

Educational project — free to use and modify.

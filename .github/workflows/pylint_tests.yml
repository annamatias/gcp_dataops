name: CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install flake8 coverage
          pip install -r requirements.txt
      - name: Lint with flake8
        run: |
          flake8 --ignore=E501 src/ tests/ --exclude=src/notebooks
      - name: Run unit tests and generate coverage report
        run: |
          coverage run -m unittest -v
          coverage report
          coverage html

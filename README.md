# Playwright-Python UI Automation Framework

This project is an end-to-end UI test automation framework built using **Playwright for Python** and **pytest**. It automates login flows, navigation between pages, and key verifications like dropdowns and initializing screens.

## Project Structure

```
playwright-python/
├── pages/                   # Page Object Models (POM)
│   ├── base_page.py
│   ├── login_page.py
│   ├── dispatch_page.py
│   └── initializing_page.py
├── tests/                   # Test cases
│   ├── test_login.py
│   ├── test_dispatch.py
│   └── test_initializing.py
├── reports/                 # HTML test reports (pytest-html)
├── .gitignore
├── pytest.ini               # Pytest config file
├── conftest.py              # Pytest fixtures
├── requirements.txt         # Dependency list
```

## Features

- Built with **Playwright Python** + **Pytest**
- Uses **Page Object Model (POM)** for scalability
- Easily tag and run test groups using `@pytest.mark`
- Supports HTML reporting via `pytest-html`

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run tests

```bash
pytest --html=reports/report.html
```

### 3. View HTML report

Open `reports/report.html` in your browser.

### 4. Run specific test by tag

```bash
pytest -m smoke --html=reports/smoke-report.html
```


## Requirements

- Python 3.8+
- Playwright
- Pytest
- pytest-playwright
- pytest-html

Install Playwright dependencies:

```bash
playwright install
```

## Clean Up

Remove HTML reports or cache:

```bash
rm -rf reports/ .pytest_cache/
```
# Internet Tests Framework
This repos provides a framework to run tests against test portal of Internet Test.

## ⚙️ Setup Instructions

### Step 1: Clone the project

```bash
git clone https://github.com/ArlindaHaliti1/internet-testing-with-playwright.git
cd internet-testing-with-playwright
```

### Step 2: Create and activate a virtual environment


#### For Linux and Mac:
```bash
python3 -m pip install --user virtualenv
python3 -m venv .venv
source .venv/bin/activate
```

#### For Windows:
```bash
python -m pip install --user virtualenv
python -m venv venv
.\venv\Scripts\activate
```

### Step 3: Install Poetry

```bash
pip install poetry
```

### Step 4: Install Project Dependencies

```bash
poetry install --no-root
```

### Step 5: Install playwright

```bash
playwright install
```

## 🏃‍♂️ Running Tests
### Framework unittests
```bash
cd unitests && pytest .
```

### End-to-End Tests
```bash
pytest testsuite
```

When no browser was selected then chrome will be used.

* Run according to tags:

```bash
pytest -m <tag_name>
```


## 📊 Viewing Test Results


### View trace results:

```bash
 playwright show-trace test-results/failed_test/trace.zip
```
## ℹ️ View Help And Other CLI Options

```bash
pytest --help
```

### Pre Commit

#### Run Pre Commit Checks Automatically

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```


#### Run Pre Commit Checks Manually On The Entire Project

```bash
pre-commit run --all-files
```

## 🛠️ Tech Stack

| Tool                                                                     | Description                                                                                 |
|--------------------------------------------------------------------------|                               |
| [axe-playwright-python](https://pypi.org/project/axe-playwright-python/) | Python library for running accessibility checks with Playwright                             |
| [playwright](https://pypi.org/project/playwright/)                       | Python library to automate the Chromium, WebKit, and Firefox browsers through a single API. |
| [pytest](https://pypi.org/project/pytest/)                               | Popular testing framework for Python                                                        |
| [pytest-base-url](https://pypi.org/project/pytest-base-url/)             | Pytest plugin for setting a base URL for your tests                                         |
| [pytest-playwright](https://pypi.org/project/pytest-playwright/)         | Pytest plugin for Playwright integration for browser automation testing                     |
| [requests](https://pypi.org/project/requests/)                           | Versatile library for making HTTP requests in Python                                        |

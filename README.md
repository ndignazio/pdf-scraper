# pdf-scraper

This repository includes a Python parser that scrapes PDF files linked in a webpage and saves them to a local directory. It was created for the purpose of downloading readings automatically from a course webpage, but should work for other use cases.

Both absolute URL paths and relative paths to files should work successfully as long as they exist and end in "pdf".

If the directory you would like to save the files to does not exist, a new filepath will be created.

## Setup

In your preferred directory, clone the repository:

```bash
git clone https://github.com/ndignazio/transit-ml.git
```
Install required packages in a [virtual environment](https://docs.python.org/3/tutorial/venv.html):

```bash
pip3 install -r requirements.txt
```
## Usage

In a Linux terminal, use the following syntax:
```bash
python3 parser.py {url} {filepath}
```
A URL is required; a filepath is optional.

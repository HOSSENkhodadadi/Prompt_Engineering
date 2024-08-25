# Car Information Extractor

This project reads a PDF file containing information about various car models and extracts this information into a structured JSON format using the LLaMA 3.1 model for prompt engineering.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
  - [Step 1: Install Python and Pip](#step-1-install-python-and-pip)
  - [Step 2: Install Required Python Packages](#step-2-install-required-python-packages)
  - [Step 3: Install Ollama](#step-3-install-ollama)
  - [Step 4: Install LLaMA 3.1 Model](#step-4-install-llama-31-model)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Overview

The purpose of this script is to:

1. Read a PDF file containing car information.
2. Extract textual data from the PDF.
3. Use the LLaMA 3.1 model to process the extracted text and structure it into a JSON format.
4. Save the JSON data to a file for further use or analysis.

## Installation

### Step 1: Install Python and Pip

Make sure you have Python 3.6 or later installed. You can download Python from the official [Python website](https://www.python.org/).

Pip is typically included with Python installations. If it's not installed, you can find instructions on the [pip installation page](https://pip.pypa.io/en/stable/installation/).

### Step 2: Install Required Python Packages

To run the script, you'll need to install the required Python packages. Run the following command to install `PyPDF2` and `ollama` modules:

```bash
pip install PyPDF2 ollama
```

### Step 3: Install Ollama

Ollama is used to interact with the LLaMA 3.1 model. To install Ollama, follow these steps:

1.Visit the Ollama official website.
2.Follow the installation instructions specific to your operating system.

### Step 4: Install LLaMA 3.1 Model

After installing Ollama, you need to install the LLaMA 3.1 model. Run the following command in your terminal or command prompt:

```bash
ollama pull llama3.1:latest
```
### Step 5:Usage
Once you have installed the necessary dependencies and Ollama, you can run the script to extract car information from a PDF file and save it as a JSON file.

Ensure that the PDF file (car_models_report.pdf) is located in the same directory as the script model_extractor_2.py.
Run the script: 
```bash
python model_extractor_2.py
```
3.The JSON output will be saved to car_models_3.json in the same directory.

### License
This project is licensed under the MIT License 






# Human-AI Interaction for Privacy Management - LLM Inference

An automated PII (Personally Identifiable Information) redaction engine powered by LLM, designed to detect and mask sensitive data in documents. This repository contains the prompt engineering and LLM inference component of a capstone project developed in collaboration with Foxit.

## Project Context

This module serves as the **core intelligence layer** of an end-to-end document privacy management system. It receives OCR-extracted document data, applies LLM to identify sensitive information, and returns structured masking coordinates for frontend rendering.

**Complete System Architecture:**
- **OCR Preprocessing**: Document parsing and text extraction
- **LLM Inference (this repo)**: Intelligent PII detection
- **Frontend Masking Interface**: Real-time visualization and user interaction

## Key Features

- **Automated PII Detection**: Identifies names, addresses, SSNs, financial information, and more
- **Few-Shot Learning**: Improves accuracy through contextual examples
- **Multi-Turn Dialogue**: Supports iterative refinement based on user feedback
- **JSON-Based Processing**: Structured I/O for seamless integration

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from prompt_eng import prompt

# Prepare input
input_json = {
    "conversion_type": "first",  # or "continued" for refinement
    "ocr_json": data['pages'][0],
    "user_input": "",  # Empty for initial pass
    "conversation_history": []  # Empty for initial pass
}

# Get PII detection results
result = prompt(input_json)
```

### Testing with Sample Data

```bash
# Place test files in /sample_data folder, then run:
python prompt_eng/test.py BudgetRequestSummary.json
python prompt_eng/test.py California-Standard-Residential-Lease-Agreement-Sophia.json
```

### Multi-Turn Refinement

For iterative refinement, use `conversion_type: "continued"` with custom prompts:

```python
input_json = {
    "conversion_type": "continued",
    "ocr_json": data['pages'][0],
    "user_input": "name and institution only",
    "conversation_history": [...]  # Previous results
}
```

## Project Structure

```
.
├── prompt_eng/
│   ├── prompt.py          # Core prompt engineering logic
│   └── test.py            # Testing script
├── sample_data/           # Test documents
├── requirements.txt
└── README.md
```

## Technical Approach

- **Instruction-based prompting**: Clear, structured instructions for PII identification
- **Few-shot examples**: Contextual examples improve model understanding
- **Zero-shot capability**: Works on new document types without retraining

## Project Contributors
- Prompt Engineering & LLM Inference (this repo): Nina Cheng
- OCR: Zeyu Pan
- Frontend: Shuxiao Yin, Kyle Wang
- Backend: Sophia Yang
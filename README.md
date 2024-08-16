# Human-ai-interaction-for-privacy-management-prompt-eng
The prompt engineering part of the Human AI Interaction for Privacy Management capstone project.

## Installation

```
pip install -r requirements.txt
```

## Usage
### Import prompt function

```
from prompt_eng import prompt

result = prompt(input_json)
```

### You can run `test.py` to see example
- First put the testing JSON file under `/sample_data` folder
- (Optional) You can customize your user prompt in `test.py` for multi-turn dialogue
    - for example, "name and institution only" for `BudgetRequestSummary.json`
- Then run the script with the filename as an argument

```
python prompt_eng/test.py <test file name>

# for example
python prompt_eng/test.py BudgetRequestSummary.json
python prompt_eng/test.py California-Standard-Residential-Lease-Agreement-Sophia.json
```
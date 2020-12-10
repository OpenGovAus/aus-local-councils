# aus-local-councils

This Python packagage returns lists of all local councils in Australia, sorted by state/territory.

A list of all Australian local councils can be found in aus_councils.json

## Setup

Install required packages with **pip3**:

`pip3 install -r requirements.txt`

## Usage

You can get the list of councils for a jurisdiction like this (South Australia is used here for example purposes):

```python
import json
import aus_local_councils.sa

council_list = aus_local_councils.sa.councils

print(json.dumps(council_list, indent=2))
```

This would print out a formatted list of all the local councils in South Australia.
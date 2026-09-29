# Instagram Handle Validator

Python CLI that validates Instagram-style handles.

## Features

- Checks handle length (3 to 30 characters)
- Allows only letters, numbers, periods, and underscores
- Rejects handles that start with a digit
- Suggests alternative handles when the input is invalid
- Requires at least one letter
- Rejects consecutive periods or underscores
- Prints a clear valid or invalid message with the reason

## Tech Used

- Python 3.x
- No external libraries

## How to Run

```bash
git clone https://github.com/harshisonthebook/instagram-handle-validator.git
cd instagram-handle-validator
python validator.py
```

## Example

```
$ python validator.py
enter the username: harsh.dev_01

Username is valid.

$ python validator.py
enter the username: harsh..dev

Username cannot contain consecutive periods or underscores.

Suggestions:
1. harsh..dev_1
2. harsh..dev
3. harsh..dev_yt
```

## What I Learned

- Working with strings: indexing, slicing, and checking characters
- Using conditionals to apply multiple rules in order

## Author

Harsh, BSc CS, Delhi University
[LinkedIn](https://www.linkedin.com/in/harsh-tiwari7)
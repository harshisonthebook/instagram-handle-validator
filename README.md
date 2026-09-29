# Instagram Handle Validator

Python CLI that checks if an Instagram handle follows the platform's rules.

## Features

- Checks handle length (1 to 30 characters)
- Allows only letters, numbers, periods, and underscores
- Rejects handles that start or end with a period
- Rejects consecutive periods
- Prints a clear valid or invalid message with the reason

## Tech Used

- Python 3.x
- No external libraries

## How to Run

```bash
git clone https://github.com/your-username/instagram-handle-validator.git
cd instagram-handle-validator
python main.py
```

## Example

```
$ python main.py
Enter handle: harsh.dev_01
Valid handle

$ python main.py
Enter handle: harsh..dev
Invalid: consecutive periods not allowed
```

## What I Learned

- Working with strings: indexing, slicing, and checking characters
- Using conditionals to apply multiple rules in order

## Author

Harsh, BSc CS, Delhi University
[LinkedIn link]
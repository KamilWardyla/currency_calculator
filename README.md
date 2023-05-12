# Currency calculator

This Python code provides a currency calculator that retrieves exchange rates from the NBP (Narodowy Bank Polski) API and calculates the converted value based on the user's input.

## Setup
```
pip install .
```

## Usage

### Console usage
```
usage: currency [-h] amount currency

positional arguments:
  amount      Amount to convert
  currency    Currency code to convert to

options:
  -h, --help  show this help message and exit
```

```
$ currency 123 EUR

558.96
```

### Python usage
```
>>> from currency_calculator import calculate
>>> calculate(12, "GBP")
62.63
```
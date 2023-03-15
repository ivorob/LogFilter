# LogFilter

## Usage

```
usage: LogFilter.py [-h] filename search regex

positional arguments:
  filename
  search
  regex

optional arguments:
  -h, --help  show this help message and exit
```

## Example of usage
```
LogFilter.py logfile.log processName ' = "([^"]+)"'
```

* Searching all occurrences of string 'processName';
* Applyng regular expression to line: search + regex; 
* In that case: 'processName = "([^"]+)"';
* Using last regular expression group as key to count occurrences;
* Printing occurrences from most popular to less popular.

You can use pipes to filter some results. For example:
```
LogFilter.py logfile.log processName ' = "([^"]+)"' | head -10
```
Print the first 10 results.

```
LogFilter.py logfile.log processName ' = "([^"]+)"' | grep "filter string"
```
Print the results contained "filter string".

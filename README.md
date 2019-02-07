# bmig_5003_count_words
A command-line script by Peter Granderson that loads a file and splits/filters it by word, counts those words, and then outputs to JSON.

# Install
```git clone https://github.com/zpeterg/bmig5003_split_to_words```

# Run
1. ```cd bmig5003_split_to_words```
2. ```python
    python index.py \
        -file=<filename> \
        -start=<start word> \
        -stop=<stop word> \
        -finish=<finish word> \
        <optional: "-f" for formating into columns>
     ```

For example: ```python index.py -file=small_test.txt -start=foo -stop=bar -finish=enough -f```

You may also add new files at the root and change the -file, -start, -stop, -finish above. 

# Run Unit Tests
```python -m unittest discover -p '*test*.py'```
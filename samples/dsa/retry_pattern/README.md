# Retry Pattern

Summary of the *Retry Pattern* and its usage.

## Description

The problem the **Retry Pattern** solves is *Transient Failure*. Most modern systems rely on external services, APIs, databases, large language models, etc. These services sometimes fail briefly, even when your code is correct.

The **Retry Pattern** wraps and *operation* that might fail and automatically *retries* it before giving up. It's a simple way of making your code more robust and fault-tolerant.

## Example

The code is responsible for fetching a random Chuck Norris joke from an *External API*. The example code simulates Transient Failure using the `random` library in Python.

```python
# Randomly raise an exception to simulate a transient error
if random.random() < 0.5:
    raise httpx.HTTPError("Simulated transient error")
```

Execute `before.py` to observe this behavior. The script will only sometimes execute successfully. This is unacceptable if the code is expected to run in production environments.

```sh
# Success
python .\before.py
Chuck Norris has never blinked in his entire life. Never.

# Failure
python .\before.py
Traceback (most recent call last):
  File "C:\Users\cityd\Documents\GitHub\python-samples\samples\dsa\retry_pattern\before.py", line 29, in <module>
    main()
    ~~~~^^
  File "C:\Users\cityd\Documents\GitHub\python-samples\samples\dsa\retry_pattern\before.py", line 25, in main
    print(fetch_joke())
          ~~~~~~~~~~^^
  File "C:\Users\cityd\Documents\GitHub\python-samples\samples\dsa\retry_pattern\before.py", line 16, in fetch_joke
    raise httpx.HTTPError("Simulated transient error")
```

## Solutions

A summary of various solutions to address the problem.

### Retry Function

Lorem ipsum.

### Using a Decorator

Lorem ipsum.

### Using Tenacity (Recommended)

Lorem ipsum.

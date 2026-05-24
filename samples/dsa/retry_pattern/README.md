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

A summary of various solutions to address the problem. These can be implemented as functions that live within utility / library modules that can then be imported on the fly.

### Retry Function

The `retry_function.py` solution defines a **generic function** that executes an *operation* up to a certain number of times with a *fixed* delay.

```python
python .\retry_function.py           
Attempt 1 failed: Simulated transient error
Attempt 2 failed: Simulated transient error
Attempt 3 failed: Simulated transient error
There are two kinds of women in the world; those who have slept with Chuck Norris, and those who want to.
```

### Exponential Backoff

Sometimes retrying a service too quickly may make things worse. You may overload a service or get rate limited (429), so just passing a fixed *delay* is not sufficient.

A solution to this is *Exponential Backoff*, where each retry waits a bit longer than the last, implemented within `retry_exponential_backoff.py`.

```python
python .\retry_exponential_backoff.py
Attempt 1 failed: Simulated transient error
Retrying in 1.00 seconds...
Attempt 2 failed: Simulated transient error
Retrying in 2.00 seconds...
Attempt 3 failed: Simulated transient error
Retrying in 4.00 seconds...
Paul Newman has Chuck Norris's Own salad dressing and mayo.
```

### Using a Decorator

This example imlpements the solution as a Decorator, which enables us to add it to any function with ease.

### Using Tenacity (Recommended)

For production-ready code, there is a library named *Tenacity* that is excellent at handling this.

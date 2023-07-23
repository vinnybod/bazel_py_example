# bazel_py_example

I ran these tests on an M1 Macbook Pro.

## Setup

```
bazel test //...
```

## Vanilla rules_python

In PyCharm:
* Run the `vanilla/main_test` target
* Debug the `vanilla/main_test` target
* Observe that the PyCharm debugger hangs on the call to `pytest.main()`
* Change the `pytest.main()` call to `add_test()` and observe that the PyCharm debugger works

## rules_py

In PyCharm:
* Run the `rules_py/main_test` target
* Debug the `rules_py/main_test` target
* Observe that the PyCharm debugger fails in PyCharm internal code.
`/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/_pydev_imps/_pydev_execfile.py`
* Swapping the `pytest.main()` call to `add_test()` does not fix the issue

```
Traceback (most recent call last):
  File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevd.py", line 1496, in _exec
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
  File "/private/var/tmp/_bazel_vinnybod/374e1bb7722987713a370205d81b8179/execroot/__main__/bazel-out/darwin_arm64-fastbuild/bin/rules_py/main_test", line 5
    set -uo pipefail; f=bazel_tools/tools/bash/runfiles/runfiles.bash
            ^
SyntaxError: invalid syntax
```

## rules_py with pytest rule

This generates the same error as the previous.
But there is a benefit to using it, which is that the `pytest` rule takes care of the 
boilerplate that is required to run `pytest` from a Bazel test seen in the other two.

In PyCharm:
* Run the `rules_py/main_test` target
* Debug the `rules_py/main_test` target
# TODO Where is it failing if it doesn't have the boilerplate
* Observe that the PyCharm debugger fails in PyCharm internal code.
`/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/_pydev_imps/_pydev_execfile.py`

```
Traceback (most recent call last):
  File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevd.py", line 1496, in _exec
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
  File "/private/var/tmp/_bazel_vinnybod/374e1bb7722987713a370205d81b8179/execroot/__main__/bazel-out/darwin_arm64-fastbuild/bin/rules_py/main_test", line 5
    set -uo pipefail; f=bazel_tools/tools/bash/runfiles/runfiles.bash
            ^
SyntaxError: invalid syntax
```

## rules_python_pytest

This also has errors in the PyCharm debugger, but it is a different error than the previous two.
This rule also takes care of the boilerplate that is required to run `pytest` from a Bazel test.

In PyCharm:
* Run the `rules_python_pytest/main_test` target
* Debug the `rules_python_pytest/main_test` target
* Observe that the PyCharm debugger fails

```
=============================== warnings summary ===============================
private/var/tmp/_bazel_vinnybod/374e1bb7722987713a370205d81b8179/execroot/__main__/bazel-out/darwin_arm64-fastbuild/bin/rules_python_pytest/test_main.runfiles/pip_pytest/site-packages/_pytest/cacheprovider.py:451
  /private/var/tmp/_bazel_vinnybod/374e1bb7722987713a370205d81b8179/execroot/__main__/bazel-out/darwin_arm64-fastbuild/bin/rules_python_pytest/test_main.runfiles/pip_pytest/site-packages/_pytest/cacheprovider.py:451: PytestCacheWarning: could not create cache path /.pytest_cache/v/cache/nodeids: [Errno 30] Read-only file system: '/.pytest_cache'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

private/var/tmp/_bazel_vinnybod/374e1bb7722987713a370205d81b8179/execroot/__main__/bazel-out/darwin_arm64-fastbuild/bin/rules_python_pytest/test_main.runfiles/pip_pytest/site-packages/_pytest/stepwise.py:56
  /private/var/tmp/_bazel_vinnybod/374e1bb7722987713a370205d81b8179/execroot/__main__/bazel-out/darwin_arm64-fastbuild/bin/rules_python_pytest/test_main.runfiles/pip_pytest/site-packages/_pytest/stepwise.py:56: PytestCacheWarning: could not create cache path /.pytest_cache/v/cache/stepwise: [Errno 30] Read-only file system: '/.pytest_cache'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================= 2 warnings in 0.00s ==============================
ERROR: file or directory not found: rules_python_pytest/main_test.py
```
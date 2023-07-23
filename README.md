# bazel_py_example

## Setup

```
bazel test //...
```

## Vanilla rules_python

In PyCharm:
* Run the `vanilla/main_test` target
* Debug the `vanilla/main_test` target
* Observe that the PyCharm debugger hangs on the call to `pytest.main()`

## rules_py

In PyCharm:
* Run the `rules_py/main_test` target
* Debug the `rules_py/main_test` target
* Observe that the PyCharm debugger fails on the call to `pytest.main()`
* 
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
* Observe that the PyCharm debugger fails on the call to `pytest.main()`

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


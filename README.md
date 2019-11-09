# hlextend_fix_msgforge
Fixes the msg string from the hlextend modul in python (https://github.com/stephenbradshaw/hlextend)

**Installing:**

Download the fix.py

Put it in the same folder as your programm is

put `import fix` at the top of your programm

use the `convert_hashforge()` function as follows:

**Usage:**
```python
mesg = fix.convert_hashforge(forged_msg_from_hlextend, string_from_beginning, string_from_end)
```
**Types:**

forged_msg_from_hlextend -> string

string_form_beginning -> string

string_from_end -> string

**Example:**
```python
forged_msg_from_hlextend_example = "hello&test\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\0cthisistheend"

mesg = fix.convert_hashforge(forged_msg_from_hlextend_example, "hello&test", "thisistheend")

print(mesg)
```
Written in python 2.7

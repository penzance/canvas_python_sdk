Autogenerate SDK Methods
==========================

** USE AT YOUR OWN RISK **

usage: generate_sdk_methods.py [-h] [-u URL]

Build Canvas SDK methods

optional arguments:
    -h, --help         show this help message and exit
    -u URL, --url URL  Base Canvas url, default is (https://canvas.instructure.com)

If run with no arguments, the script will default to the instructure url https://canvas.instructure.com

Where to run the script
------------------------

The script can be run from any directory. However, keep in mind that it will look for and create
if needed, a directory called "../canvas_sdk/methods" relative to the location of the script. It is recommended that you run the script from the scripts directory.

```
canvas_sdk_project
        |
        `--/canvas_sdk/methods (this directory will be created if needed by the script)
        |
        `--/scripts
        |      |
        |	    `--generate_sdk_methods.py (run the script from here)
        ...
```

Examples
--------

```
$ python generate_sdk_methods.py -h or --help ( print the text above )
```

```
$ python generate_sdk_methods.py -u https://canvas.instructure.com
```

creates the sdk methods from the base url canvas.instructure.com, if you run 
your own instance of canvas replace this url with yours.




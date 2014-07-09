Autogenerate Documentation
==========================

** USE AT YOUR OWN RISK **

usage: generate_sdk_methods.py [-h] [-u URL]

Build Canvas SDK methods

optional arguments:
  -h, --help         show this help message and exit
  -u URL, --url URL  Base Canvas url, default is
                     (https://canvas.instructure.com)

If run with no arguments, the script will default to the instructure url https://canvas.instructure.com


Examples
--------

1) $ python generate_sdk_methods.py -h or --help ( print the text above )

2) $ python generate_sdk_methods.py -u https://canvas.instructure.com
   creates the sdk methods from the base url canvas.instructure.com, if you run
   your own instance of canvas replace this url with yours.




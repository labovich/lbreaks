# lbreaks
  
Small command line tool for convert line breaks from UNIX format (`\n`) to DOS format (`\r\n`) or
from DOS format to UNIX format.  
GitHub [https://github.com/labovich/lbreaks](https://github.com/labovich/lbreaks) 

Work on Python 2.7, 3.4, 3.5, 3.6

Usage: 

```lbreaks.py -i <input file> -o <output file>```

Options:  
```
-i <filename>    input file
-o <filename>    output file  
-d               convert from UNIX format to DOS format  
                 (default convert from DOS format to UNIX format)  
-h, --help       show this help message  
-V, --version    print the version
```


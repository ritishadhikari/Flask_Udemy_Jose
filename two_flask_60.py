# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:53:57 2019

@author: ritis
"""

import one_flask_60

print("Top Level in two.py")

one_flask_60.func()

if __name__ == "__main__":
    print("Two.py is being run directly")
else:
    print("Two.py has been imported")

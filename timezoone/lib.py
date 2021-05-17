#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import pytz

def try_me():
    tz_Paris = pytz.timezone('Europe/Paris')
    datetime_Paris = datetime.now(tz_Paris)

    
    tz_NY = pytz.timezone('America/New_York') 
    datetime_NY = datetime.now(tz_NY)
    
    return print(f'Paris time: {datetime_Paris.strftime("%H:%M:%S")} - NY time : {datetime_NY.strftime("%H:%M:%S")}')
    

if __name__ == "__main__":
    try_me()
    
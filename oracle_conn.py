# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:24:25 2017

@author: stu
"""

import cx_Oracle

con = cx_Oracle.connect('scott/tiger@192.168.19.12:1522/orcl')
cur = con.cursor()

v_stmt='select * from skin'

cur.execute(v_stmt)

for result in cur:
    print(result)
  
    
    
cur.close()
con.close()


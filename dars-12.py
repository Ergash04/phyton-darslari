# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:08:35 2021

@author: qmukh
"""

en_uz = {'apple':'olma', 'blue':'ko`k', 'father':'ota'}
print(en_uz['apple'])

mevalar = {'olma':8000, 'tarvuz':10000, 'uzum':5000}
print(f"Olmaning narxi {mevalar['olma']} so`m")

talaba = {'ism':"murod olimov", 'yosh':21, 't_yil':2000}
print(f"{talaba['ism'].title()},\
      {talaba['t_yil']}-yilda tug`ilgan\
          {talaba['yosh']} yoshda")
 # bu buyruq orqali lug'atga o'zgartirish kiritish mumkin         
talaba['kurs'] = 4
talaba['fakultet'] = 'informatika'  
        

avto = {}




days = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

times = ['AM', 'PM', 'Night']

from random import random

def get_dict():

    result = {}

    for x in days:

        for y in times:

            result[(x,y)] = (random() < .5)

    return result





for x in range(20):

    a = db.newrecord('schedule', ctxid)

    a['schedule_times'] = get_dict()

    db.pclink(124, a.commit(), ctxid=ctxid)

    

def inst(func):
	return func()


class IterDict(dict):
  keylist = []
  @staticmethod
  def keylistiter_():
    print IterDict.keylist
    index = 0
    while 1:
      if index >= len(IterDict.keylist): index = 0
      if not IterDict.keylist: break
      yield IterDict.keylist[index]
      index += 1
  keylistiter = keylistiter_.__get__(1)()
  @classmethod
  def reset(cls): cls.keylistiter = cls.keylistiter_()
  def __setitem__(self, name, value):
    if name not in self.keylist:
        self.keylist.append(name)
    dict.__setitem__(self, name, value)
  def __delitem__(self, name):
    if name in self.keylist:
      del self.keylist[self.keylist.index(name)]
	dict.__delitem__(self, name)


import itertools


class CONT(object): pass


class PIDmanager(object):
	queue = IterDict()
	tasks = None
	@inst
	def pid_generator():
		counter = 0
		while 1:
			yield counter
			counter += 1
	@classmethod
	def put_task(self, task):
		pid = self.pid_generator.next()
		self.queue[pid] = task
        print pid
		if self.tasks == None:
            self.queue.reset()
			self.tasks = self.queue.keylistiter
            self.tasks.next()
	@classmethod
	def run_task(self):
		if self.tasks != None:
			pid = self.tasks.next()
			task = self.queue[pid]
			if hasattr(task, '__iter__') and isinstance(task[0], CONT):
				_, func, args, kwargs, cleanup = task
                result = []
				self.queue[pid] = func(*args, **kwargs)
				cleanup()
                return self.queue[pid]
			else:
				del self.queue[pid]
                return task
    @classmethod
    def run_all(self):
        try:
            while 1: self.run_task()
        except StopIteration:
            self.queue.reset()
            self.tasks == None


def print_many(gen, total=2000, count=0):
	print gen.next(),
	if count < total:
		return CONT(), print_many, (gen,), dict(total=total, count=count+1), cleanup


def cleanup(): print


PIDmanager.put_task( (CONT(), print_many, (itertools.cycle('a'),), dict(total=10), cleanup) )
PIDmanager.put_task( (CONT(), print_many, (itertools.cycle('b'),), dict(total=10), cleanup) )
PIDmanager.run_task()
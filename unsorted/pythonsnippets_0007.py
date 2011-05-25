class Fwrapper:
  fileno = 3
  def write(self, data):
      os.write(self.fileno, data)
  def read(self, data):
      pass
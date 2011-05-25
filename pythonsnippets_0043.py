    @abc.abstractmethod

    def process_chunk(self, chunk): return chunk







import re

class Grep(Pipe):

    def init(self, regex, delim='\n', *_, **__):

        self.__re = re.compile(regex)

        self.__delim = delim

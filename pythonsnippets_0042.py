    def read(self, bytes=-1):

        buf = self.process_chunk(self.__file.read(bytes))

        return buf        

    def process_chunk(self, chunk):

        buf = chunk.split(self.__delim)

        out = []

        while buf:

            line = buf.pop(0)

            if self.__re.search(line):

                out.append(line)

        return self.__delim.join(out)

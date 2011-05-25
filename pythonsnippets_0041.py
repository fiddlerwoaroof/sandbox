    def __getattribute__(self, name):

        result = None

        try:

            result = object.__getattribute__(self, name)

        except Exception, e:

            try:

                result = self.__file.__getattribute__(name)

            except:

                raise e

        return result

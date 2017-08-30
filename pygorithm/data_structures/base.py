
import inspect


class BaseDataStructure(object):

    @classmethod
    def get_code(cls):
        """
        returns the code for the current class
        """
        return inspect.getsource(cls)

    @staticmethod
    def time_complexities():
        """
        Prints time complexities of different operations
        """
        # TODO: Is it really required for all data structres?
        # If it is, change on `raise NotImplementedError`,
        # but for now not all classes have this method.
        pass

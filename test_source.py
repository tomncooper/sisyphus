""" This is module level comment """

def hello_world() -> None:
    """ This is a function level comment """
    # TODO: Say hello to everyone
    print("Hello World!")

class Test(object):
    """ This is a class level comment """

    def __init__(self, test_phrase) -> None:
        self._test_phrase: str = test_phrase

    @property
    def phrase(self) -> str:
        """ This is class method comment """
        return self._test_phrase

    def say(self) -> None:
        """ This is class method comment with a to do comment
        TODO: Make this function say nicer things
        """
        print(self.phrase)

if __name__ == "__main__":

    # This is a single line comment
    test: Test = Test("Hello Test!")

    #TODO: Say Hello in the main method
    hello_world()

    test.say()

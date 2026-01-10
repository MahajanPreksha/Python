#Public Modifier
class ABC:

    def __init__(self):
        self.public_attribute = None #This is a public attribute.

    def publicFunction(): #This is a public function.
        pass

#Private Modifier
class DEF:

    def __init__(self):
        self.__private_attribute = None #This is a private attribute.

    def __privateFunction(): #This is a private function.
        pass

#Protected Modifier
class GHI:

    def __init__(self):
        self._protected_attribute = None #This is a protected attribute.

    def _protectedFunction(): #This is a protected function.
        pass

abc = ABC()
print(abc.public_attribute) #Output: None

defi = DEF()
# print(defi.__private_attribute) --> This will throw AttributeError

ghi = GHI()
print(ghi._protected_attribute) #Output: None
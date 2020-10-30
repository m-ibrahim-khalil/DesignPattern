class IFile():
    def read(self):
        pass

    def write(self):
        pass


class BaseFile(IFile):
    def read(self):
        print("read base file")
    def write(self):
        print ("write base file")


class absDecorator(IFile):
    def __init__(self,inner):
        self.inner = inner



class CompressedFile(absDecorator):
    def read(self):
        print("decompressed file")
        self.inner.read()

    def write(self):
        self.inner.write()
        print ("compressed")


class EncryptFile(absDecorator):
    def read(self):
        print("Decrypted file")
        self.inner.read()

    def write(self):
        self.inner.write()
        print("Encrypted file")


class HeaderFile(absDecorator):
    def read(self):
        print("Remove header file")
        self.inner.read()

    def write(self):
        self.inner.write()
        print("Add header")


class client:
    if __name__ == '__main__':
        file = EncryptFile(CompressedFile(HeaderFile))
        file.write()



import bz2
#from demo_reader.util import writer
from .. import util as fuzzyboy

opener = bz2.open

if __name__ == '__main__':
    fuzzyboy.writer.main(opener)

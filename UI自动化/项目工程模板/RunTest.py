import sys
import os
from HNtest.Pltest import *

if __name__=='__main__':
    path=sys.path[0]
    Pltest(project_path=path).runcase()

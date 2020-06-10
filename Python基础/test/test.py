import sys
from os.path import dirname, abspath

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path+"\\module")
from calc import add
print(add(2,3))
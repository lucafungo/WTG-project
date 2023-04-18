import os
from api_caller import yesterday
import shutil

os.remove(f'{yesterday}.csv')
os.remove(f'{yesterday}sentiment_analysis.csv')
os.remove(f'{yesterday}.zip')
os.remove(f'{yesterday}_italian.zip')
shutil.rmtree(f'{yesterday}')
shutil.rmtree(f'{yesterday}_italian')

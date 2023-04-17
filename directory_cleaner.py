import os
from api_caller import yesterday
import shutil

os.remove(f'{yesterday}.csv')
os.remove(f'{yesterday}sentiment_analysis.csv')
os.remove(f'{yesterday}.zip')


shutil.rmtree(f'{yesterday}')

import os
from api_caller import yesterday
import shutil

os.remove(f'{yesterday}.csv')
os.remove(f'{yesterday}sentiment_analysis.csv')


shutil.rmtree(f'{yesterday}')

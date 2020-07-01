import requests
from lxml import etree
import pandas as pd
import re
url = 'http://www.weather.com.cn/weather1d/101010100.shtml#input'
with requests.get(url) as res:
content = res.content
html = etree.HTML(content)

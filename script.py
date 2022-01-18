
import requests

VIDEOID = 'lI3XJmcucy8'

r = requests.get('http://video.google.com/timedtext?lang=en&v={VIDEOID}')

print(r)
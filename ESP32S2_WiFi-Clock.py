# ESP32-S2 WiFi Clock

SSID = '' # your WiFi ssid
PW   = '' # your WiFi password
URL  = 'http://worldtimeapi.org/api/ip' # http://worldtimeapi.org/


import wifi, socketpool, ssl, adafruit_requests
import board, neopixel, rtc, time


weekday = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

colors = {'off':    (0, 0, 0),
          'white':  (255, 255, 255),
          'red':    (255, 0, 0),
          'yellow': (255, 255, 0),
          'green':  (0, 255, 0),
          'cyan':   (0, 255, 255),
          'blue':   (0, 0, 255),
          'purple': (255, 0, 255)}


pixel = neopixel.NeoPixel(board.IO18, 1, brightness=0.1, auto_write=False)

def setPixel(color):
    pixel.fill(colors.get(color, 'off'))
    pixel.show()


print('Scanning WiFi...')
setPixel('white')

for network in wifi.radio.start_scanning_networks():
    print(f'[{network.ssid}] channel: {network.channel}, rssi: {network.rssi}')

wifi.radio.stop_scanning_networks()
print('WiFi scanning completed.\n')


connected    = False
time_updated = False

try:
    
    if not SSID == '':
        print('Connecting to', SSID, '...')
        setPixel('yellow')
        
        wifi.radio.connect(SSID, PW)
        connected = True
        print('Connected.\n')
        setPixel('green')
        
    else:
        print('SSID not set.\n')
        setPixel('red')

except ConnectionError as e:
    print('Failed to connect:', e, '\n')
    setPixel('red')


time.sleep(1)
r = rtc.RTC()

if connected:

    pool = socketpool.SocketPool(wifi.radio)
    requests = adafruit_requests.Session(pool, ssl.create_default_context())

    print('Querying time...')
    setPixel('blue')

    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        unixtime = data['unixtime'] + data['raw_offset']
        
        r.datetime = time.localtime(unixtime)
        time_updated = True
        print('RTC time updated.\n')
        setPixel('green')
    
    else:
        print('Failed to query time.\n')
        setPixel('purple')


time.sleep(1)

while time_updated:
    dt = r.datetime
    y, mn, d = dt.tm_year, dt.tm_mon, dt.tm_mday
    h, mi, s = dt.tm_hour, dt.tm_min, dt.tm_sec
    w = weekday[dt.tm_wday]
    
    print(f'{y:04d}/{mn:02d}/{d:02d} {w} {h:02d}:{mi:02d}:{s:02d}')
    
    setPixel('cyan')
    time.sleep(0.1)
    
    setPixel('off')
    time.sleep(0.9)


while not time_updated:
    pass

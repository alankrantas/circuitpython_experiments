# ESP32S2 WiFi Clock with SSD1306 Display
# You need to install "adafruit_requests" and "adafruit_ssd1306" drivers
# as well as put font5x8.bin in the root directory.

SSID = '' # your WiFi ssid
PW   = '' # your WiFi password
URL  = 'http://worldtimeapi.org/api/ip' # http://worldtimeapi.org/


import wifi, socketpool, ssl, adafruit_requests
import board, busio, rtc, time, adafruit_ssd1306


weekday = ('Monday',
           'Tuesday',
           'Wednesday',
           'Thursday',
           'Friday',
           'Saturday',
           'Sunday')


i2c = busio.I2C(board.IO40, board.IO41)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.show()


print('Scanning WiFi...')
display.text('Scanning WiFi...', 0, 0, 1)
display.show()


for network in wifi.radio.start_scanning_networks():
    print(f'[{network.ssid}] channel: {network.channel}, rssi: {network.rssi}')

wifi.radio.stop_scanning_networks()
print('WiFi scanned.\n')
display.text('WiFi scanned.', 0, 8, 1)
display.show()


connected    = False
time_updated = False

try:

    if not SSID == '':
        print('Connecting to WiFi...')
        display.text('Connecting to WiFi...', 0, 24, 1)
        display.show()

        wifi.radio.connect(SSID, PW)
        connected = True
        print('Connected.\n')
        display.text('Connected.', 0, 32, 1)
        display.show()

    else:
        print('SSID not set.\n')
        display.text('SSID not set.', 0, 32, 1)
        display.show()

except ConnectionError as e:
    print('Failed to connect:', e, '\n')
    display.text('Failed to connect:', 0, 32, 1)
    display.text(e, 0, 32, 1)
    display.show()


r = rtc.RTC()

if connected:

    pool = socketpool.SocketPool(wifi.radio)
    requests = adafruit_requests.Session(pool, ssl.create_default_context())

    print('Querying time...')
    display.text('Querying time...', 0, 48, 1)
    display.show()

    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        unixtime = data['unixtime'] + data['raw_offset']

        r.datetime = time.localtime(unixtime)
        time_updated = True
        print('RTC time updated.\n')
        display.text('RTC time updated.', 0, 56, 1)
        display.show()

    else:
        print('Failed to query time.\n')
        display.text('Query failed.', 0, 56, 1)
        display.show()


time.sleep(1)

while time_updated:

    dt = r.datetime
    y, mn, d = dt.tm_year, dt.tm_mon, dt.tm_mday
    h, mi, s = dt.tm_hour, dt.tm_min, dt.tm_sec
    w = weekday[dt.tm_wday]
    date_str = f'{y:04d}/{mn:02d}/{d:02d}'
    time_str = f'{h:02d}:{mi:02d}:{s:02d}'

    print(date_str, w, time_str)
    display.fill(0)
    display.text('CircuitPython Clock', 0, 0, 1)
    display.text('ESP32-S2', 0, 16, 1)
    display.text(w, 0, 40, 1)
    display.text(f'{date_str} {time_str}', 0, 56, 1)
    display.show()


while not time_updated:
    pass

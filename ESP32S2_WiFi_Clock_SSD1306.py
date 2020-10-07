SSID = '' # your WiFi ssid
PW   = '' # your WiFi password
URL  = 'http://worldtimeapi.org/api/ip' # http://worldtimeapi.org/

UPDATE_DELAY       = 900
UPDATE_RETRY_DELAY = 15


import wifi, socketpool, ssl, adafruit_requests
import board, busio, rtc, time, adafruit_ssd1306


weekday = ('Monday',
           'Tuesday',
           'Wednesday',
           'Thursday',
           'Friday',
           'Saturday',
           'Sunday')


i2c = busio.I2C(scl=board.IO40, sda=board.IO41, frequency=400000)
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


last_updated_time = -UPDATE_DELAY

try:

    if not SSID == '':
        print('Connecting to WiFi...')
        display.text('Connecting to WiFi...', 0, 24, 1)
        display.show()

        wifi.radio.connect(SSID, PW)
        print('Connected.\n')
        display.text('Connected.', 0, 32, 1)
        display.show()
        time.sleep(1)

    else:
        print('SSID not set.\n')
        display.text('SSID not set.', 0, 32, 1)
        display.show()
        while True:
            pass

except ConnectionError as e:
    print('Failed to connect:', e, '\n')
    display.text('Failed to connect:', 0, 32, 1)
    display.text(e, 0, 32, 1)
    display.show()
    while True:
        pass


pool = socketpool.SocketPool(wifi.radio)
r = rtc.RTC()

while True:

    if time.time() - last_updated_time >= UPDATE_DELAY:

        print('Querying time...')
        display.fill(0)
        display.text('CircuitPython Clock', 0, 0, 1)
        display.text('ESP32-S2', 0, 16, 1)
        display.text('Updating time...', 0, 40, 1)
        display.show()

        try:
            requests = adafruit_requests.Session(pool, ssl.create_default_context())
            response = requests.get(URL)

            if response.status_code == 200:
                data = response.json()
                unixtime = data['unixtime'] + data['raw_offset']
                r.datetime = time.localtime(unixtime)
                response.close()
                print('RTC time updated.\n')
                last_updated_time = time.time()

            else:
                print('Failed to query time.\n')
                last_updated_time = -UPDATE_DELAY + UPDATE_RETRY_DELAY

        except Exception as e:
            print('Request error:', e, '\n')
            last_updated_time = -UPDATE_DELAY + UPDATE_RETRY_DELAY

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

    time.sleep(0.1)

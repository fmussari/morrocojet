"""Prompt 1:
Can you help me to develop a python script that monitors the speed of an "
internet connection?"""

"""Prompt 2:
can it be achieved without speedtest-cli"""

# https://convertlive.com/u/convert/megabits/to/bytes#1

# Measure download speed

import urllib.request
import time

# set the URL to a large file
url = 'https://upload.wikimedia.org/wikipedia/commons/6/6c/Morrocoy_from_Venezuela_2.jpg'

# set the size of the download buffer in bytes
buffer_size = 1024*24

# set the duration of the test in seconds
max_duration = 35

# download the file for the specified duration and calculate the download speed
elapsed_time = 0
downloaded = 0

response = urllib.request.urlopen(url)
while True:
    start_time = time.time()
    data = response.read(buffer_size)
    if not data or elapsed_time > max_duration:
        break
    downloaded += len(data)
    duration = time.time() - start_time
    elapsed_time += duration
    print(f"{downloaded / elapsed_time / 131_072:.2f} Mbps")

download_speed = downloaded / elapsed_time / 131_072 # convert from bytes to megabits

print(downloaded)
print(elapsed_time)

print(f"Download speed: {download_speed:.2f} Mbps")


# upload
import http.client
import io
import time

# set the URL to a script that will echo back the uploaded data
url = 'http://httpbin.org/post'

# set the size of the upload buffer in bytes
buffer_size = 256 * 256 * 2

# set the duration of the test in seconds
duration = 25

# create a byte stream to use as the upload data
upload_data = io.BytesIO(b'0' * buffer_size)

# upload the data for the specified duration and calculate the upload speed
start_time = time.time()
uploaded = 0
while time.time() - start_time < duration:
    conn = http.client.HTTPSConnection('httpbin.org')
    conn.request('POST', url, upload_data)
    response = conn.getresponse()
    uploaded += buffer_size
upload_speed = uploaded / duration / 131_072 # convert from bytes to megabits

# print the result
print(f"Upload speed: {upload_speed:.2f} Mbps")
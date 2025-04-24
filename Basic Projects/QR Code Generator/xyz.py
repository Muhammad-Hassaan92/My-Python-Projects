import speedtest

# Set best server
server = speedtest.Speedtest()
server.get_best_server()

# Test download speed
down = server.download()
down = down / 1000000  # Convert from bits/s to Mb/s
print(f"Download speed: {down:.2f} Mb/s")

# Test upload speed
up = server.upload()
up = up / 1000000  # Convert from bits/s to Mb/s
print(f"Upload speed: {up:.2f} Mb/s")

# Test ping
ping = server.results.ping
print(f"Ping speed: {ping:.2f} ms")

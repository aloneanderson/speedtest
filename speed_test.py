from speedtest import Speedtest

speed_test = Speedtest()
print(f"Your DOWNLOAD speed is: {speed_test.download()}")
print(f"Your UPLOAD speed is: {speed_test.upload()}")

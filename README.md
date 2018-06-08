# A Walk
Log GPS data from USB GPRS module in real time
as GPX file

Author: Omar Metwally, MD

        omar@analog.earth

## Usage
### 1. Get USB GPRS module path
```
dmesg | grep tty
```
(On my machine, this is /dev/ttyACM0)

### 2. Log latitude and longitude to file
```
sudo python3 log_gps.py
```

### 3. Install gpsbabel
```
sudo apt-get install gpsbabel
```

### 4. Convert file from step to GPX file 
```
gpsbabel -i csv -f way.csv -o gpx -F way.gpx
```






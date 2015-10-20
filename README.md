# IPGeoloc

## Description  
Take standard input, search for the 1st IP using regex and use geolite2 to output the found IP and geolocation data.  
Format : `IP: <IP> - Country: <country> - Continent: <continent> - Timezone: <timezone>`  
If no data found in geolite2 database output "-" character.  
  
## Example  
```
l3m0ntr33@nob:~/IPGeoloc# echo "8.8.8.8" | ~/IPGeoloc/ipgeoloc.py  
IP: 8.8.8.8 -  Country: US -  Continent: NA -  Timezone: America/Los_Angeles  
l3m0ntr33@nob:~/IPGeoloc#  
```
## Install dependencies  
Using pip is the easiest way :  
```
pip install pygeoip  
pip install python-geoip-geolite2  
```

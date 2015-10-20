# IPGeoloc

## Description  
Take standard input, search for the 1st IP using regex and use geolite2 to output the found IP and geolocation data.  
Format : `IP: <IP> - Country: <country> - Continent: <continent> - Timezone: <timezone>`  
If no data found in geolite2 database output "-" character.  
  
## Examples  
Simple demo
```
l3m0ntr33@nob:~/IPGeoloc# echo "8.8.8.8" | ~/IPGeoloc/ipgeoloc.py  
IP: 8.8.8.8 -  Country: US -  Continent: NA -  Timezone: America/Los_Angeles  
l3m0ntr33@nob:~/IPGeoloc#  
```  
For analysis attack logs based on geoIP  
```
root@kali:~/IPGeoloc# head -15 attack.log | ./ipgeoloc.py
IP: 79.107.77.52 -  Country: GR -  Continent: EU -  Timezone: Europe/Athens  
IP: 62.15.116.192 -  Country: ES -  Continent: EU -  Timezone: None  
IP: 14.99.179.179 -  Country: IN -  Continent: AS -  Timezone: Asia/Kolkata  
IP: 182.149.170.58 -  Country: CN -  Continent: AS -  Timezone: Asia/Shanghai  
IP: 79.107.77.52 -  Country: GR -  Continent: EU -  Timezone: Europe/Athens  
IP: 197.48.206.97 -  Country: EG -  Continent: AF -  Timezone: Africa/Cairo  
IP: 85.98.78.130 -  Country: TR -  Continent: AS -  Timezone: Europe/Istanbul  
IP: 183.88.253.186 -  Country: TH -  Continent: AS -  Timezone: Asia/Bangkok  
IP: 182.149.170.58 -  Country: CN -  Continent: AS -  Timezone: Asia/Shanghai  
IP: 197.48.206.97 -  Country: EG -  Continent: AF -  Timezone: Africa/Cairo  
IP: 86.219.78.243 -  Country: FR -  Continent: EU -  Timezone: Europe/Paris  
IP: 125.27.247.60 -  Country: TH -  Continent: AS -  Timezone: Asia/Bangkok  
IP: 125.26.222.233 -  Country: TH -  Continent: AS -  Timezone: Asia/Bangkok  
IP: 201.250.172.210 -  Country: AR -  Continent: SA -  Timezone: America/Argentina/Buenos_Aires  
IP: 86.219.78.243 -  Country: FR -  Continent: EU -  Timezone: Europe/Paris  
root@kali:~/IPGeoloc#
```
## Install dependencies  
Using pip is the easiest way :  
```
pip install pygeoip  
pip install python-geoip-geolite2  
```

# rpi-docker-boat
The repo contains setup scripts and a Docker Compose landscape with a complete setup for Raspberry Pi with a Signal K server.

## Sailors Hat
Setup I2C and SPI communication with the guide at [https://hatlabs.github.io/sh-rpi/](https://hatlabs.github.io/sh-rpi/) to make the RPi able to shut itself of on command from the SH.

In short, just do this:
```
curl -L \
    https://raw.githubusercontent.com/hatlabs/SH-RPi-daemon/main/install.sh \
    | sudo bash
```

## Software configuration
Install docker and docker compose
```
curl -sSL https://get.docker.com | sh
sudo apt-get install -y libffi-dev libssl-dev
sudo apt-get install -y python3 python3-pip
sudo apt-get remove python-configparser
python3 -m pip install -U pip
sudo pip3 install docker-compose
```

Adding docker user to correct user group
```
sudo groupadd docker
sudo usermod -aG docker $USER
```

### Install SignalK, Grafana and InfluxDB as docker containers
Clone the [KEGustafsson](https://github.com/KEGustafsson/SignalK-Telegraf-Influxdb-Grafana-in-docker) git repo.
```
git clone https://github.com/KEGustafsson/SignalK-Telegraf-Influxdb-Grafana-in-docker.git
```
Run run_me_1st.sh when installing SignalK, Telegraf, Influxdb and Grafana at first time (do not use sudo to run this script).


## Hardware configuration
### Network configuration
The wifi, LTE and CAN connections are configured using Systemd-Networkd to 
enable a local wifi hotspot with internet sharing from the LTE connection. 
The can interface is enabling communication with the NMEA2000 network.

The configuration files are in the network/systemd-networkd folder. 

The guide followed was [Use systemd-networkd for general networking](https://raspberrypi.stackexchange.com/a/108593/79866)
for switching to systemd-networkd for networking and [Setting up a Raspberry Pi as an access point - the easy way](https://raspberrypi.stackexchange.com/questions/88214/setting-up-a-raspberry-pi-as-an-access-point-the-easy-way) for enabling the
access point and internet sharing. 

Unfortunatley wpa_supplicant could not be used as AP software because of WPA2 
authentication issues with different clients. Hostapd should be used
instead.
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
The wifi configuration part is build upon [cjimti/iotwifi](https://github.com/cjimti/iotwifi). It provides a AP wifi that can be used for configuring the wifi of the RPi. 

To connect the RPi to a network use the following HTTP POST command.
```
curl -w "\n" -d '{"ssid":"batman-slow", "psk":"*"}' -H "Content-Type: application/json" \ -X POST localhost:8080/connect
```
The network to connect to must have the same channel as the RPi AP network.
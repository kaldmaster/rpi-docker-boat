# rpi-docker-boat
The repo contains a Docker Compose landscape with a complete setup for Raspberry Pi with a Signal K server.

## Wifi configuration
The wifi configuration part is build upon [cjimti/iotwifi](https://github.com/cjimti/iotwifi). It provides a AP wifi that can be used for configuring the wifi of the RPi. 

To connect the RPi to a network use the following HTTP POST command.
```
curl -w "\n" -d '{"ssid":"batman-slow", "psk":"*"}' -H "Content-Type: application/json" \ -X POST localhost:8080/connect
```
The network to connecto to must have the same channel as the RPi AP network.
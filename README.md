# aranya
smart forest related explorations

## Sound Triangulation
The objective is to detect the source of a sound source in a forest zone.

3 or  pi's with sound detectors are placed in the forest zone
The difference in the arrival time of the sound at these detectors along with their location is used to compute the location of the sound.

The solution consists of

1. Sound Detector Node
	-  This is a pi with sound detector peripheral
	-  This pi runs `shrona.py` which is a python script sends the SoundEvent to the Triangulator when a sound is heard.
	-  SoundEvent has a timestamp and the identity of the pi
2. Triangulator Node
	-  This is a pi that listens to Sound Events raised by Sound Detector Node
	-  This node knows the id and location of each of the Sound Detectors in the forest zone
trikona	-  This pi runs `trikonate.py` which is a python script that computes the location of the sound source from the arrival time difference and the location of the Sound Detectors

## How to run

### On the the Sound Detector Node
`shrona.py`  

```
$>SHRONA_GPIO_CHANNEL=17 SHRONA_DEVICE_ID=`hostname` TRIKONATE_IP=trikonate TRIKONATE_PORT=5005\
  python shrona.py
```

- depends in these enviroment variables . If there are not specified the following defaults are used
  
| Variable | Default |
| --- | --- |
| SHRONA_GPIO_CHANNEL | 17 |
| SHRONA_DEVICE_ID | \`hostname\` |
| TRIKONATE_IP | \`hostname\` |
| TRIKONATE_PORT | 5005 |

- creates a log file named `shrona.log` in the current directory - which logs sound events
- sends sound events as udp packets to  TRIKONATE_IP:TRIKONATE_PORT


### On the the Triangulator Node
`trikonate.py`

```
$>TRIKONATE_IP=`hostname` TRIKONATE_PORT=5005\
  python trikonate.py
```

- depends in these enviroment variables . If there are not specified the following defaults are used

| Variable | Default |
| --- | --- |
| TRIKONATE_IP | \`hostname\` |
| TRIKONATE_PORT | 5005 |

- creates a log file named `trikonate.log` in the current directory - which logs sound events
- this log file can be used to debug the triangulation algorithm to locate the sound source

### TODO

- Implentation of the triangulation algorithm
- This can be done inline in `trikonate.py`
- Make `shrona.py` event driven - it currently polls the GPIO channel every 300 ms
- dockerize the code







  


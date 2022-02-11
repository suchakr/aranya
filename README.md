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

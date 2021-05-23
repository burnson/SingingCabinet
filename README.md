# Singing Cabinet

The Singing Cabinet is a Raspberry Pi jukebox-style installation in an antique liquor cabinet. Opening the door begins a looping playback of a random song at a random point in the song through speakers inside the cabinet.

This is accomplished by placing a switch between Pin 18 and GND of the Raspberry Pi's GPIO and then detecting the state change to trigger a new song. For example, you can place two wires on the door jamb and then tape a piece of aluminum foil on the door to connect them when it closes.

All that is needed for the permanent part of the installation is a Raspberry Pi with the default NOOBS Raspbian system, a breakout kit, a thumb drive with .ogg files loaded on to the root folder, a powered USB hub, and some USB-powered speakers (the Kinivo ZX100 Mini Portable Speaker are great for this installation as they are cheap and can be chained together).

The setup is as simple as 1) replacing the `/etc/rc.local` with the provided file, which will help mount the thumb drive and launch the `juke.py` program on startup; 2) adding the `juke.py` file to the `/home/pi/juke` folder; and, 3) running the following commands while connected to the internet:

```
sudo apt-get install sox
mkdir /mnt/tunez
sudo modprobe snd_bcm2835
sudo amixer cset numid=3 1
```

This can all be configured with a USB keyboard, an HDMI cable, an HDMI display such as a TV, and an Ethernet cable.
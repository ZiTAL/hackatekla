# HACKATEKLA

```
su
apt-get install gocr python3-pip scrot
pip3 install Pillow
exit
```

## Fluxbox konfiguratu pantallazoa egiteko

**~/.fluxbox/keys

```
#...
#Print :Exec scrot -b '%Y-%m-%d-%H-%M-%S.png' -e 'mv $f ~/Irudiak/'
Print :Exec scrot -b 'takatekla.png' -e 'mv $f /tmp'
```
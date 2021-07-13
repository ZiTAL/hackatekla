# HACKATEKLA

```
su
apt-get install gocr python3-pip scrot php7-cli
pip3 install Pillow
exit
```

Greasemonkey Firefox-entzako instala:

https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/

## Fluxbox konfiguratu pantallazoa egiteko

**~/.fluxbox/keys

```
#...
#Print :Exec scrot -b '%Y-%m-%d-%H-%M-%S.png' -e 'mv $f ~/Irudiak/'
Print :Exec scrot -b 'takatekla.png' -e 'mv $f /tmp'
```

# PHP zerbitzaria martxan jarri

Zerbitzaria jarri behar dugu **takatekla.json** twitch-en JS bidez hartzeko
```
cd /tmp
php -S localhost:8000
```

# PYTHON

Honek **/tmp/takatekla.png** fitxategia irakurriko du, eta **/tmp/takatekla.json** fitxategia sortuko du php zerbitzaritik hartzeko

```
cd python
python3 takatekla.py
```

# JS - GREASEMONKEY

**js/takatekla.js** fitxategiarekin script-a sortu beharko dugu
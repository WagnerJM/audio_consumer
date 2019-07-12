# Audio consumer

## todo

## About
Das Programm verbindet sich mit einem RabbitMQ Server und "lauscht" auf ob die Queue mit dem Name __recorder__ füllt ist. Wenn ja, wird der Recorder Prozess ausfgeführt.
Der Recorder Prozess öffnet einen Browser(headless) über Selenium, interagiert auf der aufgerufenen Seite, startet eine Audioaufnahme und speichert die Aufnahme in einem spezifischen Verzeichnis auf dem Server als .wav-Datei.

## Installation

1. Git repo clonen
2. Service Datei erstellen unter `/lib/systemd/system/consumer.service`

``` Python
[Unit]
Description=Audio Consumer
After=multi-user.target

[Service]
Type=simple
WorkingDirectory=/home/darkwing/apps/audio_consumer
ExecStart=venv/bin/python main.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

3. Ausführbar machen: `sudo chmod 644 /lib/systemd/system/consumer.service`
4. Lädt die Service Liste neu: `sudo systemctl daemon-reload`

__Verschiedene nützliche Befehle:__
Start bei Boot: `sudo systemctl enable consumer.service`
Starten: `sudo systemctl start consumer.service`
Status: `sudo systemctl status consumer.service`

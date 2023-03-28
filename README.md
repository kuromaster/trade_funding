## PREPARE TO RUN:
```sh
apt install -y python3-pip python3-dev python3-virtualenv vim screen
```

```sh
cd /opt ; git clone https://github.com/kuromaster/trade_funding.git funding ; cd funding
```

```sh
python3 -m virtualenv venv
```

```sh
source venv/bin/activate
```

```sh
pip install -r requriements.txt
```
## ADD API_KEY and API_SECRET TO .env

Заменить _KEY_ и _SECRET_ на свои API_KEY, API_SECRET
```sh
echo 'export API_KEY="KEY"' > .env
```

```sh
echo 'export API_SECRET="SECRET"' >> .env
```

## TREE SCRIPT
```
(venv) root@bybitbinance:/opt/funding# tree -L 2
.
├── libs
│   ├── __pycache__
│   ├── bybit_api.py
│   ├── cprint.py
│   └── vars.py
├── main.py
├── requirements.txt
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

## RUN SCRIPT
```bash
screen -S FUNDING
```

```sh
source venv/bin/activate
```

```bash
./main.py
```

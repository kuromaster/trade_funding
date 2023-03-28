**PREPARE TO RUN:**
```sh
apt install -y python3-pip python3-dev python3-virtualenv
```

```sh
cd /opt ; mkdir funding ; cd funding
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

```sh
echo 'export API_KEY="KEY"' > .env
```

```sh
echo 'export API_SECRET="SECRET"' >> .env
```

**TREE SCRIPT**
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

**ADD API_KEY and API_SECRET TO .env**
```sh
(venv) root@srv01:/opt/funding# cat .env
export API_KEY="..."
export API_SECRET="..."
```

**RUN SCRIPT**
```bash
screen -S FUNDING
```

```sh
source venv/bin/activate
```

```bash
./main.py
```

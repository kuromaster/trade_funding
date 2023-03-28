**PREPARE TO RUN:**
```bash
apt install -y python3-pip python3-dev python3-virtualenv
```

```bash
cd /opt ; mkdir funding ; cd funding
```
```bash
python3 -m virtualenv venv
```

```bash
source venv/bin/activate
```
```bash
pip install -r requriements.txt
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

```bash
./main.py
```

**PREPARE TO RUN:**
```bash
apt install -y python3-pip python3-dev python3-virtualenv
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

**ADD API_KEY and API_SECRET TO .env**
```sh
(venv) root@srv01:/opt/funding# cat .env
export API_KEY="..."
export API_SECRET="..."
```

```bash
screen -S FUNDING
```

```bash
./main.py
```

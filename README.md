apt install -y python3-pip python3-dev python3-virtualenv
apt install sqlite3

python3 -m virtualenv venv
source venv/bin/activate
pip install -r requriements.txt

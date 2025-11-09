echo "Setting up environment"
# Set python virtual environment
deactivate
rm -rf .venv
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt




echo "Done"



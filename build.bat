cd front
pnpm install
pnpm run build
cd ..
pip install -r back/requirements.txt
python -m venv venv

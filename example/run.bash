poetry build
python -m venv ${BASH_SOURCE%/*}/.venv
${BASH_SOURCE%/*}/.venv/bin/pip install -U pip
${BASH_SOURCE%/*}/.venv/bin/pip install --force-reinstall ${BASH_SOURCE%/*}/../dist/*.whl
${BASH_SOURCE%/*}/.venv/bin/python ${BASH_SOURCE%/*}/main.py

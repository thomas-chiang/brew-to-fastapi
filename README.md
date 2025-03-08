/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install pipx

pipx ensurepath

pipx install poetry

poetry config virtualenvs.in-project true

poetry init

poetry add "fastapi[standard]"

touch product_api.py

poetry run fastapi run product_api.py
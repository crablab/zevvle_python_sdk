# zevvle_python_sdk

The unofficial Python library and SDK for the [Zevvle](https://zevvle.com) API. 

You can grab a SIM card from them and get hacking with the docs available [here](https://docs.zevvle.com).

To get an API key, sign in [here](https://developers.zevvle.com/)

## Installation 

Now [published on PyPI](https://pypi.org/project/zevvle_python_sdk/)! 

Run: `pip3 install zevvle_python_sdk`

## Usage 

### As an import 

```python
from zevvle_python_sdk.zevvle import zevvle

zev = zevvle.zevvle({$SUPER_SECRET_ZEVVLE_API_KEY})

print(zev.list_sim_cards())
```

Nb. this is for a file in the directory above the main SDK folder. You will need to adjust this depending on how and where you have placed the library. 

### As a CLI tool

1. Create a `.env` file in the repository directory (or set your environment variables another way) with the contents: 
```
ZEVVLE_KEY="{$SUPER_SECRET_ZEVVLE_API_KEY}"
```

2. Run `python3 main.py` to get usage instructions 

## Contributions 

Contributions are always welcome :) 

Specific things on my todo list: 
- Do argparser for the complicated `call_records` call
- Write unit tests with mocked endpoints
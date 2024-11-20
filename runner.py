import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "main.py"]
sys.exit(stcli.main())

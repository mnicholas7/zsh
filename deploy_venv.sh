# before 15.1.0
# virtua.venv --no-site-packages --distribute .venv &&\
#     source .venv/bin/activate &&\
#     pip install -r requirements.txt

# after deprecation of some arguments in 15.1.0
python -m .venv .venv && source .venv/bin/activate && pip install -r requirements.txt

printf ">>>>>>>> Flake8 Format Checking <<<<<<<<\n\n"
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
printf "\n\n>>>>>>>> Mypy Static Type Checking <<<<<<<<\n\n"
mypy .
printf "\n\n>>>>>>>> Pytest Unit Testing <<<<<<<<\n\n"
pytest --cov . --cov-config tests/.coveragerc

My Little date Calculator
---

# To install the tool from source

- Create virtual environment and activate it
  ```bash
  virtualenv -p python3 env
  source env/bin/activate
  ```
- Installing the tool
  ```bash
  (env) python3 setup.py install
  ```
- Running the tool
  ```bash
  (env) little-date-calculator -h
  ```
 - Sample command 
  ```bash
little-date-calculator -s "02/06/1983" -e "22/06/1983"
little-date-calculator -s "04/07/1984" -e "25/12/1984"
little-date-calculator -e "03/01/1989" -s "03/08/1983"
little-date-calculator --input-file input.csv --output-file output.csv
  ```
  

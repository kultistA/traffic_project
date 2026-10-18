import requests
import os
import pandas as pd
from pathlib import Path


# https://situas.istat.it/ShibO2Module/api/Report/Spool/2001-12-31/74?&pdoctype=CSV
# from the url we can see that there is date and a doctype parameter 
# let's set a base_url without the parameters
base_url = "https://situas.istat.it/ShibO2Module/api/Report/Spool/{data}/74"

# let's set directory and namefile, and make the directory
root = Path(__file__).resolve().parent.parent 
raw_dir = root / "data" / "raw"
output_dir = raw_dir / "csv_istat"
output_file = raw_dir / "area_raw.csv"
os.makedirs(output_dir, exist_ok=True)

# here there are some columns codes that will be useful afterwards
old_codes = [1, 10, 15, 27, 37, 48, 58, 63, 72, 80, 82, 83, 87, 92]
# basically the new codes are = to the old ones plus 200
new_codes = {}
for c in old_codes:
    new_codes[c] = c +200
# the only new code with a different logic is 107
new_codes[107] = 111

# apparently to access situas.istat.it is required to set user agent and other session data
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://situas.istat.it/",
    "Accept": "text/csv, application/octet-stream, */*",
    "Content-Type": "application/json"
})

# a cycle that for each year generates the url and downloads it
for anno in range(2001, 2025):
    data = f"{anno}-12-31"
    url = f"{base_url.format(data=data)}?pdoctype=CSV"
    
    print(f"Downloading {anno} data...")
    response = session.post(url, json={})

    # a check to see if there are error codes
    if response.status_code == 200:
        # just to be safe and later check the files we make a single file per year
        single_year_file = os.path.join(output_dir, f"situas_{anno}.csv")
        with open(single_year_file, "wb") as f:
            f.write(response.content)
        print(f"Saved: {single_year_file}")
        
        # then we read the file with the correct encoding and separator
        df = pd.read_csv(single_year_file, sep=";", encoding="utf-8")
        
        # starting from 2015 onwards there is an extra column, the third one which stores old provinces codes
        if anno >= 2015:
            col = df.columns[2]
            df = df.drop(columns=col)
            print(f"Removed extra column: '{col}'")
        
        # before 2015 we have to make some correction to the province code
        # so it will match the new ones
        else:
            col = df.columns[2]
            df[col] = df[col].replace(new_codes)
            print(f"Remapped codes in column: '{col}'")

        # let's take the headers from 2001 and just the content lines otherwise
        mode = "w" if anno == 2001 else "a"
        header = anno == 2001

        df.to_csv(output_file, mode=mode, header=header, index=False, sep=";", encoding="utf-8")
        print(f"Added {len(df)} record to the main csv")
    else:
        print(f"Error {response.status_code} writing year {anno}")
        print(f"{response.text[:300]}")

print(f"Output: {output_file}")
print(f"Now fixing {output_file}")


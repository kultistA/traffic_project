## Project Description

**Assignment**: Your company operates in road traffic management and accident prevention, and has asked you to build an up-to-date dashboard showing which Italian municipalities are the most promising for investment. After talking with the business team, you conclude that the key question is which areas have had the highest car accident rates in recent years, ideally with a forecasting component. The data currently available is unreliable, outdated, and too messy to use as it is.

**The goal**: identify which towns have the highest accident rates, total number of accidents, population, and any other metrics relevant to the business objective. For example: which cities are the best candidates for investment, and why?

## Sources
* For traffic accidents statistics, the endpoint [https://esploradati.istat.it/SDMXWS/rest/data/41_983](link)
* For demographic data the SITUAS data [https://situas.istat.it/web/#/territorio/body?id=74&dateFrom=2020-12-31](link) 
* To study the use of ISTAT APIs [https://ondata.github.io/guida-api-istat/](link)
* SDMX Web Services ISTAT [https://www.istat.it/en/classifications-and-tools/sdmx-web-services/](link)

## Project Structure

In `../scripts/` you can find the main import scripts to download the raw data.. **Run those first**

Raw files will be saved in `../data/raw/`

Afterwards in `../notebooks/` there is the notebook containing the EDA using pandas/numpy, seaborn, scipy

Outuput files, used as base for PowerBI will be saved in `../data/outputs/`

Finally in `../reports/` you can find a short deck explaining the project and a Power BI dashboard
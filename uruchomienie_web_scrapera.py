import web_scraper as gs
import pandas as pd

path = "C:/Users/Mikolaj/Polska_Data-science/chromedriver"

niemcy = gs.get_jobs("data scientist", 500, False, path, 15)



niemcy.to_csv("niemcy.csv", index = False)
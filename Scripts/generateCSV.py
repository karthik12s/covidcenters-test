import requests
import pandas as pd

def google_maps(url):

    ret = requests.get(url)
    url_ = ret.request.path_url

    lis = url_.split("/")

    if len(lis) == 10 or len(lis) == 9:

        loc = lis[8].split(",")

    else:

        loc = lis[4].split(",")

    if '@' in loc[0]:
        loc[0] = loc[0].replace('@','')
    elif '%40' in loc[0]:
        loc[0] = loc[0].replace('%40','')

    loc.pop(2)

    return loc[0],loc[1]


# df = pd.read_excel(r'/home/srujan/Downloads/Testing Centres Sheet.xlsx')



def read_excel_sheets(xls_path):
    """Read all sheets of an Excel workbook and return a single DataFrame"""
    print(f'Loading {xls_path} into pandas')
    xl = pd.ExcelFile(xls_path)
    df = pd.DataFrame()
    columns = None
    for idx, name in enumerate(xl.sheet_names):
        print(f'Reading sheet #{idx}: {name}')
        sheet = xl.parse(name)
        if idx == 0:
            # Save column names from the first sheet to match for append
            columns = sheet.columns
        sheet.columns = columns
        # Assume index of existing data frame when appended
        df = df.append(sheet, ignore_index=True)



    return df

## Provide path to the .xlsx file or load the .csv directly if possible
xl_path = '/home/srujan/Downloads/Testing Centres Sheet.xlsx'

df = read_excel_sheets(xl_path)

latitudes = []
longitudes = []

for index, row in df.iterrows():
    url = row['LOCATION']

    if not type(url) == str:
        # print("Its not a url")
        lat = ""
        lon = ""
    else:
        # print("its proper")
        # print(url)
        lat, lon = google_maps(url)

    latitudes.append(lat)
    longitudes.append(lon)

    print('Finished Processing {}/{} row with lat, lon = {},{}'.format(index, len(df.index), lat, lon))

df['LATITUDES'] = latitudes
df['LONGITUDES'] = longitudes

df.to_csv('data.csv')

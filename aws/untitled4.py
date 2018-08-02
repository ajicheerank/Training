import fix_yahoo_finance as fy
from datetime import date, timedelta
from time import strftime


today = date.today()
yday = today - timedelta(1)
dformat = '%Y-%m-%d'

def download_data_4_symbols(ticker):
    data = fy.download('MMM',yday.strftime(dformat),today.strftime(dformat))
    return data
    
def write_to_file(file_name, data):
    fs = open(file_name, "w")
    fs.write(data.to_csv())
    fs.close()
    #print("Downloaded {}".format(file_name))

if __name__ == "__main__":
    lstTicker = input("Input ticker seperated by , : ").split(",")
    #lstTicker = Tickers
    
    for ticker in lstTicker:
        data = download_data_4_symbols(ticker)
        #write_to_file(ticker+".txt", data)
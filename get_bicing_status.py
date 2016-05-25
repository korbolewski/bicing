import urllib, json, os

def append_record(record, fname):
    with open(fname, 'a') as f:
        json.dump(record, f)
        f.write(os.linesep)

fname = "out.txt"
url = "http://wservice.viabicing.cat/v2/stations"

if __name__ == "__main__":

	response = urllib.urlopen(url).read()[7:-7]
	data = json.loads(response)
	append_record(data, fname)

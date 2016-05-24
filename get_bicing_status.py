import urllib, json, os

def append_record(record, fname):
    with open(fname, 'a') as f:
        json.dump(record, f)
        f.write(os.linesep)


def file_to_dict(fname):
	with open(fname) as f:
		mylist = [json.loads(line) for line in f]
	return mylist


fname = "out.txt"
url = "http://wservice.viabicing.cat/v2/stations"


if __name__ == "__main__":

	response = urllib.urlopen(url).read()[7:-7]
	data = json.loads(response)
	append_record(data, fname)
	#content = file_to_dict(fname)

# this is how to use the content
# print data['stations'][0]
# for item in data['stations']:
# 	print float(item['bikes']) / (float(item['bikes']) + float(item['slots']))

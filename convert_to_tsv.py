# -*- coding: utf-8 -*-
import json, os, time

def get_data_from_file(fname):
	with open(fname) as f:
	    data = [json.loads(line) for line in f]
	return data

def write_to_tsv_file (dataset, output_file):
	singlejson = data[0]
	station = singlejson['stations'][0]
	station_attributes = sorted(station.keys())

	headers = "updateDateTime" + "\t" + "updateTime" + "\t" + "\t".join(station_attributes)
	with open(output_file, 'w') as f:
		f.write(headers)
		f.write(os.linesep)
		for singlejson in dataset:
			for item in singlejson['stations']:
				station_attribute_values = []
				for attribute in station_attributes:
					station_attribute_values.append(item[attribute].encode('utf-8'))
				line = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(singlejson["updateTime"])) + "\t" + str(singlejson["updateTime"]) + "\t" + "\t".join(station_attribute_values)
				#print station_attribute_values
				f.write( line )
				f.write(os.linesep)

input_file = "out.txt"
output_file = "data.tsv"

if __name__ == "__main__":
	data = get_data_from_file(input_file)
	write_to_tsv_file(data, output_file)



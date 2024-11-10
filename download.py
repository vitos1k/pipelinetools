import requests
import os
import posixpath

#url_template = r'http://cdn.gea.esac.esa.int/Gaia/gdr1/tgas_source/csv/TgasSource_000-000-{index:03d}.csv.gz'
url_template = r'https://cdsarc.cds.unistra.fr/ftp/I/259/tyc2.dat.{index:02d}.gz'

def main():
	for index in range(20):
		url = url_template.format(index=index)
		filename = posixpath.basename(url)
		if os.path.isfile(filename):
			print ("Skipped", filename)
			continue
		print ("Downloading", filename)
		response = requests.get(url, stream=True)
		with open(filename, 'wb') as fp:
			for chunk in response.iter_content(1024):
				fp.write(chunk)

if __name__ == '__main__':
	main()
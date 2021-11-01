import os
import sys


def Landsat_cloud_detection(scenedir: str, outfile: str):
    try:
        os.system(f'fmask_usgsLandsatStacked.py -o cloud.img --scenedir {scenedir}')
        os.system(f'gdal_translate -of "Gtiff" cloud.img {outfile}')
        return f'Success: result is saved in {outfile}'
    except Exception as e:
        return f'Failed: {e}'


def Sentinel2_cloud_detection(safedir: str, outfile: str):
    try:
        os.system(f'fmask_sentinel2Stacked.py -o cloud.img --safedir {safedir}')
        os.system(f'gdal_translate -of "Gtiff" cloud.img {outfile}')
        return f'Success: result is saved in {outfile}'
    except Exception as e:
        return f'Failed: {e}'


def main(inputdir: str, outfile: str):
    if inputdir.startswith('LC'):
        msg = Landsat_cloud_detection(inputdir, outfile)
    else:
        msg = Sentinel2_cloud_detection(inputdir, outfile)
    return msg


if __name__ == '__main__':
    print(main(sys.argv[1], sys.argv[2]))

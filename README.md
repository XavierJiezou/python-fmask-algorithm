# Python-Fmask-Algorithm

Python modules that implement the `fmask` algorithm. (Refer to: [python-fmask](https://www.pythonfmask.org/))

## Install

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
conda create -n fmask python-fmask
conda activate fmask
```

## Usage

```bash
git clone https://github.com/XavierJiezou/python-fmask-algorithm.git
cd python-fmask-algorithm
python main.py inputdir outfile
```

### USGS Landsat

```bash
python main.py LC81230322021250LGN00 cloud.jpg
```

### Sentinel2

```bash
python main.py S2B_MSIL1C_20180918T235239_N0206_R130_T56JNQ_20180919T011001.SAFE cloud.jpg
```

## Color-Maps

|VALUE|MEANING|COLOR|
|:---:|:-----:|:---:|
|  0  | null  |  \  |
|  1  | clear |  \  |
|  2  | cloud | 紫色|
|  3  | shadow| 黄色|
|  4  | snow  | 浅蓝|
|  5  | water | 深蓝|

## Link

> [https://github.com/ubarsc/python-fmask](https://github.com/ubarsc/python-fmask)

## Cite

> [0] [Zhu, Z. and Woodcock, C.E. (2012). Object-based cloud and cloud shadow detection in Landsat imagery Remote Sensing of Environment 118 (2012) 83-94.](https://www.sciencedirect.com/science/article/pii/S0034425711003853)
> [1] [Zhu, Z., Wang, S. and Woodcock, C.E. (2015). Improvement and expansion of the Fmask algorithm: cloud, cloud shadow, and snow detection for Landsats 4-7, 8, and Sentinel 2 images Remote Sensing of Environment 159 (2015) 269-277.](https://www.sciencedirect.com/science/article/pii/S0034425714005069)
> [2] [Frantz, D., Hass, E., Uhl, A., Stoffels, J., & Hill, J. (2018). Improvement of the Fmask algorithm for Sentinel-2 images: Separating clouds from bright surfaces based on parallax effects. Remote Sensing of Environment 215, 471-481.](https://www.sciencedirect.com/science/article/pii/S0034425718302037)

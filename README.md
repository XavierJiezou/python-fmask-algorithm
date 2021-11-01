# Introduction
Python modules that implement the `fmask` algorithm.(Refer to: [python-fmask](https://www.pythonfmask.org/))
# Install
```
conda config --add channels conda-forge
conda config --set channel_priority strict
conda create -n fmask python-fmask
conda activate fmask
```
# Usage
```
```
## USGS Landsat
## Sentinel2
# Color-maps
|VALUE|MEANING|COLOR|
|:---:|:-----:|:---:|
|  0  | null  |  \  |
|  1  | clear |  \  |
|  2  | cloud | 紫色|
|  3  | shadow| 黄色|
|  4  | snow  | 浅蓝|
|  5  | water | 深蓝|
# Link
> [https://github.com/ubarsc/python-fmask](https://github.com/ubarsc/python-fmask)
# Cite
```
[0] Zhu, Z. and Woodcock, C.E. (2012). Object-based cloud and cloud shadow detection in Landsat imagery Remote Sensing of Environment 118 (2012) 83-94.
[1] Zhu, Z., Wang, S. and Woodcock, C.E. (2015). Improvement and expansion of the Fmask algorithm: cloud, cloud shadow, and snow detection for Landsats 4-7, 8, and Sentinel 2 images Remote Sensing of Environment 159 (2015) 269-277.
[2] Frantz, D., Hass, E., Uhl, A., Stoffels, J., & Hill, J. (2018). Improvement of the Fmask algorithm for Sentinel-2 images: Separating clouds from bright surfaces based on parallax effects. Remote Sensing of Environment 215, 471-481.
```


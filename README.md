
# Color Detection

## Installation


```
    git clone
    pip install opencv-python numpy matplotlib 
```

---


## Usage

### args

- `r` : red [0~255] (required)
- `g` : green [0~255] (required)
- `b` : blue [0~255] (required)
- `p` : path file path (required)
- `d` : Sensitivity (0~1)

```
    python color_detection.py -r 18 -g 0 -b 108 -p test.jpg
```

##  original image
![](test.jpg)

## mask image
![](test_mask.jpg)

## masked image
![](test_masked.jpg)







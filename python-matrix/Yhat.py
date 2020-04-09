import numpy as np

X = [[17.93020121, 94.52059195,  1.        ],
       [97.14469719, 69.59328198,  1.        ],
       [81.77590078,  5.7376481 ,  1.        ],
       [55.85434242, 70.32590168,  1.        ],
       [49.36654999, 75.11404016,  1.        ],
       [ 3.19270247, 29.25629886,  1.        ],
       [49.20078406, 86.14443851,  1.        ],
       [21.8828039 , 46.8415052 ,  1.        ],
       [79.50986272, 87.39735554,  1.        ],
       [88.1538875 , 65.20564193,  1.        ],
       [60.74385434, 99.9576339 ,  1.        ],
       [67.41558195, 50.36830961,  1.        ],
       [48.31811577, 99.12895314,  1.        ],
       [28.82997197, 87.18494885,  1.        ],
       [43.85374266, 64.47363908,  1.        ],
       [25.31369409, 83.54529426,  1.        ],
       [10.80772667, 45.69556859,  1.        ],
       [98.36574588, 82.69739353,  1.        ],
       [29.14690997, 66.36510676,  1.        ],
       [65.1003019 , 33.3538835 ,  1.        ],
       [24.64411349, 39.54005274,  1.        ],
       [37.55980488,  1.34572784,  1.        ],
       [88.16450624, 95.15366257,  1.        ],
       [13.83462084, 25.4940482 ,  1.        ],
       [64.41084375, 77.25983813,  1.        ],
       [68.9259918 , 97.4536008 ,  1.        ],
       [39.48844224, 50.85612819,  1.        ],
       [52.46317768, 59.77650969,  1.        ],
       [48.48478698, 66.97035422,  1.        ],
       [ 8.06208781, 98.24260014,  1.        ],
       [32.73188771, 18.85353553,  1.        ],
       [11.6523788 , 66.26451174,  1.        ],
       [13.73035353, 70.47250913,  1.        ],
       [ 8.18555177, 41.85198942,  1.        ],
       [53.60987615, 94.56012164,  1.        ],
       [95.36860989, 47.29550696,  1.        ],
       [87.33360921, 93.80393433,  1.        ],
       [66.35761109, 81.84755128,  1.        ],
       [19.75471753, 65.52330092,  1.        ],
       [21.13344045, 47.43718199,  1.        ],
       [22.37386481, 25.95562754,  1.        ],
       [93.99040405,  0.12789052,  1.        ],
       [86.7201981 , 18.41376678,  1.        ],
       [98.99837299, 60.23126569,  1.        ],
       [ 3.59396564, 96.25221732,  1.        ],
       [15.10236337, 92.55690357,  1.        ],
       [97.83414077,  2.0239081 ,  1.        ],
       [19.93821969, 46.77827346,  1.        ],
       [30.37351114, 58.77752516,  1.        ],
       [73.29288315, 67.66962776,  1.        ],
       [52.23090088, 81.90244825,  1.        ],
       [86.42957611, 66.5402276 ,  1.        ],
       [93.40080214, 18.07524594,  1.        ],
       [13.21346006, 91.48885878,  1.        ],
       [ 4.5934627 , 46.33593152,  1.        ],
       [15.66929158, 35.543744  ,  1.        ],
       [52.95935977, 68.72020961,  1.        ],
       [56.81752123, 47.57273192,  1.        ],
       [51.13354308, 78.04216746,  1.        ],
       [ 7.86216472, 17.72908178,  1.        ],
       [54.6986037 , 92.74458414,  1.        ],
       [86.39906301, 41.88869459,  1.        ],
       [11.94750602, 42.96138674,  1.        ],
       [70.35840106, 83.70623451,  1.        ],
       [29.02236633, 84.32778308,  1.        ],
       [42.75947991, 97.49332608,  1.        ],
       [96.21565644, 25.83428258,  1.        ],
       [53.22772766, 27.90550857,  1.        ],
       [30.36098967,  0.93964422,  1.        ],
       [83.27756539, 73.17934857,  1.        ],
       [30.18769248,  7.1465386 ,  1.        ],
       [11.78841846, 51.69776084,  1.        ],
       [18.29242401, 61.97797605,  1.        ],
       [96.71266769,  9.02910151,  1.        ],
       [31.01273869, 78.28338246,  1.        ],
       [11.39726075, 61.72869324,  1.        ],
       [17.39255579,  4.24114086,  1.        ],
       [72.18269373, 34.53907217,  1.        ],
       [73.98002078,  3.71649344,  1.        ],
       [94.49305835, 88.41719702,  1.        ],
       [84.56282073, 20.24116219,  1.        ],
       [51.74247397, 11.00974796,  1.        ],
       [53.7485904 , 60.0251023 ,  1.        ],
       [85.05083476, 95.73699695,  1.        ],
       [46.77725045, 90.20220624,  1.        ],
       [49.75843417, 52.83449436,  1.        ],
       [24.1192565 , 42.10281078,  1.        ],
       [27.20157645, 29.97874929,  1.        ],
       [ 7.00959617, 55.87605839,  1.        ],
       [97.64694967,  8.14762513,  1.        ],
       [ 1.38298251, 84.94408692,  1.        ],
       [22.32353035, 27.51507504,  1.        ],
       [45.04540623, 93.52040222,  1.        ],
       [40.16399147,  0.16169923,  1.        ],
       [53.18273979,  8.17031616,  1.        ],
       [46.45677916, 82.00017091,  1.        ],
       [77.13030069, 95.18875945,  1.        ],
       [68.60060757, 72.57118072,  1.        ],
       [41.69388712, 69.24112597,  1.        ],
       [ 4.1426694 , 52.25472638,  1.        ]]

Y = [320.2595296 , 404.63447153, 181.48510774, 321.77363802,
       322.46548558,  94.6188109 , 356.34809275, 181.65376923,
       423.55774319, 369.22924544, 427.60580366, 292.47182155,
       395.52981141, 319.03134845, 287.4281441 , 292.76890884,
       159.66330767, 438.79896387, 250.98630903, 231.71150792,
       163.39816083,  83.48015514, 466.26580579, 100.88643027,
       365.64104806, 426.14001549, 235.53238946, 283.29164032,
       298.58144037, 309.23410878, 129.61013901, 224.15054209,
       235.30566563, 153.48418946, 394.93944425, 336.12673888,
       449.36335199, 387.01481648, 240.38944159, 177.14828058,
       119.61125795, 196.71616666, 236.26080836, 384.38134469,
       293.23718304, 304.89088281, 201.29359842, 170.61009304,
       242.37348423, 353.0829913 , 348.72568856, 365.95997095,
       235.47238163, 300.60687826, 145.81874525, 138.88033469,
       317.16370774, 254.9036313 , 334.5843335 ,  69.35558881,
       386.85993724, 294.87171358, 156.75421955, 391.80613529,
       319.31046285, 376.29158948, 280.61704387, 194.43046507,
        69.64886318, 384.59718499,  89.5390084 , 181.5506828 ,
       224.77338288, 219.5670937 , 298.49021648, 199.94404471,
        43.91569235, 256.06837823, 159.37258064, 447.13270362,
       233.07882958, 131.07017963, 298.8143327 , 451.80352299,
       368.36643595, 254.70677401, 168.30843276, 146.34226   ,
       176.81014898, 219.16028041, 252.90565295, 127.57047884,
       375.82234034,  80.38901933, 142.71818308, 336.87615438,
       438.46058613, 355.90028692, 284.83463671, 168.03440095]


# Transposing the X array, converting columns to rows:
X = np.array(X)
Xt = X.T

# dot product of Xt and X:
XtX = np.dot(Xt, X)

# dot product of Xt and Y:
XtY = np.dot(Xt, Y)

# inverse of XtX
XtXinv = np.linalg.inv(XtX)

# Yhat = dot product of XtXinv and XtY
Yhat = np.dot(XtXinv, XtY)
print("Yhat: ", Yhat)
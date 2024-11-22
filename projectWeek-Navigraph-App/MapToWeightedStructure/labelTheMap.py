from math import sqrt
import matplotlib.pyplot as plt
"""
backGroundImg=plt.imread("campus.png")
fig,ax=plt.subplots()
ax.imshow(backGroundImg,extent=[0,640,0,480])
plt.show()

xy_dict={
		"0": [ 187, 205 ],
		"1": [ 103, 181 ],
		"2": [ 304, 110 ],
		"3": [ 118, 328 ],
		"4": [ 315, 319 ],
		"5": [ 443, 306 ],
		"6": [ 431, 460 ],
		"7": [ 53, 266 ],
		"8": [ 535, 74 ],
		"9": [ 535, 192 ],
		"10": [ 535, 316 ],
		"11": [ 63, 314 ],
		"12": [ 636, 374 ],
		"13": [ 583, 43 ],
		"14": [ 525, 474 ],
		"15": [ 368, 314 ],
		"16": [ 371, 441 ],
		"17": [ 286, 251 ]
	}
		"""
xy=[
(337,339),
(271,240),
(195,338),
(159,364),
(112,315),
(91 ,339),
(94 ,266),
(135, 215),
(105, 140),
(146 ,82),
(147, 30),
(202 ,70),
(268, 70),
(265, 91),
(330 ,70),
(382 ,70),
(382, 91),
(436 ,70),
(436 ,91),
(512 ,70),
(70, 166 ),
(569, 104 ),
(70 ,291 ),
(74 ,255)
]
"""
for i in xy_dict:
	xy.append(xy_dict[i])
	"""
for it in enumerate(xy):
    i,a=it
    print("\"{}\":{},".format(i,a))
	
 
paths=[]
while True:
	try:
		i=int(input("id of point1"))
		ii=int(input("id of point2"))
		x1=xy[i][0]
		y1=xy[i][1]
		x2=xy[ii][0]
		y2=xy[ii][1]
		paths.append(list((i,ii,round(sqrt((x1-x2)**2+(y1-y2)**2),3))))
	except BaseException:
		break
print(paths)

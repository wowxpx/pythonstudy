import re
img = "<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" " \

src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display:inline;">"


src1 = re.findall(r'src="(.*)"',img)
print(src1)
src2 = re.findall(r'src="(.*?)"',img)
print(src2)
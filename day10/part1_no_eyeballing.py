import utils
import matplotlib.pyplot as plt
from pytesseract import image_to_string
from PIL import Image

# Credit to github.com/fletchto99/advent-of-code/blob/master/2018/Day%2010/solution.py
# for the OCR part of this solution

lights = utils.load_data()

while lights.size < lights.prev_size:
    lights.update()
    lights.compute_size()
lights.update(-1)

fig = plt.figure(figsize=(3.5, 0.9))
ax = plt.axes()
ax.scatter(lights.x, -lights.y, s=20, c='k')
ax.set_xticks([])
ax.set_yticks([])
plt.setp(ax.spines.values(), color='white')
plt.tight_layout()
plt.savefig('solution.png')

text = image_to_string(Image.open('solution.png'))
print(text)

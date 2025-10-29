import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO  #used for buffer memory to store or capture image


def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

#elephant_url = "https://images.pexels.com/photos/133394/pexels-photo-133394.jpeg"
elephant_url ="https://images.pexels.com/photos/145979/pexels-photo-145979.jpeg?cs=srgb&dl=animal-big-cat-safari-145979.jpg"
elephant= load_image_from_url(elephant_url)

elephant_np = np.array(elephant)# Convert to NumPy array and print shape
print("Elephant image shape:", elephant_np.shape)

plt.figure(figsize=(6, 4))
plt.imshow(elephant)
plt.title("Elephant")
plt.axis("off")
plt.show()

# Convert to grayscale
elephant_gray = elephant.convert("L")

# Display grayscale image
plt.figure(figsize=(6, 4))
plt.imshow(elephant_gray, cmap="grey")
plt.title("Elephant (Grayscale)")
plt.axis("off")
plt.show()
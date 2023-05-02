# HW3Q4



<img width="407" alt="image" src="https://user-images.githubusercontent.com/62819751/235676587-732c0210-be8d-4c29-b36f-73f8ebcd3eba.png">


Counting neurons and cells
-------------------------------------------------------------------


![Blood-cells_12 Red-blood-ce](https://user-images.githubusercontent.com/62819751/235676677-a2e58711-323a-4a83-9dc9-9d107aa969a0.jpg)


![neuron](https://user-images.githubusercontent.com/62819751/235676698-248fbfb5-ab67-43b4-9fbf-6c69cfc6b591.jpg)


Turn the image to grey scale and equalize the images for more clarity in the image. Then using opencv threshold function apply binary and otsu algorithm to find the threshold to turn it into a binary image. 


![BinaryImageBlood](https://user-images.githubusercontent.com/62819751/235677238-5a487160-c94f-45f4-98e8-a318c877469d.png)


![BinaryImageNeurons](https://user-images.githubusercontent.com/62819751/235677243-6da15251-2ea6-4312-9579-46173b1a260e.png)


After turning the images into binary images, the noise needs to be cleared a bit better. Therefore, using opencv package to dilate the image to get rid of unwanted blobs and then erode the remaining blobs. 


![DilatedErosionImageBlood](https://user-images.githubusercontent.com/62819751/235677665-fa85cc0a-fc92-4c0c-886f-e3f6ca0bd6a6.png)

![DilatedErosionImageNeurons](https://user-images.githubusercontent.com/62819751/235677668-cf999a67-7b6c-4176-8224-ed299c157e37.png)


It is time to count each blob using connected components from the CV package to count each blob on the image.


![Results](https://user-images.githubusercontent.com/62819751/235677818-e6b72054-1901-4e5b-b893-2762bd39ff5a.png)

7 Neurons and 136 Blood Cells




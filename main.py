import cv2
from matplotlib import pyplot as plt

image = cv2.imread(r'Image.tiff', 0)

if image is not None:
    # Применение фильтра NLMeans
    filtered_image = cv2.fastNlMeansDenoising(image, None, h=15, templateWindowSize=5, searchWindowSize=25)

    # Отображение исходного и отфильтрованного изображения
    plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Исходное изображение')
    plt.subplot(122), plt.imshow(filtered_image, cmap='gray'), plt.title('Отфильтрованное изображение')
    plt.show()

    # Сохранение отфильтрованного изображения
    cv2.imwrite('Image_1.tiff', filtered_image)
else:
    print("Не удалось загрузить изображение.")
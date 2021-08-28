from selenium import webdriver
from pathlib import Path
from PIL import Image
import numpy as np
import time, urllib.request
import imgaug.augmenters as iaa

def augment(image, pixel, search_name, numbers):
    aug_pipeline = iaa.Sequential([
        iaa.SomeOf((0,3),
        [
            iaa.Fliplr(1.0), 
            iaa.Flipud(1.0),
            iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)), 
            iaa.Crop(percent=(0, 0.4)),
            iaa.Sometimes(0.5, iaa.Affine(rotate=5)),
            iaa.Sometimes(0.5,iaa.GaussianBlur(sigma=(0, 0.5))),
            iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
        ]),
        iaa.Resize(pixel)
    ],
    random_order=True)
    images_aug = np.array([aug_pipeline.augment_image(np.asarray(image)) for _ in range(numbers)])
    Path(f"C://augimg/{search_name}").mkdir(parents=True, exist_ok=True)
    for i, augimg in enumerate(images_aug):
        im = Image.fromarray(augimg)
        im = im.convert('RGB')
        im.save(f"C:/augimg/{search_name}/{time.time()}.png")



def search_selenium(search_name, search_limit, pixel, numbers) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome('C:/chromedriver.exe', options=options)
    browser.implicitly_wait(3)
    browser.get(search_url)
    time.sleep(1)

    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    Path(f"C:/img/{search_name}").mkdir(parents=True, exist_ok=True)

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Chrome/90.0.4430.212')]
    urllib.request.install_opener(opener)
    
    images = browser.find_elements_by_class_name("rg_i.Q4LuWd")
    cnt = 1
    for img in images[:search_limit]:
        try:
            img.click()
            time.sleep(2)
            img_xpath = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img'
            img_element = browser.find_element_by_xpath(img_xpath)
            img_url = img_element.get_attribute("src")
            urllib.request.urlretrieve(img_url, f"C:/img/{search_name}/{cnt}.png")
            print(f'downloading.........{cnt}.jpg')
            image = Image.open(f'C:/img/{search_name}/{cnt}.png')
            augment(image, pixel, search_name, numbers)
            cnt += 1
        except:
            pass
    browser.close()
 
if __name__ == "__main__" :
    search_name = input("Image to crawl: ")
    search_limit = int(input("Number of images: "))
    pixel = int(input("Image size wanted: "))
    numbers = int(input("How many augmentations per image?: "))
    print("Crawl Start")
    begin = time.time()
    search_selenium(search_name, search_limit, pixel, numbers)
    print("Crawl End")
    end = time.time()
    print(f"Crawling time: {str(end-begin)} seconds")


from selenium import webdriver
import time

def main():
    driver = webdriver.Chrome()
    driver.get("https://steambuy.com/draw/")
    button = driver.find_element_by_class_name("draw-item__btn_take")
    button.click()
    login = driver.find_element_by_name("email").send_keys("89524092018")
    password = driver.find_element_by_name("pass").send_keys("464fak10")
    vk_button = driver.find_element_by_id("install_allow")
    vk_button.click()
    a = driver.find_element
if __name__ == "__main__":
    while True:
        main()
        print("Запись прошла успешно!")
        print("Так, уже записался!")
        time.sleep(14400)
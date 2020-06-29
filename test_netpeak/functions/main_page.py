import os
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.main_page_link = "https://netpeak.ua/"
        self.logo_link = "//img[@alt='Netpeak']"
        self.career_link = "//nav[@id='main-menu']/ul/li[5]/a[contains(@href, 'career.netpeak.ua') and text()='Карьера']"
        self.hiring_link = "//a[contains(@href, 'career.netpeak.ua/hiring/') and text() = 'Я хочу работать в Netpeak']"
        self.cv_upload_button_path = "//input[@type='file']"
        self.cv_upload_png_error_path = "// div[ @ id = 'up_file_name'] / label[text() = 'Ошибка: неверный формат " \
                                        "файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf).']"

        self.first_name_input_path = "//input[@id='inputName']"
        self.last_name_input_path = "//input[@id='inputLastname']"
        self.email_input_path = "//input[@id='inputEmail']"
        self.year_input_path = "//select[@name='by']"
        self.month_input_path = "//select[@name='bm']"
        self.day_input_path = "//select[@name='bd']"
        self.phone_numb_input_path = "//input[@id='inputPhone']"

        self.submit_button_path = "//button[@id='submit']"

        self.wrong_file_form_path = "//label[text()='Ошибка: неверный формат файла (разрешённые форматы: " \
                                    "doc, docx, pdf, txt, odt, rtf).']"

        self.all_fields_text_red_error_path = "//p[text()='Все поля являются обязательными для заполнения']" \
                                              "/parent::div[@class='form-group has-error']"

    def open_main_page(self):
        self.driver.get(self.main_page_link)
        WebDriverWait(self.driver, 5).until(EC.title_contains("Раскрутка сайта, продвижение сайтов"))

    def click_on_logo(self):
        self.driver.find_element_by_xpath(self.logo_link).click()
        WebDriverWait(self.driver, 5).until(EC.title_contains("Раскрутка сайта, продвижение сайтов"))
        return self

    def click_career_link(self):
        self.driver.find_element_by_xpath(self.career_link).click()
        WebDriverWait(self.driver, 5).until(EC.title_contains("Работа в Netpeak"))
        return self

    def click_hiring_form(self):
        self.driver.find_element_by_xpath(self.hiring_link).click()
        WebDriverWait(self.driver, 5).until(EC.title_contains("Заполнение анкеты на вакансию — Netpeak Украина"))

        return self

    def fill_personal_data_form(self, name=None, lastname=None, email=None, phone=None, file=None):
        if name and lastname and email and phone:
            self.driver.find_element_by_xpath(self.first_name_input_path).send_keys(name)
            self.driver.find_element_by_xpath(self.last_name_input_path).send_keys(lastname)
            self.driver.find_element_by_xpath(self.email_input_path).send_keys(email)

            select_year = Select(self.driver.find_element_by_xpath(self.year_input_path))
            random.choice(select_year.options).click()

            select_month = Select(self.driver.find_element_by_xpath(self.month_input_path))
            random.choice(select_month.options).click()

            select_day = Select(self.driver.find_element_by_xpath(self.day_input_path))
            random.choice(select_day.options).click()

            self.driver.find_element_by_xpath(self.phone_numb_input_path).send_keys(phone)

        if file:
            self.driver.find_element_by_xpath(self.cv_upload_button_path).send_keys(os.getcwd() + file)

        return self

    def send_resume(self):
        self.driver.find_element_by_xpath(self.submit_button_path).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.all_fields_text_red_error_path)))
        return self

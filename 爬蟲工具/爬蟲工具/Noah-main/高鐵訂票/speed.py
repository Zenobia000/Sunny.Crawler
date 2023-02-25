from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import re
import ddddocr 
import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import undetected_chromedriver as uc

# 指令區
def info_accept():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cookieAccpetBtn"]'))).click()
def start_station():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[1]/div/select/option[10]'))).click()
def end_station():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[2]/div/select/option[3]'))).click()
def date_choose1():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="BookingS1Form"]/div[3]/div[2]/div/div[1]/div[1]/input[2]'))).click()
def date_choose2():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div[2]/div/div[2]/div[2]/span[18]'))).click()
def time_choose():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="BookingS1Form"]/div[3]/div[2]/div/div[2]/div[1]/select/option[29]'))).click()
def people_choose():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="BookingS1Form"]/div[4]/div[1]/div[1]/div/select/option[4]'))).click()
def send_code():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="securityCode"]'))).send_keys(get_code().upper())
def submit():
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="SubmitButton"]'))).click()
def get_code():
    ocr = ddddocr.DdddOcr()
    res = ocr.classification(img_base64)
    return res
def refresh():
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="BookingS1Form_homeCaptcha_reCodeLink"]/span'))).click()
def p2_submit():
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="BookingS2Form"]/section[2]/div/div/input'))).click()
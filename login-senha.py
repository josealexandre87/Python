from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\chromedriver')
driver.implicitly_wait(10)

def login():
    id_login = 'id_userLoginId'
    id_pass = 'id_password'
    id_btn = 'btn login-button btn-submit btn-small'
    login = 'admim'
    passw = '12345'
    driver.get('https://www.netflix.com/br/login')
    input_login = driver.find_element(id_login)
    input_pass = driver.find_element(id_pass)
    btn_login = driver.find_element(id_btn)
    input_login.send_keys(login)
    input_login.send_keys(passw)
    btn_login.click()


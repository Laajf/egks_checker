from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_data_money(number_card):
    print("Starting the script...")

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless=new")  # Вместо обычного "--headless"
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--remote-debugging-port=9222")  # для отладки

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://payberry.ru/pay/4253/")

        # Вместо find_element_by_id используем find_element с By.ID
        email_form = driver.find_element(By.CLASS_NAME, "field-row__input")
        email_form.send_keys(f"{number_card}")

        entered_value = email_form.get_attribute("value")
        print(f"Entered value: {entered_value}")

        if entered_value == f"{number_card}":
            print("наконец-то")
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".g-btn.m-btn-lg.request-btn"))
            )
            button.click()
            print("Button clicked")

            print("Waiting for text 'Текущий билет:' to appear...")
            ticket_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Текущий билет:')]"))
            )
            print("Text 'Текущий билет:' appeared.")

            ticket_text = ticket_element.text
            print(f"Found text: {ticket_text}")

    except Exception as e:
        print(f"Element not found or another error occurred: {e}")
    finally:
        driver.quit()

get_data_money("000464198")
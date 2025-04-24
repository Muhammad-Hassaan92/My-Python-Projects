from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
time.sleep(10)  # Wait for WhatsApp Web to load

def open_group(group_name):
    """Search and open the WhatsApp group."""
    search_box_xpath = '//div[@contenteditable="true"][@title="Search input textbox"]'
    try:
        search_box = driver.find_element(By.XPATH, search_box_xpath)
        search_box.click()
        search_box.send_keys(group_name)
        time.sleep(3)
        search_box.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Error opening group: {e}")

def create_poll(question, options):
    """Creates a poll in the opened group."""
    try:
        # Click the attachment (paperclip) button
        attach_button_xpath = '//div[@title="Attach"]'
        attach_button = driver.find_element(By.XPATH, attach_button_xpath)
        attach_button.click()
        time.sleep(2)

        # Click the poll option (WhatsApp might change this)
        poll_button_xpath = '//span[contains(text(),"Poll")]'
        poll_button = driver.find_element(By.XPATH, poll_button_xpath)
        poll_button.click()
        time.sleep(2)

        # Enter poll question
        question_box_xpath = '//div[@contenteditable="true"]'
        question_box = driver.find_elements(By.XPATH, question_box_xpath)[0]
        question_box.send_keys(question)
        time.sleep(1)

        # Enter poll options
        option_boxes = driver.find_elements(By.XPATH, question_box_xpath)[1:]  # Exclude the first (question) box
        for i, option in enumerate(options):
            if i < len(option_boxes):
                option_boxes[i].send_keys(option)
                time.sleep(0.5)
        
        # Send the poll
        send_button_xpath = '//button[@aria-label="Send"]'
        send_button = driver.find_element(By.XPATH, send_button_xpath)
        send_button.click()
        time.sleep(2)

        print("Poll created successfully!")

    except Exception as e:
        print(f"Error creating poll: {e}")

if __name__ == "__main__":
    group_name = "Your Group Name Here"  # Replace with actual group name
    poll_question = "Which programming language do you prefer?"
    poll_options = ["Python", "JavaScript", "C++", "Java"]

    open_group(group_name)
    time.sleep(2)
    create_poll(poll_question, poll_options)

    driver.quit()

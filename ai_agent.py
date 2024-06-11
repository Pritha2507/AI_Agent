from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to ChromeDriver
driver_path = '/Users/admin/Desktop/chromedriver'

# Dummy data
dummy_data = {
    'first_name': 'Ria',
    'middle_name': 'Rim',
    'last_name': 'Bose',
    'street_address': '123 Main St',
    'address_line_2': 'Apt 101',
    'city': 'Mumbai',
    'state': 'Maharashtra',
    'zip_code': '10001',
    'email': 'example@example.com',
    'phone': '1234567890',
    'linkedin': 'https://linkedin.com/in/riabose',
    'ai_agents_interest': 'AI agents are revolutionizing various industries by automating tasks and providing intelligent solutions.',
    'web_automation_interest': 'Web automation enables seamless interaction with web applications, improving efficiency and accuracy.',
    'cover_letter': 'I am excited about the opportunity to apply for this position. Please find attached my resume for your consideration.'
}

def fill_form():
    try:
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get('https://form.jotform.com/241617189501153')
        time.sleep(2)  # Allow the page to load

        # Fill in the name
        first_name_field = driver.find_element(By.NAME, 'q3_fullName3[first]')
        middle_name_field = driver.find_element(By.NAME, 'q3_fullName3[middle]')
        last_name_field = driver.find_element(By.NAME, 'q3_fullName3[last]')
        first_name_field.send_keys(dummy_data['first_name'])
        middle_name_field.send_keys(dummy_data['middle_name'])
        last_name_field.send_keys(dummy_data['last_name'])

        # Fill in the address
        street_address_field = driver.find_element(By.NAME, 'q7_address[addr_line1]')
        address_line_2_field = driver.find_element(By.NAME, 'q7_address[addr_line2]')
        city_field = driver.find_element(By.NAME, 'q7_address[city]')
        state_field = driver.find_element(By.NAME, 'q7_address[state_code]')
        zip_code_field = driver.find_element(By.NAME, 'q7_address[postal]')
        street_address_field.send_keys(dummy_data['street_address'])
        address_line_2_field.send_keys(dummy_data['address_line_2'])
        city_field.send_keys(dummy_data['city'])
        state_field.send_keys(dummy_data['state'])
        zip_code_field.send_keys(dummy_data['zip_code'])

        # Fill in email and phone number
        email_field = driver.find_element(By.NAME, 'q5_email')
        phone_field = driver.find_element(By.NAME, 'q10_mobileNumber')
        email_field.send_keys(dummy_data['email'])
        phone_field.send_keys(dummy_data['phone'])

        # Fill in LinkedIn URL
        linkedin_field = driver.find_element(By.NAME, 'q8_linkedin')
        linkedin_field.send_keys(dummy_data['linkedin'])

        # Fill in interesting facts
        ai_agents_field = driver.find_element(By.NAME, 'q13_aiAgentsInterest')
        web_automation_field = driver.find_element(By.NAME, 'q14_webAutomationInterest')
        ai_agents_field.send_keys(dummy_data['ai_agents_interest'])
        web_automation_field.send_keys(dummy_data['web_automation_interest'])

        # Reverse a LinkedList (fill in with any answer)
        reverse_linkedlist_field = driver.find_element(By.NAME, 'q15_reverseLinkedList')
        reverse_linkedlist_field.send_keys('A LinkedList can be reversed by iterating through it and changing the pointers.')

        # Upload resume
        resume_upload = driver.find_element(By.NAME, 'q9_uploadResume')
        resume_upload.send_keys('/Users/admin/Desktop/Resume_2024-03-17_7744260.pdf')

        # Fill in cover letter
        cover_letter_field = driver.find_element(By.NAME, 'q11_coverLetter')
        cover_letter_field.send_keys(dummy_data['cover_letter'])

        # Submit the form
        submit_button = driver.find_element(By.ID, 'input_2')
        submit_button.click()

        # Close the browser after submission
        time.sleep(5)  # Wait for submission to complete

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    fill_form()

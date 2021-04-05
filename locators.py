from selenium.webdriver.common.by import By

locator = {
    "submit_message_btn": (By.ID, "submitMessage"),
    "message": (By.ID, "message"),
    "attach_file_button": (By.ID, "fileUpload"),
    "order_refrence": (By.ID, "id_order"), 
    "email": (By.ID, "email"),
    "subject_heading": (By.ID, "id_contact"),
    "contact_us": (By.XPATH, "//*[@id='contact-link']/a")
}

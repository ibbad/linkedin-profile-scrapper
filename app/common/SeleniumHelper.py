import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumHelper:
    driver = None
    TIMEOUT = 99999
    defaultWaitForUrlResponse = 5           # in seconds

    def load_page(self, page):
        try:
            self.driver.get(page)
            return True
        except:
            return False

    def submit_form(self, element):
        try:
            element.submit()
            return True
        except TimeoutException:
            return False

    def wait_show_element(self, selector, wait=99999):
        try:
            wait = WebDriverWait(self.driver, wait)
            element = wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, selector)))
            return element
        except:
            return None

    def wait_hide_element(self, selector, wait):
        try:
            wait = WebDriverWait(self.driver, wait)
            element = wait.until(EC.invisibility_of_element_located((
                By.CSS_SELECTOR, selector)))
            return element
        except:
            return None

    def get_element_from(self, from_object, selector):
        try:
            return from_object.find_element_by_css_selector(selector)
        except NoSuchElementException:
            return None

    def get_elements_from(self, from_object, selector):
        try:
            return from_object.find_element_by_css_selector(selector)
        except NoSuchElementException:
            return None

    def get_element(self, selector):
        return self.get_element_from(self.driver, selector)

    def get_elements(self, selector):
        return self.get_elements_from(self.driver, selector)

    def get_element_from_value(self, from_object, selector):
        element = self.get_element_from(from_object, selector)
        return self.get_value(element)

    def get_element_value(self, selector):
        element = self.get_element(selector)
        return self.get_value(element)

    def get_value(self, element):
        if element:
            return element.text
        return None

    def get_attribute(self, element, attribute):
        if element:
            return element.get_attribute(attribute)
        return None

    def get_element_from_attribute(self, from_object, selector, attribute):
        element = self.get_element_from(from_object, selector)
        return self.get_attribute(element, attribute)

    def get_element_attribute(self, selector, attribute):
        element = self.get_element(selector)
        return self.get_attribute(element, attribute)

    def get_parent_levels(self, node, levels):
        path = '..'
        if levels > 1:
            for i in range(1, levels):
                path += '/..'
        return node.find_element_by_xpath(path)

    def get_parent_node(self, node):
        return node.find_element_by_xpath('../')

    def get_child_nodes(self, node):
        return node.find_element_by_xpath('./*')

    def select_and_write(self, field, value):
        field_obj = self.get_element(field)
        field_obj.send_keys(value)
        return field_obj

    def wait_and_write(self, field, value):
        field_obj = self.wait_show_element(field, self.TIMEOUT)
        field_obj.send_keys(value)
        return field_obj

    def press_enter(self, field_object):
        return field_object

    def click_selector(self, selector):
        element = self.get_element(selector)
        if element:
            try:
                actions = webdriver.ActionChains(self.driver)
                actions.move_to_element(element)
                actions.click(element)
                return True
            except:
                return False
        return False

    def click(self, element):
        actions = webdriver.ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    def move_to_element(self, element):
        self.driver.execute_script('return arguments[0].scrollIntoView();',
                                   element)
        actions = webdriver.ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, "
                                   "document.body.scrollHeight);")

    def scrolling_down(self, times):
        for i in range(1, times):
            self.scroll_down()
            time.sleep(0.5)

    def get_field_value(self, record, parent=None):
        ext = None
        if parent:
            if record['type'] == 'attr':
                if record['selector']:
                    ext = self.get_element_from_attribute(parent,
                                                          record['selector'],
                                                          record['attr'])
                else:
                    ext = self.get_attribute(parent)
            elif record['type'] == 'text':
                if record['selector']:
                    ext = self.get_element_from_value(parent,
                                                      record['selector'])
                else:
                    ext = self.get_value(parent)
            elif record['type'] == 'style':
                ext = record['attr']
        else:
            if record['type'] == 'attr':
                ext = self.get_element_attribute(record['selector'],
                                                 record['attr'])
            elif record['type'] == 'text':
                ext = self.get_element_value(record['selector'])
            elif record['type'] == 'style':
                ext = record['attr']
        return ext

    def extract_section(self, section):
        ext = {}
        for subsection in self.SECTIONS[section]:
            container = self.SECTIONS[section][subsection]
            if container['quantity'] == 'multiple':
                ext[subsection] = []
                elements = self.get_elements(container['selector'])
                for element in elements:
                    row = {}
                    for field in self.FIELDS[section][subsection]:
                        record = self.FIELDS[section][subsection][field]
                        row[field] = self.get_field_value(record, element)
                    ext[subsection].append(row)
            elif container['quantity'] == 'single':
                ext[subsection] = self.get_field_value(container)
        return ext

    def save_screenshot(self, file_path):
        """
        Save screen shot to given file path.
        :param file_path: file path to save screenshot.
        :return:
        """
        self.driver.save_screenshot(file_path)

    def load_and_wait(self, url, selector, wait=99999):
        """
        Load page and wait until it is completely loaded.
        :param url: url of the page to be loaded
        :param selector: the element which needs to be loaded.
        :param wait: time to wait for selector to be loaded.
        :return:
        """
        self.load_page(url)
        return self.wait_show_element(selector, wait)

    def close(self):
        """
        Close the selenium driver.
        :return:
        """
        self.drive.quit()

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from toolbelt import base_url_mock
from toolbelt import base_url_snz
import allure


class TestPageLoader:
    def test_init_page(self):
        self.driver.get(base_url_snz)
        self.driver.implicitly_wait(10)
        assert self.driver.title == "Snezana 2.4.0"


class TestTooltips:
    def cls_config(self):
        wait = WebDriverWait(self.driver, 10)
        return wait

    def test_copymarkup_tooltip(self):
        copymarkup_tooltip = 'Copy markup'
        actual_copymarkup_tooltip = self.driver.find_element_by_class_name('copy-btn').get_attribute('title')
        assert copymarkup_tooltip == actual_copymarkup_tooltip

    def test_pastemarkup_tooltip(self):
        pastemakup_tooltip = 'Paste markup'
        actual_pastemakup_tooltip = self.driver.find_element_by_class_name('paste-btn').get_attribute('title')
        assert pastemakup_tooltip == actual_pastemakup_tooltip

    def test_annotationrules_tooltip(self):
        annotationrules_tooltip = 'Annotation rules'
        actual_annotationrules_tooltip = self.driver.find_elements_by_class_name('nav__header_r d-flex wrap justify-content-between align-items-center')[0].get_attribute('title')
        assert annotationrules_tooltip == actual_annotationrules_tooltip

    def test_shortcutsmousegestures_tooltip(self):
        shortcuts_tooltip = 'Shortcuts'
        actual_shortcuts_tooltip = self.driver.find_elements_by_class_name('nav__header_r d-flex wrap justify-content-between align-items-center')[1].get_attribute('title')
        assert shortcuts_tooltip == actual_shortcuts_tooltip

    def test_objects_tooltip(self):
        objects_tooltip = 'Objects area'
        actual_objects_tooltip = self.driver.find_element_by_class_name('dropdown dropdown_blue').get_attribute('title')
        assert objects_tooltip == actual_objects_tooltip

    def test_boundaryboxesaddbuttons_tooltip(self):
        pass

    def test_deleteoblect_tooltip(self):
        pass

    def test_keyframe_tooltip(self):
        pass

    def test_keyframebuttons_tooltip(self):
        pass

    def test_keyframebuttons2_tooltip(self):
        pass

    def test_invalidvideo_tooltip(self):
        pass

    def test_devicelocation_tooltip(self):
        pass

    def test_precipitations_tooltip(self):
        pass

    def test_colormode_tooltip(self):
        pass

    def test_importantvideo_tooltip(self):
        pass


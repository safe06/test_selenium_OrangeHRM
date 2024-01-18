# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

opts = ChromeOptions()
opts.add_argument("--window-size=2560,1440") 

class LoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_logout(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME,"username").click()
        driver.find_element(By.NAME,"username").clear()
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").click()
        driver.find_element(By.NAME,"password").clear()
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.save_screenshot("screenshot/orangeHRM.png")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class GererMesInformation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_gerer_mes_information(self):
        driver = self.driver

        # Connexion
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME,"username").click()
        driver.find_element(By.NAME,"username").clear()
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").click()
        driver.find_element(By.NAME,"password").clear()
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()

        # Naviguer sur la page viewPersonalDetails
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[6]/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7")

        # Modifier les données 
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div/div/div/div/div[2]/div/div/div[2]/i").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button").click()

        la_liste_des_info= driver.find_elements(By.XPATH, "//div[@class='orangehrm-tabs-wrapper']")

        for info in la_liste_des_info:
            print(f'info : {info.text}')
            if info.text == 'Salary' :
                print("there is Salary in the list")
        
        # driver.save_screenshot("screenshot/orangeHrm-infordadmin.png")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[8]/a/span").click() 

       
        # Déconnexion 
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class AddLikeDeletePost(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_like_delete_post(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME,"username").click()
        driver.find_element(By.NAME,"username").clear()
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").click()
        driver.find_element(By.NAME,"password").clear()
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[12]/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
        driver.find_element(By.ID,"heart").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div/div/div[2]/form/div/textarea").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div/div/div[2]/form/div/textarea").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div/div/div[2]/form/div/textarea").send_keys("It's time to eat")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.save_screenshot("screenshot/posterdansBUZZ.png")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[3]/div[3]/div/div/div/div[2]/li/button/i").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[3]/div[3]/div/div/div/div[2]/li/ul/li/p").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class AddRemoveCandidat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_remove_candidat(self):
        driver = self.driver

        # Connexion
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME,"username").click()
        driver.find_element(By.NAME,"username").clear()
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").click()
        driver.find_element(By.NAME,"password").clear()
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()

        # Navigation sur la page recruitment 
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[5]/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        #le nombre initial des candidats 
        list_initial = driver.find_elements(By.XPATH,"//div[@class='oxd-table']/div/div[@class='oxd-table-card']")

        nombre_initial = len(list_initial)

        # Suppression des candidats
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/label/span/i").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/div/div/div/div/label/span/i").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[2]/div/div/button").click()
        driver.save_screenshot("screenshot/deleteCandidat.png")
        driver.find_element(By.XPATH,"//div[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()

        # Ajout des candidats
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()

        for index in range(5):
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")
            driver.find_element(By.NAME,"firstName").click()
            driver.find_element(By.NAME,"firstName").clear()
            driver.find_element(By.NAME,"firstName").send_keys(f"paul{index}")
            driver.find_element(By.NAME,"lastName").click()
            driver.find_element(By.NAME,"lastName").clear()
            driver.find_element(By.NAME,"lastName").send_keys(f"kack{index}")
            driver.save_screenshot("screenshot/addCandidat.png")
            driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div").click()
            driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").clear()
            driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").send_keys(f"paul@gmail.com{index}")
            driver.find_element(By.XPATH,"//button[@type='submit']").click()
            driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[5]/a/span").click()

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        # Nombre des candidats aprés modification 
        list_final = driver.find_elements(By.XPATH,"//div[@class='oxd-table']/div/div[@class='oxd-table-card']")

        nombre_final = len(list_final)

        # Vérification des modification dans la liste des candidats 
        self.assertNotEqual(nombre_final,nombre_initial)

        print(f'Le nombre des candidats initial : {nombre_initial} aprés modification le nombre des candidats final est {nombre_final}')

        # Déconnecion 
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class AddProjectCheckList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_project_check_list(self):
        driver = self.driver

        # Connexion
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME,"username").click()
        driver.find_element(By.NAME,"username").clear()
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").click()
        driver.find_element(By.NAME,"password").clear()
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()

        # Navigation sur la page viewEmployeeTimesheet
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.LINK_TEXT,"Time").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li[4]/span").click()
        driver.find_element(By.LINK_TEXT,"Projects").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewProjects")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()

        # Ajouter un projet 
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/saveProject")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div[2]/input").send_keys("recrutement_phase2")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/input").send_keys("Internal")
        driver.save_screenshot("screenshot/projet_ajouté.png")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li[4]/span").click()
        driver.find_element(By.LINK_TEXT,"Projects").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li[4]/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewProjects")

        
        nombres_des_projets = driver.find_elements(By.XPATH,"//div[@class='orangehrm-container']/div/div[@class='oxd-table-body']/div[@class='oxd-table-card']")
        assert len(nombres_des_projets) == 11, "Y'a une changement dans la liste.. Vérifier SVP!"

        driver.save_screenshot("screenshot/checklist_project.png")

        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[8]/a/span").click()

        # Déconnexion 
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

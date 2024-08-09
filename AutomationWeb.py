from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AutomationWeb:

    def __init__(self, tempo_de_espera) -> None:
        self.opcoes = webdriver.ChromeOptions()
        self.opcoes.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.opcoes)
        self.driver.implicitly_wait(tempo_de_espera)
        self.elemento = None
        
        
    def abrir_navegador(self, url: str) -> None:
        self.driver.get(url)
        
    def fechar_navegador(self):
        self.driver.quit()
        
    def pegar_titulo_navegador(self, titulo_esperado: str) -> None:
        titulo = self.driver.title
        if titulo == titulo_esperado:
            print('Página acessada com sucesso')
        
    def esperar(self, segundos: int) -> None:
        self.driver.implicitly_wait(segundos)
        print('aguardando...')
        
    def encontrar_elemento_xpath(self, elemento: str) -> None:
        self.elemento = self.driver.find_element(by=By.XPATH, value=elemento)
        print(self.elemento)
        print('Elemento encontrado xpath')
    
    def encontrar_elemento_name(self, elemento: str) -> None:
        self.elemento = self.driver.find_element(by=By.NAME, value=elemento)
        print(self.elemento)
        print('Elemento encontrado name')
        
    def encontrar_elemento_id(self, elemento: str) -> None:
        self.elemento = self.driver.find_element(by=By.ID, value=elemento)
        print(self.elemento)
        print('Elemento encontrado id')
        
    def encontrar_elemento_class(self, elemento: str) -> None:
        self.elemento = self.driver.find_element(by=By.CLASS_NAME, value=elemento)
        print(self.elemento)
        print('Elemento encontrado class')
        
    def encontrar_elemento_content(self, elemento: str) -> None:
        self.elemento = self.driver.find_element(by=By.LINK_TEXT, value=elemento)
        print(self.elemento)
        print('Elemento encontrado content')
    
    def encontrar_elemento_css_selector(self, elemento: str) -> None:
        self.elemento = self.driver.find_element(by=By.CSS_SELECTOR, value=elemento)
        print(self.elemento)
        print('Elemento encontrado css selector')
    
    def clicar_elemento(self) -> None:
        if self.elemento == None:
            print('Nenhum elemento foi localizado')
        self.elemento.click()
        self.elemento = None
        print('Botão clicado com sucesso')
        
    def click_wait(self):
        element = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'helper-div')))
        time.sleep(5)
        print(element.is_displayed())
        self.elemento.click()
        self.elemento = None
        print('Botão espera clicado com sucesso')
        
        
    def digitar(self, texto) -> None:
        self.elemento.send_keys(texto)
        print('Digitado com sucesso')
        
    def trocar_janela(self):
        # janela_atual = self.driver.current_window_handle
        janelas = self.driver.window_handles
        
        # for janela in janelas:
        #     if janela != janela_atual:
        #         nova_janela = janela
        
        self.driver.switch_to.window(janelas[-1])
        
    def verificar_janelas(self):
        janela_atual = self.driver.current_window_handle
        janelas = self.driver.window_handles
        print(janela_atual)
        print(janelas)
        conteudo = self.driver.page_source
        print(conteudo)

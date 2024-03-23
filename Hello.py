import streamlit as st
from streamlit.logger import get_logger
from playwright.async_api import async_playwright
import asyncio

BETFAIR = "https://www.betfair.com/exchange/plus/pt/futebol-apostas-1/inplay"

async def Obter_Jogos_Vivo(PAGINA):
    async with async_playwright() as p:

        print(f'Processo para obter a página {PAGINA} iniciado.')

        # Iniciação do Navegador e definição do contexto aplicado
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            locale='pt-BR',
            timezone_id='America/Sao_Paulo',
            extra_http_headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'Accept-Language': 'pt-BR,en;q=0.9'})

        # Criação de uma página usando o contexto aplicado.
        page = await context.new_page()
        await page.goto(BETFAIR)
        await page.wait_for_timeout(5000)
        await page.screenshot(path='screenshot1.png')


        # Identificação, localizçaão e click no botão para aceitar os cookies

        # Clique abrir as opções de "Visualiza por"
        await page.locator(
            '//*[@id="onetrust-accept-btn-handler"]'
        ).click()


        # Clique abrir as opções de "Visualiza por"
        await page.locator(
            '//*[@id="main-wrapper"]/div/div[2]/div/ui-view/ui-view/div/div/div/div/div[1]/div/div[1]/bf-super-coupon/main/ng-include[2]/section/div[1]/div/bf-select/div/label'
        ).click()

        # Seleciona a opção para "Visualiza por Data"
        await page.locator(
            '//*[@id="main-wrapper"]/div/div[2]/div/ui-view/ui-view/div/div/div/div/div[1]/div/div[1]/bf-super-coupon/main/ng-include[2]/section/div[1]/div/bf-select/div/div/bf-option[2]/span'
        ).click()

        await page.goto(BETFAIR + "/" + str(PAGINA))

        # Espera 5 segundos para a página carregar
        await page.wait_for_timeout(5000)

        # Obtém o html da página
        html = await page.content()
        await browser.close()

    print(f'Página {PAGINA} obtida.')

    # Retorna o html da página
    return html


def run():
    st.set_page_config(
        page_title="Betfair App",
    )

    Codigohtml = asyncio.run(Obter_Jogos_Vivo(1))
    st.code(Codigohtml, language="cshtml", line_numbers=False)

    st.write("# Welcome to Streamlit! 👋")

run()

from setuptools import setup, find_packages

setup(
    name="robo_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyautogui",
        "pyinstaller",
        "setuptools",
        "Selenium"
    ],

    author="Radier",
    author_email = "estagiario.seg@parenteandrade.com.br",
    description="Automação de gerar relatorio de ASO'S a vencer"
)
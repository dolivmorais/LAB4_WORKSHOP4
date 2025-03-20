from frontend import ExcelValidatorUI
from backend import process_excel

def main():
    ui = ExcelValidatorUI()
    ui.display_header()

    uploaded_file = ui.upload_file()  # Chame uma vez e armazene

    if uploaded_file is not None:  # Verifique se o arquivo foi carregado
        result, erros = process_excel(uploaded_file)
        ui.display_results(result, erros)

if __name__ == '__main__':
    main()

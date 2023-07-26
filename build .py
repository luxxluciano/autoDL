import os
import shutil
import sys
import socket
from datetime import datetime

log_file = "W10Mobilidade_OFFLINE_V3.log"
log_separator = "===========================================================================================\n"

# Função para copiar e juntar os arquivos em um arquivo ZIP
def create_zip():
    file_prefix = "W10Mobilidade_OFFLINE_V3."
    zip_filename = "W10Mobilidade_OFFLINE_V3.zip"

    total_files = 25
    progress_width = 50

    with open(log_file, "a") as log:
        log.write(log_separator)
        log.write(socket.gethostname() + "\n")
        log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        log.write(log_separator)

        print("*=================================*")
        print("*   Aguarde alguns minutos..      *")
        print("* Inicia criacao de arquivo ZIP   *")
        print("*=================================*")

        log.write("*=================================*\n")
        log.write("*   Aguarde alguns minutos..      *\n")
        log.write("* Inicia criacao de arquivo ZIP   *\n")
        log.write("*=================================*\n")
        log.write(log_separator)
        log.write(datetime.now().strftime("%H:%M:%S") + "  Inicia junção dos arquivos\n")

        # Lista dos arquivos a serem copiados
        files_to_copy = [file_prefix + f"{i:03}" for i in range(1, total_files + 1)]
        zip_file_path = os.path.join(os.getcwd(), zip_filename)

        try:
            with open(zip_file_path, "wb") as zip_file:
                for i, file_to_copy in enumerate(files_to_copy, 1):
                    with open(file_to_copy, "rb") as part_file:
                        shutil.copyfileobj(part_file, zip_file)

                    progress = i / total_files
                    sys.stdout.write("\rProgresso: [{:<{}}] {}%".format("=" * int(progress * progress_width), progress_width, int(progress * 100)))
                    sys.stdout.flush()

            print("\nArquivo {} gerado com sucesso.".format(zip_filename))
            log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Arquivo " + zip_filename + " gerado com sucesso\n")
            log.write(log_separator)

        except Exception as e:
            print("\nErro ao criar o arquivo ZIP: {}".format(e))
            log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Erro ao criar o arquivo ZIP: {}\n".format(e))
            log.write(log_separator)

# Execução da função para criar o arquivo ZIP
create_zip()

print("*===================================================================*")
print("* Para a criação do Pendrive W10Mobilidade_OFFLINE_V3, recomendamos  *")
print("* a utilização da ferramenta RUFUS, pois o Pendrive deve ser UEFI   *")
print("*===================================================================*")

input("Pressione Enter para continuar...")

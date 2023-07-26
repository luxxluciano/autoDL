import os
import streamlit as st
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

MAX_CONCURRENT_DOWNLOADS = 5

def download_file(url, filename):
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get("content-length", 0))
        with open(filename, 'wb') as file, tqdm(
                desc=filename,
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                dynamic_ncols=True
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                progress_bar.update(len(chunk))

def main():
    st.title("Download App")
    st.write("Insira as URLs que deseja baixar e escolha a pasta de destino.")

    urls_input = st.text_area("Cole as URLs aqui (uma por linha)")

    # Dropdown menu para selecionar o caminho na máquina local
    folder_path = st.selectbox("Selecione a pasta de destino", os.listdir())

    if st.button("Baixar"):
        urls = urls_input.strip().split('\n')
        if not urls:
            st.warning("Nenhuma URL fornecida.")
            return

        if not folder_path:
            st.warning("Selecione a pasta de destino.")
            return

        st.info("Iniciando o download...")
        with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_DOWNLOADS) as executor:
            futures = [executor.submit(download_file, url, os.path.join(folder_path, url.split("/")[-1])) for url in urls]
            for future in tqdm(futures, desc="Downloads", unit="file"):
                future.result()

        st.success("Downloads concluídos com sucesso!")

if __name__ == "__main__":
    main()

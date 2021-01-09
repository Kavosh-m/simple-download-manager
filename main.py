import requests as re
import subprocess
import os

#link = "https://images.hgmsites.net/lrg/2020-ford-mustang-dick-johnson-limited-edition-by-herrod-performance_100729851_l.jpg"
#link = "https://dl4.lionsdl.pw/Serial/BoJack.Horseman/S06/BoJack.Horseman.S06E01.720p.WEB-DL.x265.PSA.mkv"
#link = "https://i.giphy.com/media/3NtY188QaxDdC/giphy-downsized.gif"
#link = "https://dl6.downloadha.com/hosein/soft/December2020/Windows.10.BME.20H2.Build.19042.685.MSDN.Retail.64bit_www.Downloadha.com_.part1.rar"
#link = "https://soft1.downloadha.com/NarmAfzaar/November2020/BWMeter.9.0_www.Downloadha.com_.zip"
link = input("Paste download link here: ")

try:
    con = re.get(link, stream=True)

    if con.headers.get('content-type')[:4] == 'text':
        print("There is no downloadable content. please check the link and try again.")
    else:
        file_size = float(con.headers.get('content-length')) // 1

        # Extract full name from the link
        def extract_name(link):
            i = 0
            while True:
                i -= 1
                if link[i] == '/':
                    break
            return link[i+1:]

        print("Name:", extract_name(link))

        # Showing file size
        def file_size_(file_size):
            if file_size < 1024:
                print(f'Size: {file_size} Bytes')
            elif 1024 <= file_size < 1024**2:
                print(f'Size: {round(file_size/1024, 2)} KB')
            elif 1024**2 <= file_size < 1024**3:
                print(f'Size: {round(file_size/1024**2, 2)} MB')
            else:
                print(f'Size: {round(file_size/1024**3, 2)} GB')

        file_size_(file_size)


        # Download process
        def download():
            f = open(extract_name(link), 'wb')
            size_now = 0
            counter = 0
            for i in con.iter_content(chunk_size=4096):
                counter += 1
                size_now += len(i)
                percent = round((size_now / file_size) * 100, 2)
                print(f'Progress: {percent} %\r', end='')
                f.write(i)
            f.close()
            print("\nDownload complete")

            # Open folder after download
            while True:
                n = input("Open folder?[Y/N]: ")
                if n == 'Y' or n == 'y':
                    cwd = os.getcwd()
                    subprocess.Popen(f'explorer {cwd}')
                    break
                elif n == 'N' or n == 'n':
                    break
                else:
                    pass


        while True:
            p = input("To start download, press ENTER or press Q to quit: ")
            if p == '':
                download()
                break
            elif p == 'Q' or 'q':
                break
            else:
                pass
except:
    print("connection error. If you live in IRAN, using a VPN is recommended!")
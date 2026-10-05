import sys
import requests
from colorama import init, Fore

init(autoreset=True)

def main():
    print(Fore.CYAN + "="*40)
    print(Fore.GREEN + "MAI SCA Lab 1: Анализ зависимостей")
    print(Fore.CYAN + "="*40)
    print(Fore.YELLOW + f"Версия приложения: 1.0.0")
    print(Fore.YELLOW + f"Версия Python: {sys.version.split()[0]}")
    try:
        ip = requests.get('https://api.ipify.org?format=json', timeout=3).json().get('ip', 'Нет сети')
        print(Fore.WHITE + f"Твой IP: {ip}")
    except:
        print(Fore.RED + "Не удалось получить IP")
    print(Fore.MAGENTA + "\n[!] Для анализа запустите генерацию SBOM.")

if __name__ == "__main__":
    main()
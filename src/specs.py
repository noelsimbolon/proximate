import platform

import cpuinfo
import psutil


def get_computer_specs() -> str:
    """
    :return: computer specs as a string
    """

    # Get CPU information
    cpu_info = cpuinfo.get_cpu_info()
    cpu_model = cpu_info['brand_raw']
    cpu_cores = psutil.cpu_count(logical=True)
    cpu_clock_speed = cpu_info['hz_actual_friendly']
    cpu_cache_size = cpu_info['l3_cache_size'] / 1024 / 1024
    cpu_architecture = cpu_info['arch']

    # Get RAM information
    ram_total = psutil.virtual_memory().total / 1024 / 1024 / 1024
    ram_available = psutil.virtual_memory().available / 1024 / 1024 / 1024
    ram_usage_percent = psutil.virtual_memory().percent

    # Get disk information
    disk_total = psutil.disk_usage('/').total / 1024 / 1024 / 1024
    disk_available = psutil.disk_usage('/').free / 1024 / 1024 / 1024
    disk_usage_percent = psutil.disk_usage('/').percent

    # Get operating system information
    os_name = platform.system()
    os_architecture = platform.architecture()[0]

    # Specs info
    return f"CPU Model: {cpu_model}\n" \
           f"CPU Cores: {cpu_cores}\n" \
           f"CPU Clock Speed: {cpu_clock_speed}\n" \
           f"CPU Cache Size: {cpu_cache_size} MB\n" \
           f"CPU Architecture: {cpu_architecture}\n" \
           f"Total RAM: {ram_total:.2f} GB\n" \
           f"Available RAM: {ram_available:.2f} GB\n" \
           f"RAM Usage: {ram_usage_percent}%\n" \
           f"Total Disk Space: {disk_total:.2f} GB\n" \
           f"Available Disk Space: {disk_available:.2f} GB\n" \
           f"Disk Usage: {disk_usage_percent}%\n" \
           f"Operating System: {os_name}\n" \
           f"OS Architecture: {os_architecture}"

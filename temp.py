# # # import subprocess
# # #
# # #
# # # def get_adb_devices():
# # #     result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
# # #
# # #
# # #     lines = result.stdout.strip().splitlines()
# # #     print((lines))
# # #
# # #     # Skip the first line ("List of devices attached") and extract device IDs
# # #     devices = [line.split()[0] for line in lines[1:] if 'device' in line]
# # #
# # #     return devices
# # #
# # #
# # # device_list = get_adb_devices()
# # # print(device_list)
# #
# #
# # import subprocess
# #
# #
# # def get_adb_devices():
# #     # Run the 'adb devices' command and capture the output
# #     result = subprocess.run(['adb', 'shell','getprop','ro.build.version.release'], capture_output=True, text=True)
# #     print(result)
# #     lines = result.stdout.strip().splitlines()
# #     print(lines)
# #     # devices = [line.split()[0] for line in lines[1:] if 'device' in line and 'offline' not in line]
# #     # return devices
# #
# #
# # # Get the list of devices
# # device_list = get_adb_devices()
# # print(device_list)
#
# class temp:
#     sts=20
#
#     def dri(self):
#         print(self.sts)
#         self.sts=self.sts+1
#
# obj=temp()
# for ch in range(5):
#     obj.dri()
import configparser
import os
import subprocess
#
# raw_data="report\\allureData"
# final_report="report\\allureReport"
# current_dir = os.getcwd()
# rawd=os.path.join(os.getcwd(),raw_data)
# final=os.path.join(os.getcwd(),final_report)
# print(f"full path {rawd}")
# print(f"final path {final}")


raw_data = "report\\allureData"
final_report = "report\\allureReport"
current_dir = os.getcwd()
rawd = os.path.join(current_dir, raw_data)
finald = os.path.join(current_dir, final_report)
# Create directory if it doesn't exist
print(subprocess.run(["where","allure"],check=True))
try:
    subprocess.run(
        ["C:\\Users\\abc\\AppData\\Roaming\\npm\\allure.cmd", "generate", "--single-file", rawd, "-o", finald, "--clean"], check=True)
    print(f"Allure report generated at {finald}")
except subprocess.CalledProcessError:
    print("Failed to generate Allure report")
from cx_Freeze import setup, Executable

executables = [Executable('InterDipl.py',
targetName='Nadezhnost.exe',
base='Win32GUI',
icon=r'D:\STUDING\programhelp\images\icon3.ico')]


includes = ['tkinter', 'numpy', 'PIL', 'turtle', 'ctypes']

zip_include_packages = ['tkinter', 'numpy', 'PIL', 'turtle', 'ctypes']

include_files = [r'D:\STUDING\programhelp\images\icon3.png',
r'D:\STUDING\programhelp\images\Background.png',
r'D:\STUDING\programhelp\images\1_1.jpg',
r'D:\STUDING\programhelp\images\1_2.jpg',
r'D:\STUDING\programhelp\images\1_3.jpg',
r'D:\STUDING\programhelp\images\4_1.jpg',
r'D:\STUDING\programhelp\images\4_2.jpg',
r'D:\STUDING\programhelp\images\5_1.jpg',
r'D:\STUDING\programhelp\images\5_2.jpg',
r'D:\STUDING\programhelp\images\5_3.jpg',
r'D:\STUDING\programhelp\images\5_4.jpg',
r'D:\STUDING\programhelp\images\5_5.jpg',
r'D:\STUDING\programhelp\images\6_1.jpg',
r'D:\STUDING\programhelp\images\6_2.jpg',
r'D:\STUDING\programhelp\images\6_3.jpg',
r'D:\STUDING\programhelp\images\7_1.jpg',
r'D:\STUDING\programhelp\images\7_2.jpg',
r'D:\STUDING\programhelp\images\7_3.jpg',
r'D:\STUDING\programhelp\images\7_4.jpg',
r'D:\STUDING\programhelp\images\7_5.jpg',
r'D:\STUDING\programhelp\images\8_1.jpg',
r'D:\STUDING\programhelp\images\8_2.jpg',
r'D:\STUDING\programhelp\images\8_3.jpg',
r'D:\STUDING\programhelp\images\8_4.jpg',
r'D:\STUDING\programhelp\images\8_5.jpg',
r'D:\STUDING\programhelp\images\9_1.jpg',
r'D:\STUDING\programhelp\images\9_2.jpg',
r'D:\STUDING\programhelp\images\9_3.jpg',
r'D:\STUDING\programhelp\images\10_1.jpg',
r'D:\STUDING\programhelp\images\10_2.jpg',
r'D:\STUDING\programhelp\images\10_3.jpg',
r'D:\STUDING\programhelp\images\10_4.jpg',
r'D:\STUDING\programhelp\images\10_5.jpg',
]

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
'include_files': include_files,
}
}

setup(name='Надежность',
version='0.0.3',
description='Расчет надежности системы, состоящей из указанных элементов',
executables=executables,
options=options)
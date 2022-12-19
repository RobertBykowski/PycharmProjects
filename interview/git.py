import os

# Zmienia aktualny katalog na podany katalog
os.chdir('C:\\Users\\Admin\\PycharmProjects\\pythonProject1')

# Wykonuje comende add
os.system('git add -A')

# Wykonuje commit z podaną wiadomościąpyinstaller
os.system('git commit -am "Dodano nowy plik"')

# Wykonuje push do repozytorium
os.system('git push')

import cx_Oracle, os

print("Prosze podawac sciezki uzywajac '//' oraz konczac tym samym symbolem, np. C://Windows// lub //home//.")

folder_check=False
while(folder_check==False):
  folder_path=raw_input("Podaj sciezke folderu z plikami: ")
  folder_check=os.path.isdir(folder_path)

  if(folder_check==True):
    print("Folder znaleziono")
    print("Znaleziono nastepujace pliki w wybranym folderze: ")
    for file in os.listdir(folder_path):
      if file.endswith(".txt"):
        print(file)
    file_check=False
    while(file_check==False):
      file_path=raw_input("Wybierz plik, ktory chcesz obrobic: ")
      file_check=os.path.exists(folder_path+file_path)
      if(file_check==True):
        print("Wybrany plik jest poprawny")
        break
      else:
        print("Wybrano niepoprawny, lub nieisteniejacy plik")
    break
  else:
    print("Folder nie istnieje, podaj poprawna sciezke.")
filefolder_path=(folder_path+file_path)
print("Wybrany plik to: "+filefolder_path)

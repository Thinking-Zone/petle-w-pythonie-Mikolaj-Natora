import random 
def zgadnij_pudlko():
  skarb = random.randint(1,3) # Losuje pudełko ze skarbem
  print("Wybierz pudełko:))
  if wybór = int(input("Twoje pudełko:))
  if wybór < 1 or wybor > 3:
   print("Pudełko musi być 1,2 lub 3. Spróbuj ponownie.")
   continue
  if wybór == skarb:
   print("Gratulacje! Znalazłeś skarb!")
   break
  else:
   print("Pudło! Spróbuj ponownie.")
  except ValueError:
   print("Podaj liczbę (1,2 lub 3).")
zgadnij_pudełko()

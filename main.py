# Gerekli kütüphanelerimizi ekliyoruz
import requests # pip install requests
from bs4 import BeautifulSoup # pip install BeautifulSoup
from googletrans import Translator # pip install googletrans==3.1.0a0
from tkinter import * # pip install tkinter

# Class objemizi oluşturuyoruz
class Name_Dictionary:
	def __init__(self) -> None:
		# Gerekli Ekran Bilgileri...
		self.root = Tk()
		self.root.title("Name Dictionary")
		self.root.geometry("350x265")
		self.root.resizable(0,0)
		self.root.configure(bg = "gray2")

		# UI güzel gözükmesi için Özelleştirme, Tıklayınca Referans yazısını siler

		def click(event):
			self.name.configure(fg = "gray90",font = ("Arial",9,"bold"),justify="center")
			self.name.delete(0,END)

		# Temel Buton Komutu

		def button_command():
			url = f"https://www.urbandictionary.com/define.php?term={self.name.get()}"

			# URL de verilen Sayfaya bağlanıyoruz
			def get_content():
				response = requests.get(url)
				content = response.content
				return content

			# İsme göre veriyi çekip türkçeye çeviriyoz
			def get_definition(content):
				soup = BeautifulSoup(content,"html.parser")
				definition = soup.find(class_="meaning").text 
				translator = Translator()
				result = translator.translate(definition,dest='tr')
				return result.text

			arg = get_definition(get_content())
			print(arg)
			self.out.configure(text = arg)

		self.name = Entry(
			self.root,
			bg = "gray2",
			fg = "gray70",
			highlightthickness=0,
			font = ("Arial",10,"italic"),
			)
		self.name.insert(1,"          -- Adınız --")
		self.name.pack() 
		self.name.place(x = 100,y = 20,width = 150)
		self.name.bind("<Button-1>",click)

		self.save = Button(
			self.root,
			bg = "gray2",
			fg = "gray90",
			highlightthickness=0,
			text = "Print",
			font = ("Arial",9,"bold"),
			command = button_command
			)
		self.save.pack()
		self.save.place(x = 147,y = 50,width=55)

		self.out = Label(
			self.root,
			bg = "gray3",
			fg = "gray90",
			highlightthickness=0,
			font = ("Arial",10),
			anchor='w',
			wraplength=300,
			justify="left"
			)
		self.out.pack(side=LEFT)
		self.out.place(x = 25,y = 100,width=300,height = 160)
		self.root.mainloop()


if __name__ == "__main__":
	Name_Dictionary()
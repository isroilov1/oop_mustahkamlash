# class Library:
#     def __init__(self, books_number, shelfs_number):
#         self.__shelfs_number = shelfs_number
#         self.__books_number = books_number
#
# class Books(Library):
#     def __init__(self, name, author, genres):
#         self.__name = name
#         self.author = author
#         self.genres = genres
#     def __str__(self):
#         return f"Kitob: {self.__name}"
#
# class Authors(Library):
#     def __init__(self, name, familiya):
#         self.__name = name
#         self.__familiya = familiya
#
#     def __str__(self):
#         return f"Muallif: {self.__name} {self.__familiya}"
#
# class Genres(Library):
#     def __init__(self, name):
#         self.__name = name
#
#     def __str__(self):
#         return f"Janr: {self.__name}"
#
#
# book = Books("Alqasos", "Xoshimov", "Ujas")
# print(book)






# class Xodimlar:
#     def __init__(self, ismi_fam, id, tel_raqam, kunlik, ishlagan_kuni):
#         self.ishlagan_kuni = ishlagan_kuni
#         self.kunlik = kunlik
#         self.tel_raqam = tel_raqam
#         self.id = id
#         self.ismi_fam = ismi_fam
#     def ish_xaqqi(self):
#         print(f"{self.ishlagan_kuni * self.kunlik}$")
# class Menejer(Xodimlar):
#     def __init__(self, ismi_fam, id, tel_raqam, kunlik, ishlagan_kuni):
#         super().__init__(ismi_fam, id, tel_raqam, kunlik, ishlagan_kuni)
#     def ish_xaqqi(self):
#         return f"{self.ishlagan_kuni * self.kunlik}$"
#
# class Dasturchi(Xodimlar):
#     def __init__(self, ismi_fam, id, tel_raqam, kunlik, ishlagan_kuni):
#         super().__init__(ismi_fam, id, tel_raqam, kunlik, ishlagan_kuni)
#     def ish_xaqqi(self):
#         return f"{self.ishlagan_kuni * self.kunlik}$"
#
# xodimlar=[
# Menejer("Solijonov Abror", 1212, "+998991209889", 200, 24),
# Dasturchi("Isroilov Ismoiljon", 2003, "+998991114515", 280, 25)
# ]
# for i in xodimlar:
#     print(f"ism-familiyasi: {i.ismi_fam}, oyligi: {i.ish_xaqqi()}")
# #for loopdan foydalanib chiqarish ham mumkin ekan








# class Musiqalar:
#     def __init__(self, nomi, artist, albums, yoqdi=False):
#         self.albums = albums
#         self.artist = artist
#         self.nomi = nomi
#         self.cnt = 0
#         self.ls = []
#         self.yoqdi = yoqdi
#
#     def tinglash(self):
#         self.ls.append(self.nomi)
#
# class Playlist(Musiqalar):
#     def __init__(self, nomi, artist, albums, yoqdi):
#         super().__init__(nomi, artist, albums, yoqdi)
#
#     def tinglash(self):
#         self.ls.append(self.nomi)
#
#     def add_playlist(self):
#         playlist = []
#         for song in self.ls:
#             a = self.ls.count(song)
#             if a>1:
#                 playlist.append(song)
#         return playlist
#
# class Sevimlilar(Musiqalar):
#     def __init__(self, nomi, artist, albums, yoqdi):
#         super().__init__(nomi, artist, albums, yoqdi)
#
#     def tinglash(self):
#         self.ls.append(self.nomi)
#
#     def sevimli_musics(self):
#         sevimli = []
#         for i in self.ls:
#             print(1)
#             if self.yoqdi==True:
#                 sevimli.append(i)
#         return sevimli
#
#
#
#
# a = Musiqalar("Another love", "aaa", "Love", True)
# # b = Musiqalar("Kabutarlar", "Ulug'bek Raxmatullayev", "Love", False)
# a.tinglash()
# a.tinglash()
# print(a.cnt)
# c = Sevimlilar("Kabutarlar", "Ulug'bek Raxmatullayev", "Love", True)
# c.tinglash()
# c.tinglash()
# print(c.sevimli_musics())









# class Maxsulotlar:
#     def __init__(self, nomi, narxi):
#         self.narxi = narxi
#         self.nomi = nomi
#     def __str__(self):
#         return f"{self.nomi} - {self.narxi}"
# class XaridSavati:
#     def __init__(self):
#         self.mahsulotlar = []
#     def mahsulot_qoshish(self, mahsulot):
#         self.mahsulotlar.append(mahsulot)
#     def mahsulotlar_soni(self):
#         return len(self.mahsulotlar)
#     def umumiy_summa(self):
#         return sum(mahsulot.narxi for mahsulot in self.mahsulotlar)
#     def mahsulotlar_royxati(self):
#         return self.mahsulotlar
# class Mijozlar:
#     def __init__(self, ism, familiya):
#         self.ism = ism
#         self.familiya = familiya
#         self.xarid_savati = XaridSavati()
#
#     def xarid_qilish(self, mahsulot):
#         self.xarid_savati.mahsulot_qoshish(mahsulot)
#
#     def xarid_savati_tarkibi(self):
#         return self.xarid_savati.mahsulotlar_royxati()
#
#     def umumiy_summa(self):
#         return self.xarid_savati.umumiy_summa()
#
# m1 = Maxsulotlar("Olma", 4000)
# m2 = Maxsulotlar("Anor", 5000)
# m3 = Maxsulotlar("Kartoshka", 4500)
#
#
# mijoz1 = Mijozlar("Abduqunduz", "Botirov")
# mijoz2 = Mijozlar("Qodirali", "Sottiyev")
#
#
# mijoz1.xarid_qilish(m1)
# mijoz1.xarid_qilish(m2)
# mijoz2.xarid_qilish(m3)
#
# print(f"{mijoz1.ism}ning xarid savati:")
# for mahsulot in mijoz1.xarid_savati_tarkibi():
#     print(mahsulot)
# print(f"Umumiy summa: {mijoz1.umumiy_summa()}")
#
# print(f"\n{mijoz2.ism}ning xarid savati:")
# for mahsulot in mijoz2.xarid_savati_tarkibi():
#     print(mahsulot)
# print(f"Umumiy summa: {mijoz2.umumiy_summa()}")







class Menyular:
    def __init__(self, nomi, narxi):
        self.narxi = narxi
        self.nomi = nomi
class Buyurtmalar:
    def __init__(self, mahsulotlar):
        self.mahsulotlar = mahsulotlar
    def mahsulot_qoshish(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def mahsulot_olib_tashlash(self, mahsulot):
        self.mahsulotlar.remove(mahsulot)

    def buyurtma_narxini_hisoblash(self):
        jami_narx = 0
        for mahsulot in self.mahsulotlar:
            jami_narx += mahsulot.narxi
        return jami_narx
class Jadvallar:
    pass
class Xodimlar:
    pass






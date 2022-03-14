# 1. soru cevabı
# Verilen değerlerin veri yapılarını inceleyiniz.
# Type() metodunu kullanınız.

x=8
y=3.2
z=8j+18
a="Hello World"
b=True
c=23<22
l=[1,2,3,4]
d={"Name":"Jake",
   "Age":27,
   "Adress":"Downtown"}
t=("Machine Learning","Data Science")
s={"Python","Machine Learning","Data Science"}
type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(l)
type(d)
type(t)
type(s)

# 2. soru cevabı
# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
# String metodlarını kullanınız.


text = "The goal is to turn data into information, and information info into insight."
text=text.upper()
text.replace(",","")
text.replace(".","")
print(text.split(" "))

# 3. soru cevabı
# Verilen listeye aşağıdaki adımları uygulayınız.
# Adım1: Verilen listenin eleman sayısına bakınız.
# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım4: Sekizinci indeksteki elemanı siliniz.
# Adım5: Yeni bir elemanek leyiniz.
# Adım6: Sekizinci indekse"N" elemanını tekrar ekleyiniz.


len(lst)
lst[0]
lst[10]
lst[0:4]
lst.pop(8)
lst.append("EfeGami")
lst.insert(8,"N")

# 4. soru cevabı
# Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
# Adım1: Key değerlerine erişiniz.
# Adım2: Value'lara erişiniz.
# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Adım4: Key değeri Ahmet value değeri[Turkey,24] olanyeni bir değer ekleyiniz.
# Adım5: Antonio'yudictionary'den siliniz.

dict = {'Chirstian':["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}
dict.keys()
dict.values()
dict['Daisy'][1]=13
dict['Ahmet']=["Turkey",24]
dict['Antonio'].pop()

# 5. soru cevabı
# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift
# sayıları ayrı listelere atayan ve bu listeleri return
# eden fonksiyon yazınız.
# Liste elemanlarına tek tek erişmeniz gerekmektedir.
# Her bir elemanın çift veya tek olma durumunu kontrol etmekiçin  % yapısını kullanabilirsiniz.

l=[2,13,18,93,22]
double = []
single = []

def ayırma(l):
    for i in l:
        if i % 2 == 0:
            double.append(i)
        else:
            single.append(i)
    print(double + single)
    return

ayırma(l)

# 6. soru cevabı
# ListComprehension yapısı kullanarak car_crashes verisindeki numeric
# değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# Beklenençıktı: Numeric olmayan değişkenlerin de isimleri büyümeli.
# Tek bir list comprehension yapısı kullanılmalı.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns =[col.upper() for col in df.columns ]

["NUM_"+ col  if df[col].dtype != "O" else col for col in df.columns]

# 7. soru cevabı
# List Comprehension yapısı kullanarak car_crashes verisinde
# isminde"no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.
# Tüm değişkenlerin isimleri büyük harf olmalı.
# Tek bir list comprehension yapısı ile yapılmalı.


df = sns.load_dataset("car_crashes")
df.columns =[col.upper() for col in df.columns ]

[col+"_FLAG"  if "NO" not in col else col for col in df.columns ]

# 8. soru cevabı
# List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden
# FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir data frame oluşturunuz.
# Önce verilen listeye göre list comprehension kullanarak "new_cols" adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz.

df = sns.load_dataset("car_crashes")
df.columns
og_list = ["abbrev","no_previous"]

new_cols = [col  for col in df.columns if col not in og_list]
soz={}
agg_list=["mean","min","max","sum"]

for col in new_cols:
    soz[col]=agg_list

df[new_cols].head()
 #8.soru 2. yol
new_soz={col: agg_list for col in new_cols}
new_df=df[new_cols].head()
new_df



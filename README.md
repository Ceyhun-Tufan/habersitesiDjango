**Yapay zeka entegrasyonlu haber sitesi backend projesi**


Sistem gereksinimleri:
- Python 3.12+

Kurulum ve Çalıştırma:
 ```shell
> python3 -m venv venv
> source venv/bin/activate
(venv)> pip3 install -r path/to/req.txt
(venv)> cd habersitesi
(venv)> python3 manage.py makemigrations
(venv)> python3 manage.py migrate
(venv)> python3 manage.py runserver
(venv)> celery -A habersitesi worker --loglevel=info 
```
> Windows kullanıyorsanız python3 ve pip3 yerine python ve pip kullanmanız yeterli.


# POST ```api/haber-ekle```

```json
{
    "title": "yeni bir haber",
    "subtitle": "django",
    "author": 1,
    "content": "guzel haberler",
    "tags": [], // Burada ufak bir hata var, düzelene kadar boş kullanın
    "image": null,
    "is_featured": false
}
```
# GET ```api/haberler/```
- Paging vardır, yani ```api/haberler/?page=2``` ile 2. sayfaya geçiş yapabilirsiniz. Her sayfa 10 adet haber içerir. Bu haber dataları **detaylı değildir**.

```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "izninizle python sertifikamı çıkarabilir miyim",
            "subtitle": "django",
            "slug": "neset-ertasla-hasbihal-1736710023",
            "author": "jeihun",
            "category": {
                "id": 1,
                "name": "guncel",
                "slug": "guncel"
            },
            "created_at": "2025-01-12T19:27:03.335360Z",
            "tags": [],
            "image": null,
            "view_count": 0,
            "is_featured": false
        }
    ]
}
```

# GET ```api/haberler/<slug>```
- Bir haberin **detaylı** bilgisini verir.

```json
{
    "id": 1,
    "title": "IETT aracında eşya",
    "subtitle": "iett aracında unutulan eşya",
    "slug": "neset-ertasla-hasbihal-1736710023",
    "content": "Istanbul'da İETT'ye bağlı toplu ulaşım araçlarında unutulan eşyalar, açık artırmayla satıldı. Aralarında ütü, drone, cep telefonu, pos makinesi gibi ürünlerin yer aldığı 3 bin 921 parça eşya, 705 bin liraya alıcı buldu.",
    "author": "jeihun",
    "created_at": "2025-01-12T19:27:03.335360Z",
    "updated_at": "2025-01-12T19:27:03.681383Z",
    "category": { // yapay zeka ile oluşturuldu
        "id": 1,
        "name": "guncel",
        "slug": "guncel"
    },
    "tags": [],
    "image": null,
    "view_count": 0,
    "is_featured": false,
    "source": "https://www.ntv.com.tr/galeri/turkiye/iett-araclarinda-unutulan-esyalar-acik-artirmayla-satildi-3-bin-921-esya-705-bin-liraya-alici-buldu,QQhwbgx4ekiPQKd747UE1w"
}
```



# GET ```api/kategoriler/```
- Tüm kategorileri listeler

```json
[
    {
        "id": 1,
        "name": "Sohbet",
        "slug": "sohbet"
    }
]

```

# GET ```api/kategoriler/<slug>```
- Slug'ı verilmiş kategorideki tüm haberleri döndürür. (Paging eklenecek buraya da)

```json
[
    {
        "id": 1,
        "title": "Deneme",
        "subtitle": "Mukemmel",
        "slug": "qwe",
        "author": "jeihun",
        "published_date": "2024-12-15T12:30:33Z",
        "category": {
            "id": 1,
            "name": "Sohbet",
            "slug": "sohbet"
        },
        "tags": [
            {
                "id": 1,
                "name": "muhabbet",
                "slug": "mahabut"
            }
        ],
        "image": null,
        "view_count": 0,
        "is_featured": false
    }
]
```


# Sonradan kaldırılacak endpointler
- **GET** ```api/haberler-all/```
  
  > Tüm haberleri döndürür











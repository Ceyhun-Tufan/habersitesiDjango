# habersitesiDjango

# GET ```api/haberler/```
- Paging vardır, yani ```api/haberler/?page=2``` ile 2. sayfaya geçiş yapabilirsiniz. Her sayfa 10 adet haber içerir. Bu haber dataları **detaylı** değildir.

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Deneme",
            "subtitle": "Mukemmel",
            "slug": "denemeslug",
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
                    "slug": "muhabbet"
                }
            ],
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
    "title": "Deneme",
    "subtitle": "Mukemmel",
    "slug": "qwe",
    "content": "Uzun bir content",
    "author": "jeihun",
    "published_date": "2024-12-15T12:30:33Z",
    "created_at": "2024-12-15T12:31:01.743113Z",
    "updated_at": "2024-12-15T12:31:01.743136Z",
    "category": {
        "id": 1,
        "name": "Sohbet",
        "slug": "sohbet"
    },
    "tags": [
        {
            "id": 1,
            "name": "muhabbet",
            "slug": "muhabbet"
        }
    ],
    "image": null,
    "view_count": 0,
    "is_featured": false,
    "source": null
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











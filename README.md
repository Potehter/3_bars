# Ближайшие бары

Код вычисляет самый большой бар, самый маленький бар и ближайший бар

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
В аргументы запуска надо передать путь до файла, затем широту и долготу

Запуск на Linux:

```bash

$ python bars.py bars.json 37.61 55.62 # possibly requires call of python3 executive instead of just python
# пример ответа скрипта
The biggest bar is:
{
    "geometry": {
        "coordinates": [
            37.638228501070095,
            55.70111462948684
        ],
        "type": "Point"
    },
    "properties": {
        "ReleaseNumber": 2,
        "Attributes": {
            "Address": "Автозаводская улица, дом 23, строение 1",
            "OperatingCompany": null,
            "SocialPrivileges": "нет",
            "global_id": 169375059,
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 795-15-84"
                }
            ],
            "District": "Даниловский район",
            "AdmArea": "Южный административный округ",
            "IsNetObject": "нет",
            "Name": "Спорт бар «Красная машина»",
            "SeatsCount": 450
        },
        "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8",
        "DatasetId": 1796,
        "VersionNumber": 2
    },
    "type": "Feature"
}
The smallest bar is:
{
    "geometry": {
        "coordinates": [
            37.35805920566864,
            55.84614475898795
        ],
        "type": "Point"
    },
    "properties": {
        "ReleaseNumber": 2,
        "Attributes": {
            "Address": "Дубравная улица, дом 34/29",
            "OperatingCompany": null,
            "SocialPrivileges": "нет",
            "global_id": 20675518,
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 258-94-19"
                }
            ],
            "District": "район Митино",
            "AdmArea": "Северо-Западный административный округ",
            "IsNetObject": "нет",
            "Name": "БАР. СОКИ",
            "SeatsCount": 0
        },
        "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53",
        "DatasetId": 1796,
        "VersionNumber": 2
    },
    "type": "Feature"
}
The closest bar is:
{
    "geometry": {
        "coordinates": [
            37.603133945101874,
            55.62323523333079
        ],
        "type": "Point"
    },
    "properties": {
        "ReleaseNumber": 2,
        "Attributes": {
            "Address": "Днепропетровская улица, дом 2",
            "OperatingCompany": "Космик",
            "SocialPrivileges": "нет",
            "global_id": 20731603,
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 223-43-83"
                }
            ],
            "District": "район Чертаново Северное",
            "AdmArea": "Южный административный округ",
            "IsNetObject": "да",
            "Name": "Спорт-бар «КОСМИК»",
            "SeatsCount": 150
        },
        "RowId": "e6104887-6c03-4427-b052-9a0d4facba8a",
        "DatasetId": 1796,
        "VersionNumber": 2
    },
    "type": "Feature"
}


```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

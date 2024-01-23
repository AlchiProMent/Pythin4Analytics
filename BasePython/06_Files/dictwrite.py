# запись справочника в дисковый файл
import json

file_name = 'direct.txt'

# справочник групп VK
res_dict = {
"response": {
"count": 5,
"items": [{
"description": "Программирование, 163 663 подписчика",
"type": "group",
"group": {
"id": 79831840,
"like": {
"is_liked": False,
"friends": {
"count": 0,
"preview": []
}
},
"name": "Программирование",
"screen_name": "bookflow",
"is_closed": 0,
"type": "page",
"is_admin": 0,
"is_member": 1,
"is_advertiser": 0,
"photo_50": "https://sun1-28.u...0,512,512&ava=1",
"photo_100": "https://sun1-28.u...0,512,512&ava=1",
"photo_200": "https://sun1-28.u...0,512,512&ava=1",
"track_code": "642b60b6KGSdFh108lODtAsxgZgf40pXFK2lgkgfqq6_UZsuSTt5tBbp"
}
}, {
"description": "Программирование, 261 381 подписчик",
"type": "group",
"group": {
"id": 16108331,
"like": {
"is_liked": False,
"friends": {
"count": 0,
"preview": []
}
},
"name": "Программирование ITmozg:",
"screen_name": "itmozg",
"is_closed": 0,
"type": "page",
"is_admin": 0,
"is_member": 1,
"is_advertiser": 0,
"photo_50": "https://sun1-15.u...0,200,200&ava=1",
"photo_100": "https://sun1-15.u...0,200,200&ava=1",
"photo_200": "https://sun1-15.u...0,200,200&ava=1",
"track_code": "200ed226K1tA0uqPgrbMwG9mcKPCd6L6A8_zgeRq3WFh5m3TpAV6i8st"
}
}, {
"description": "Программирование, 55 776 подписчиков",
"type": "group",
"group": {
"id": 66170841,
"like": {
"is_liked": False,
"friends": {
"count": 0,
"preview": []
}
},
"name": "For Web — фронтенд, дизайн, программирование",
"screen_name": "forwebdev",
"is_closed": 0,
"type": "page",
"is_admin": 0,
"is_member": 1,
"is_advertiser": 0,
"photo_50": "https://sun1-14.u...0,511,511&ava=1",
"photo_100": "https://sun1-14.u...0,511,511&ava=1",
"photo_200": "https://sun1-14.u...0,511,511&ava=1",
"track_code": "9b179a34-glzwDa-qax0Btp1mdhj9nlhVm_Sryt8qRd-YF4LOvSr2fg_"
}
}, {
"description": "Обучающие курсы, 2 подписчика",
"type": "group",
"group": {
"id": 206247301,
"like": {
"is_liked": False,
"friends": {
"count": 0,
"preview": []
}
},
"name": "Программирование для всех",
"screen_name": "club206247301",
"is_closed": 0,
"type": "page",
"is_admin": 1,
"admin_level": 3,
"is_member": 1,
"is_advertiser": 1,
"photo_50": "https://sun1-93.u...2,262,262&ava=1",
"photo_100": "https://sun1-93.u...2,262,262&ava=1",
"photo_200": "https://sun1-93.u...2,262,262&ava=1",
"track_code": "952862d7Qca6jV6nypB1D9nyoafRp7bvHwL_OWG6dAOBtLIaaaADDz9ljA"
}
}, {
"description": "23 года, Москва",
"type": "profile",
"profile": {
"id": 583983550,
"first_name": "Программирование-Информатика",
"last_name": "Статистика",
"can_access_closed": True,
"is_closed": False,
"track_code": "70a0f6e3H-heD49E1aR0I1fJQ7zzTam-UUWj46QlvQji0r6UFit-iGdYhhro8i4jakqeBGZ6paBVVrrlvnrcZI4"
}
}]
}
}

try:
    with open(file_name, 'w') as dictxt:
        json.dump(res_dict, dictxt)
except:
    print(f'Ошибка записи в файл {file_name}!')
else:
    print('Словарь успешно сохранен.')


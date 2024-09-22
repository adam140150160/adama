from flet import *

def main(page:Page):
    page.title = "test"
    page.scroll='auto'
    page.window.height = 740
    page.window.width = 390
    page.bgcolor = "#26355D"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    

    def change_route(route):
        page.views.clear()
        if page.route == "/apple_phone":
            page.views.append(apple_phone())
        elif page.route == "/samsung_phone":
            page.views.append(samsung_phone())
        elif page.route == "/tecno_phone":
            page.views.append(tecno_phone())
        elif page.route == "/infinx_phone":
            page.views.append(infinx_phone())
        elif page.route == "/Realme_phone":
            page.views.append(Realme_phone())
        elif page.route == "/Xiaomi_phone":
            page.views.append(Xiaomi_phone())
        elif page.route == "/Honer_phone":
            page.views.append(Honer_phone())        
        elif page.route == "/":
            page.views.append(home())

        page.update()


    home_appbar = AppBar(title=Text("Store Phone"),color="black",bgcolor=colors.WHITE,center_title=True)
    sam_appbar = AppBar(title=Text("SAMSUNG Phone Price"),color="black",bgcolor='#0079FF',center_title=True)
    app_appbar = AppBar(title=Text("APPLE Phone Price"),color="white",bgcolor=colors.BLACK87,center_title=True)
    tecn_appbar = AppBar(title=Text("TECNO Phone Price"),color="black",bgcolor='#D2E0FB',center_title=True)
    infi_appbar = AppBar(title=Text("INFINX Phone Price"),color="black",bgcolor='#6EC207',center_title=True)
    Realme_appbar = AppBar(title=Text("REALME Phone Price"),color="black",bgcolor='#FFEB00',center_title=True)
    Xiaomi_appbar = AppBar(title=Text("Xiaomi Phone Price"),color="black",bgcolor='#F94C10',center_title=True)
    Honer_appbar = AppBar(title=Text("Honer Phone Price"),color="black",bgcolor='#B5C0D0',center_title=True)

    samsung = ElevatedButton("SAMSUNG",width=120,height=50,color="white",bgcolor="#0079FF",on_click=lambda _:page.go("/samsung_phone"))
    tecno = ElevatedButton("TECNO",width=120,height=50,color="#4379F2",bgcolor="#D2E0FB",on_click=lambda _:page.go("/tecno_phone"))
    infinx = ElevatedButton("INFINX",width=120,height=50,color="white",bgcolor="#6EC207",on_click=lambda _:page.go("/infinx_phone"))
    apple = ElevatedButton("APPLE",width=120,height=50,color="white",bgcolor="black",on_click=lambda _:page.go("/apple_phone"))
    Realme = ElevatedButton("Realme",width=120,height=50,color="black",bgcolor="#FFEB00",on_click=lambda _:page.go("/Realme_phone"))
    Xiaomi = ElevatedButton("Xiaomi",width=120,height=50,color="white",bgcolor="#F94C10",on_click=lambda _:page.go("/Xiaomi_phone"))
    Honer = ElevatedButton("Honer",width=120,height=50,color="white",bgcolor="#B5C0D0",on_click=lambda _:page.go("/Honer_phone"))
    
    def home():
        return View(
            "/",
            appbar=home_appbar,
            controls=[
                Container(height=600,
                          width=380,
                          bgcolor="whati",
                          margin=margin.only(top=20),
                          border_radius=15,
                          alignment=alignment.center,
                          content=Column(
                              controls=[Text(""),
                                        samsung,
                                        tecno,
                                        infinx,
                                        apple,
                                        Realme,
                                        Xiaomi,
                                        Honer
                                        
                                  
                              ],spacing=30
                          ))
                
                ]
        )
    def apple_phone():
        return View(
            "/apple_phone",
            appbar=app_appbar,
            controls=[
                Row(
                    controls=[
                        Text("15 Pro max 256 / master / 1700",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("pad 9 / 64 / 330",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("...",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        
                        
                Row(
                    controls=[
                        ElevatedButton("Go Back",bgcolor="white",color="black",width=120,height=50,on_click=lambda _:page.go("/"))
                        ],alignment=MainAxisAlignment.CENTER)
            ]

        )

    def samsung_phone():
        return View(
            "/samsung_phone",
            appbar=sam_appbar,
            scroll='auto',
            controls=[
                Row(
                    controls=[
                        Text("S24 ultra /256/ 1300",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        Text("A55/256/485",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("A35/256/410",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("A35/128/380",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("A25/256-8/310",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("A25/128-6/258",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("A06/128-8/180",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("A06/128-4/165",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("A15/256/215",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("A15/128-6/187",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("A15/128-4/158",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("A05/128-6/150",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("A05/128-4/130",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("A05/64-4/115)",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("A05s/128-6/180",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("A05s/128-4/165",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("A05s/64-4/120",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),

                        

                Row(
                    controls=[
                        ElevatedButton("Go Back",bgcolor="white",color="black",width=120,height=50,on_click=lambda _:page.go("/"))
                        ],alignment=MainAxisAlignment.CENTER)
            ]

        )

    def tecno_phone():
        return View(
            "/tecno_phone",
            appbar=tecn_appbar,
            controls=[
                Row(
                    controls=[
                        Text("Camon 30 Premier 5G/512-12/550",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        Text("Camon 30 pro 5G/256-12/425",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("Camon 30 4G/256-8/225",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("Pova 6 pro/256-12/280",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Pova 6 /256-8/250",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text('Spark 20 pro +/256-8/215',size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Spark 20 pro/256-12/220",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Spark 20 pro/256-8/200",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("Spark 20 /256-8/155",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("Spark 20c /256-8/135",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Spark 20c /128-8/125",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Spark go 2024 /128-4/115",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Spark go 2024 /64-4/97",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        
                Row(
                    controls=[
                        ElevatedButton("Go Back",bgcolor="white",color="black",width=120,height=50,on_click=lambda _:page.go("/"))
                        ],alignment=MainAxisAlignment.CENTER)
            ]
        
        )
    def infinx_phone():
        return View(
            "/infinx_phone",
            appbar=infi_appbar,
            scroll='auto',
            controls=[
                Row(
                    controls=[
                        Text("Zero 40 5G /512-12/500",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        Text("Zero 40 4G/512-12/325",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("GT 20 pro /256-12/425",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Zero 30 5G/256-12/375",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Zero 30 4G/256-12/285",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("Note 40 pro +/256-12/400",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("Note 40 pro/256-12/300",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("Note 40 pro /256-8/285",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Note 40 /256-8/245",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("HOT 50 /256-8/163",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("HOT 50i /256-4/140",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("HOT 40 pro /256-12/210",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("HOT 40 pro /256-8/190",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("HOT 40 /256-8/179",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("HOT 40i /256-8/155",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("HOT 40i /128-8/145",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("HOT 40i /128-4/125",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Smart 9 /64-3/100",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                          Row(
                    controls=[
                        Text("Smart 8 pro /256/125",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Smart 8 + /64-4/100",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Smart 8 /64/95",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        ElevatedButton("Go Back",bgcolor="white",color="black",width=120,height=50,on_click=lambda _:page.go("/"))
                        ],alignment=MainAxisAlignment.CENTER)
            ]

        )
    def Realme_phone():
        return View(
            "/Realme_phone",
            appbar=Realme_appbar,
            scroll='auto',
            controls=[
                Row(
                    controls=[
                        Text("Realme GT 6 /512/785",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        Text("Realme GT 6/256/705",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("Realme GT 6T/512/615",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Realme 12 pro+/512/565",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                          Row(
                    controls=[
                        Text("Realme 12 pro/512/480",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("Realme 12 pro/256/415",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text("Realme 12 +/512/440",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Realme 12 +/256/380",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Realme 12 /512/315",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Realme 12/256/285",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Realme C67/256/215",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Realme C65/256/200",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Realme C65/128/165",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Realme C63/256-8/210",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Realme C63/128-6/170",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Realme C61/256-8/195",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                          Row(
                    controls=[
                        Text("Realme C61/128-6/160",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                          Row(
                    controls=[
                        Text("Realme C53/256-8/195",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                          Row(
                    controls=[
                        Text("Realme C51/128-4/135",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                          Row(
                    controls=[
                        Text("Realme Note 50 /128-4/115",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                          Row(
                    controls=[
                        Text("Realme Note 50 /64-3/100",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        ElevatedButton("Go Back",bgcolor="white",color="black",width=120,height=50,on_click=lambda _:page.go("/"))
                        ],alignment=MainAxisAlignment.CENTER)
            ]

        )
    
    def Xiaomi_phone():
        return View(
            "/Xiaomi_phone",
            appbar=Xiaomi_appbar,
            scroll='auto',
            controls=[
                Row(
                    controls=[
                        Text("Mi 14 Ultra /512-12/1400",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        Text("Note 13 pro+/512-12/490",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Note 13 pro 5G/512-12/425",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                          Row(
                    controls=[
                        Text("Note 13 pro 4G/512-12/325",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                          Row(
                    controls=[
                        Text("Note 13 5G/256-8/275",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Note 13 /512-12/235",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        Row(
                    controls=[
                        Text('Note 13 /256-8/205',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('Redmi 14C/256-8/165',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('Redmi 14C/128-4/135',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('Redmi 13/256-8/195',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('Redmi A3/128-4/110',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('xiaomi pad 6/256-8/410',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                    Row(
                    controls=[
                        Text('xiaomi pad se/256-8/230',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('xiaomi pad 8 pro/256-8/360',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('xiaomi pad 6 pro/256-8/720',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('Poco F6 pro/512/685',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('Poco F6 /512/505',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('Poco X6 pro /512/445',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                     Row(
                    controls=[
                        Text('Poco M6 pro /512/300',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                      Row(
                    controls=[
                        Text('Poco M6 /256/200',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                      Row(
                    controls=[
                        Text('Poco C65/256/300',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                      Row(
                    controls=[
                        Text('Poco Pad /256-8/330',size=20,color='black')
                    ],alignment=MainAxisAlignment.CENTER),
                    
                    
                    
                    
            
                                                
                Row(
                    controls=[
                        ElevatedButton("Go Back",bgcolor="white",color="black",width=120,height=50,on_click=lambda _:page.go("/"))
                        ],alignment=MainAxisAlignment.CENTER)
            ]

        )
    def Honer_phone():
        return View(
            "/Honer_phone",
            appbar=Honer_appbar,
            scroll='auto',
            controls=[
                Row(
                    controls=[
                        Text("Honer 200 pro/512-12/860",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        Text("Honer200 /512-12/625",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Honer200 /256-8/525",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Honer200 /512-12/625",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Honer200 Lite/256-8/290",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Honer X9b/256-12/350",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Honer X9b/256-8/325",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Honer X8b/512-8/275",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Honer X8b/256-8/235",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Honer X7b/256-8/190",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Honer X6b/256-6/155",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                         Row(
                    controls=[
                        Text("Honer X6b/128-6/140",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                          Row(
                    controls=[
                        Text("Honer X6a/128-4/125",size=20,color="black")
                        ],alignment=MainAxisAlignment.CENTER),
                        
                Row(
                    controls=[
                        ElevatedButton("Go Back",bgcolor="white",color="black",width=120,height=50,on_click=lambda _:page.go("/"))
                        ],alignment=MainAxisAlignment.CENTER)
            ]

        )
    



    page.on_route_change = change_route
    page.go("/")

    page.update()

app(target=main,assets_dir='assets/')



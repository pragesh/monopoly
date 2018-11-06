"""TODO:Ensure board can't be modified by agents""" 

board = {
-1:{
"class":"Jail",
"name":"Jail",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
0:{
"class":"Idle",
"name":"Go",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
1:{
"class":"Street",
"name":"Mediterranean Avenue",
"monopoly":"Brown",
"monopoly_size":2,
"price":60,
"build_cost":50,
"rent":2,
"rent_house_1":10,
"rent_house_2":30,
"rent_house_3":90,
"rent_house_4":160,
"rent_hotel":250,
"tax":0,
"monopoly_group_elements":[3]
},
2:{
"class":"Chest",
"name":"Community Chest",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
3:{
"class":"Street",
"name":"Baltic Avenue",
"monopoly":"Brown",
"monopoly_size":2,
"price":60,
"build_cost":50,
"rent":4,
"rent_house_1":20,
"rent_house_2":60,
"rent_house_3":180,
"rent_house_4":320,
"rent_hotel":450,
"tax":0,
"monopoly_group_elements":[1]
},
4:{
"class":"Tax",
"name":"Income Tax",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":200
},
5:{
"class":"Railroad",
"name":"Reading Railroad",
"monopoly":"Railroad",
"monopoly_size":4,
"price":200,
"build_cost":0,
"rent":25,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0,
"monopoly_group_elements":[15, 25, 35]
},
6:{
"class":"Street",
"name":"Oriental Avenue",
"monopoly":"Light Blue",
"monopoly_size":3,
"price":100,
"build_cost":50,
"rent":6,
"rent_house_1":30,
"rent_house_2":90,
"rent_house_3":270,
"rent_house_4":400,
"rent_hotel":550,
"tax":0,
"monopoly_group_elements":[8, 9]
},
7:{
"class":"Chance",
"name":"Chance",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
8:{
"class":"Street",
"name":"Vermont Avenue",
"monopoly":"Light Blue",
"monopoly_size":3,
"price":100,
"build_cost":50,
"rent":6,
"rent_house_1":30,
"rent_house_2":90,
"rent_house_3":270,
"rent_house_4":400,
"rent_hotel":550,
"tax":0,
"monopoly_group_elements":[6, 9]
},
9:{
"class":"Street",
"name":"Connecticut Avenue",
"monopoly":"Light Blue",
"monopoly_size":3,
"price":120,
"build_cost":50,
"rent":8,
"rent_house_1":40,
"rent_house_2":100,
"rent_house_3":300,
"rent_house_4":450,
"rent_hotel":600,
"tax":0,
"monopoly_group_elements":[6, 8]
},
10:{
"class":"Idle",
"name":"Jail",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
11:{
"class":"Street",
"name":"St. Charles Place",
"monopoly":"Pink",
"monopoly_size":3,
"price":140,
"build_cost":100,
"rent":10,
"rent_house_1":50,
"rent_house_2":150,
"rent_house_3":450,
"rent_house_4":625,
"rent_hotel":750,
"tax":0,
"monopoly_group_elements":[13, 14]
},
12:{
"class":"Utility",
"name":"Electric Company",
"monopoly":"Utility",
"monopoly_size":2,
"price":150,
"build_cost":0,
"rent":4,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0,
"monopoly_group_elements":[28]
},
13:{
"class":"Street",
"name":"States Avenue",
"monopoly":"Pink",
"monopoly_size":3,
"price":140,
"build_cost":100,
"rent":10,
"rent_house_1":50,
"rent_house_2":150,
"rent_house_3":450,
"rent_house_4":625,
"rent_hotel":750,
"tax":0,
"monopoly_group_elements":[11, 14]
},
14:{
"class":"Street",
"name":"Virginia Avenue",
"monopoly":"Pink",
"monopoly_size":3,
"price":160,
"build_cost":100,
"rent":12,
"rent_house_1":60,
"rent_house_2":180,
"rent_house_3":500,
"rent_house_4":700,
"rent_hotel":900,
"tax":0,
"monopoly_group_elements":[11, 13]
},
15:{
"class":"Railroad",
"name":"Pennsylvania Railroad",
"monopoly":"Railroad",
"monopoly_size":4,
"price":200,
"build_cost":0,
"rent":25,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0,
"monopoly_group_elements":[5, 25, 35]
},
16:{
"class":"Street",
"name":"St. James Place",
"monopoly":"Orange",
"monopoly_size":3,
"price":180,
"build_cost":100,
"rent":14,
"rent_house_1":70,
"rent_house_2":200,
"rent_house_3":550,
"rent_house_4":750,
"rent_hotel":950,
"tax":0,
"monopoly_group_elements":[18, 19]
},
17:{
"class":"Chest",
"name":"Community Chest",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
18:{
"class":"Street",
"name":"Tennessee Avenue",
"monopoly":"Orange",
"monopoly_size":3,
"price":180,
"build_cost":100,
"rent":14,
"rent_house_1":70,
"rent_house_2":200,
"rent_house_3":550,
"rent_house_4":750,
"rent_hotel":950,
"tax":0,
"monopoly_group_elements":[16, 19]
},
19:{
"class":"Street",
"name":"New York Avenue",
"monopoly":"Orange",
"monopoly_size":3,
"price":200,
"build_cost":100,
"rent":16,
"rent_house_1":80,
"rent_house_2":220,
"rent_house_3":600,
"rent_house_4":800,
"rent_hotel":1000,
"tax":0,
"monopoly_group_elements":[16, 18]
},
20:{
"class":"Idle",
"name":"Free Parking",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
21:{
"class":"Street",
"name":"Kentucky Avenue",
"monopoly":"Red",
"monopoly_size":3,
"price":220,
"build_cost":150,
"rent":18,
"rent_house_1":90,
"rent_house_2":250,
"rent_house_3":700,
"rent_house_4":875,
"rent_hotel":1050,
"tax":0,
"monopoly_group_elements":[23, 24]
},
22:{
"class":"Chance",
"name":"Chance",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
23:{
"class":"Street",
"name":"Indiana Avenue",
"monopoly":"Red",
"monopoly_size":3,
"price":220,
"build_cost":150,
"rent":18,
"rent_house_1":90,
"rent_house_2":250,
"rent_house_3":700,
"rent_house_4":875,
"rent_hotel":1050,
"tax":0,
"monopoly_group_elements":[21, 24]
},
24:{
"class":"Street",
"name":"Illinois Avenue",
"monopoly":"Red",
"monopoly_size":3,
"price":240,
"build_cost":150,
"rent":20,
"rent_house_1":100,
"rent_house_2":300,
"rent_house_3":750,
"rent_house_4":925,
"rent_hotel":1100,
"tax":0,
"monopoly_group_elements":[21, 23]
},
25:{
"class":"Railroad",
"name":"B. & O. Railroad",
"monopoly":"Railroad",
"monopoly_size":4,
"price":200,
"build_cost":0,
"rent":25,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0,
"monopoly_group_elements":[5, 15, 35]
},
26:{
"class":"Street",
"name":"Atlantic Avenue",
"monopoly":"Yellow",
"monopoly_size":3,
"price":260,
"build_cost":150,
"rent":22,
"rent_house_1":110,
"rent_house_2":330,
"rent_house_3":800,
"rent_house_4":975,
"rent_hotel":1150,
"tax":0,
"monopoly_group_elements":[27, 29]
},
27:{
"class":"Street",
"name":"Ventnor Avenue",
"monopoly":"Yellow",
"monopoly_size":3,
"price":260,
"build_cost":150,
"rent":22,
"rent_house_1":110,
"rent_house_2":330,
"rent_house_3":800,
"rent_house_4":975,
"rent_hotel":1150,
"tax":0,
"monopoly_group_elements":[26, 29]
},
28:{
"class":"Utility",
"name":"Water Works",
"monopoly":"Utility",
"monopoly_size":2,
"price":150,
"build_cost":0,
"rent":4,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0,
"monopoly_group_elements":[12]
},
29:{
"class":"Street",
"name":"Marvin Gardens",
"monopoly":"Yellow",
"monopoly_size":3,
"price":280,
"build_cost":150,
"rent":24,
"rent_house_1":120,
"rent_house_2":360,
"rent_house_3":850,
"rent_house_4":1025,
"rent_hotel":1200,
"tax":0,
"monopoly_group_elements":[26, 27]
},
30:{
"class":"GoToJail",
"name":"Go To Jail",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
31:{
"class":"Street",
"name":"Pacific Avenue",
"monopoly":"Green",
"monopoly_size":3,
"price":300,
"build_cost":200,
"rent":26,
"rent_house_1":130,
"rent_house_2":390,
"rent_house_3":900,
"rent_house_4":1100,
"rent_hotel":1275,
"tax":0,
"monopoly_group_elements":[32, 34]
},
32:{
"class":"Street",
"name":"North Carolina Avenue",
"monopoly":"Green",
"monopoly_size":3,
"price":300,
"build_cost":200,
"rent":26,
"rent_house_1":130,
"rent_house_2":390,
"rent_house_3":900,
"rent_house_4":1100,
"rent_hotel":1275,
"tax":0,
"monopoly_group_elements":[31, 34]
},
33:{
"class":"Chest",
"name":"Community Chest",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
34:{
"class":"Street",
"name":"Pennsylvania Avenue",
"monopoly":"Green",
"monopoly_size":3,
"price":320,
"build_cost":200,
"rent":28,
"rent_house_1":150,
"rent_house_2":450,
"rent_house_3":1000,
"rent_house_4":1200,
"rent_hotel":1400,
"tax":0,
"monopoly_group_elements":[31, 32]
},
35:{
"class":"Railroad",
"name":"Short Line",
"monopoly":"Railroad",
"monopoly_size":4,
"price":200,
"build_cost":0,
"rent":25,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0,
"monopoly_group_elements":[5, 15, 25]
},
36:{
"class":"Chance",
"name":"Chance",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":0
},
37:{
"class":"Street",
"name":"Park Place",
"monopoly":"Dark Blue",
"monopoly_size":2,
"price":350,
"build_cost":200,
"rent":35,
"rent_house_1":175,
"rent_house_2":500,
"rent_house_3":1100,
"rent_house_4":1300,
"rent_hotel":1500,
"tax":0,
"monopoly_group_elements":[39]
},
38:{
"class":"Tax",
"name":"Luxury Tax",
"monopoly":"None",
"monopoly_size":0,
"price":0,
"build_cost":0,
"rent":0,
"rent_house_1":0,
"rent_house_2":0,
"rent_house_3":0,
"rent_house_4":0,
"rent_hotel":0,
"tax":100
},
39:{
"class":"Street",
"name":"Boardwalk",
"monopoly":"Dark Blue",
"monopoly_size":2,
"price":400,
"build_cost":200,
"rent":50,
"rent_house_1":200,
"rent_house_2":600,
"rent_house_3":1400,
"rent_house_4":1700,
"rent_hotel":2000,
"tax":0,
"monopoly_group_elements":[37]
}
}


property_to_space_map = {
2:0,
4:1,
6:2,
7:3,
9:4,
10:5,
12:6,
13:7,
14:8,
15:9,
16:10,
17:11,
19:12,
20:13,
22:14,
24:15,
25:16,
26:17,
27:18,
28:19,
29:20,
30:21,
32:22,
33:23,
35:24,
36:25,
38:26,
40:27
}

print(0 in property_to_space_map)
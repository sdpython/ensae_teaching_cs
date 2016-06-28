data = 
[
{'velo': 12817.0, 'last_update': '10/9/13 11:35', 'minute': 35.0, 'heure': 11.0, 'place': 25202.0, 'name': '10/9/13 11:35', 'roulant': 225.0, 'somme': 38019.0}
,{'velo': 12744.0, 'last_update': '10/9/13 11:40', 'minute': 40.0, 'heure': 11.0, 'place': 25273.0, 'name': '10/9/13 11:40', 'roulant': 227.0, 'somme': 38017.0}
,{'velo': 12674.0, 'last_update': '10/9/13 11:45', 'minute': 45.0, 'heure': 11.0, 'place': 25349.0, 'name': '10/9/13 11:45', 'roulant': 221.0, 'somme': 38023.0}
,{'velo': 12646.0, 'last_update': '10/9/13 11:50', 'minute': 50.0, 'heure': 11.0, 'place': 25380.0, 'name': '10/9/13 11:50', 'roulant': 218.0, 'somme': 38026.0}
,{'velo': 12568.0, 'last_update': '10/9/13 11:55', 'minute': 55.0, 'heure': 11.0, 'place': 25457.0, 'name': '10/9/13 11:55', 'roulant': 219.0, 'somme': 38025.0}
// ... 
]
;

var parseDate = d3.time.format("%d/%m/%Y %H:%M").parse;

for (var i = 0; i < data.length; i++) {
    element = data[i] ;
    element['last_update'] = parseDate(element['last_update']) ;
}


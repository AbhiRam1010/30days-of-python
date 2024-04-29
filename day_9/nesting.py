# travel_log= {
#     "france": {"city_visited": ["paris", "lille", "dijon"],"total_visits": 12},
#     "Germany":{"city_visited": ["berlin", "humberg","stuttgart"], 'total_visit': 13}
# }
travel_logg= [
    {
        "country":  "france", 
        "city_visited": ["paris", "lille", "dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "city_visited": ["berlin", "humberg","stuttgart"],
        'total_visit': 5
    },
  ]
def add_new_country(country_visited,city,total_time):
    new_country={}
    new_country["country"]=country_visited
    new_country["city_visited"]=city
    new_country["total_visits"]=total_time
    travel_logg.append(new_country)
    print(travel_logg)




add_new_country("Russia",["Moscow","saint peterberg"],2,)
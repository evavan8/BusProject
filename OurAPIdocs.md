# Why is my bus late? 
## API documentation for 
https://api.um.warszawa.pl/api/action/

Website: https://api.um.warszawa.pl/#

-------------------------------------

### busestrams_get
##### Online location of public transport, updated every 10 seconds

#### Required parameters
  - resource_id=f2e5503e-927d-4ad3-9500-4ab9e55deb59
  - apikey=
  - type=1    (2 for tram locations, which we won't need)
#### Optional parameters
- line=
- brigade=

 #### Available data
- Lat - latitude coordinate in the WGS84 system (EPSG: 4326)
- Lon - longitude coordinate in the WGS84 system (EPSG: 4326)
- Time - time of sending the GPS signal
- Lines - number of a bus or tram line
- Brigade - the brigade number of the vehicle


#### Sample output

~~~
{
	   "result": [
        {
            "Brigade": "1",
            "Lat": 52.1798648,
            "Lines": "213",
            "Lon": 21.232337,
            "Time": "2020-09-18 22:53:42",
            "VehicleNumber": "1001"
        },
        {
            "Brigade": "3",
            "Lat": 52.2120383,
            "Lines": "213",
            "Lon": 21.1047441,
            "Time": "2020-09-18 22:53:52",
            "VehicleNumber": "1004"
        },
        ...
        {
            "Brigade": "3",
            "Lat": 52.249916,
            "Lines": "719",
            "Lon": 20.841076,
            "Time": "2020-09-18 22:53:47",
            "VehicleNumber": "9954"
        }
    ]
}
~~~

-------------------------------------


### dbtimetable_get

##### Gives access to public transport timetables

  - set of stops: 
	 id=b27f4c17-5c50-4a5b-89dd-236b282bc499
      - name=
      - apikey=

  - lines available at the stop: 
	 id=88cd555f-6f31-43ca-9de4-66c479ad5942
      - busstopId=
      - busstopNr=
      - apikey=

  - timetable for the line:
	 id=e923fa0e-d96c-43f9-ae6e-60518c9f3238
      - busstopId=
      - busstopNr=
      - line=
      - apikey=

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNzYyNzU1NjVdfQ==
-->
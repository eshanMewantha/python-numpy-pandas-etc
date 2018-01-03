# anaconda installation will by default install flask

Run rest_api.py

GET
send a http GET request to : http://localhost:5000/eshan/api/v1.0/superheroes

GET with parameters passed in request url
send a http GET request to : http://localhost:5000/eshan/api/v1.0/superheroes/powers?name=superman

POST with values passed in body
send a http POST request to : http://localhost:5000/eshan/api/v1.0/superheroes/add
with the POST body having
{
	"name" : "batman",
	"details" : {
		"from": "Earth",
        "description": "Dark Knight",
        "powers": ["intellect", "martial arts", "money"]
	}
}
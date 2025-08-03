# smart-home-api-testing
# Smart Home API (Live)

Live Swagger: [https://smart-home-api-testing.onrender.com/docs](https://smart-home-api-testing.onrender.com/docs)

A sample CRUD API for managing smart devices (like Resideo/Phoenix apps).

 Built With using : FastAPI (Python) using pycharm,  Render (deployed 24x7), Tested with Swagger & Postman

Below are the end API Endpoints

- `GET /devices`
- `GET /devices/{id}`
- `POST /devices`
- `PUT /devices/{id}`
- `DELETE /devices/{id}`

Payload:
```json
{
  "id": 1,
  "name": "Smart Bulb",
  "type": "light",
  "status": "on"
}

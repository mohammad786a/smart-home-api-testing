from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

@app.get("/")
def read_root():
    return {"message": "Smart Home API is running"}

class Device(BaseModel):
    id: int
    name: str
    type: str
    status: str

devices = []

@app.post("/devices")
def add_device(device: Device):
    for d in devices:
        if d.id == device.id:
            raise HTTPException(status_code=400, detail="Device already exists")
    devices.append(device)
    return device

@app.get("/devices")
def get_devices():
    return devices

@app.get("/devices/{device_id}")
def get_device(device_id: int):
    for d in devices:
        if d.id == device_id:
            return d
    raise HTTPException(status_code=404, detail="Device not found")

@app.put("/devices/{device_id}")
def update_device(device_id: int, device: Device):
    for i, d in enumerate(devices):
        if d.id == device_id:
            devices[i] = device
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.delete("/devices/{device_id}")
def delete_device(device_id: int):
    for i, d in enumerate(devices):
        if d.id == device_id:
            devices.pop(i)
            return {"message": "Device deleted"}
    raise HTTPException(status_code=404, detail="Device not found")

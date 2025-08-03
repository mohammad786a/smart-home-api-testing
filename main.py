from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Dummy in-memory data store
devices = []

# Schema for device
class Device(BaseModel):
    id: int
    name: str
    type: str
    status: str  # on/off

@app.get("/")
def read_root():
    return {"message": "Smart Home API is running"}

@app.get("/devices", response_model=List[Device])
def get_devices():
    return devices

@app.post("/devices", response_model=Device)
def add_device(device: Device):
    for d in devices:
        if d.id == device.id:
            raise HTTPException(status_code=400, detail="Device ID already exists")
    devices.append(device)
    return device

@app.get("/devices/{device_id}", response_model=Device)
def get_device(device_id: int):
    for device in devices:
        if device.id == device_id:
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.put("/devices/{device_id}", response_model=Device)
def update_device(device_id: int, updated_device: Device):
    for i, device in enumerate(devices):
        if device.id == device_id:
            devices[i] = updated_device
            return updated_device
    raise HTTPException(status_code=404, detail="Device not found")

@app.delete("/devices/{device_id}")
def delete_device(device_id: int):
    for i, device in enumerate(devices):
        if device.id == device_id:
            del devices[i]
            return {"message": "Device deleted"}
    raise HTTPException(status_code=404, detail="Device not found")



from fastapi import HTTPException

@app.get("/devices/{device_id}")
def get_device_by_id(device_id: int):
    for device in devices:
        if device["id"] == device_id:
            return device
    raise HTTPException(status_code=404, detail="Device not found")


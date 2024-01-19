from fastapi import APIRouter, WebSocket, WebSocketDisconnect

ws = APIRouter()
@ws.websocket("/websocket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Connection established")

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"You wrote: {data}")
    except WebSocketDisconnect:
        await websocket.close()
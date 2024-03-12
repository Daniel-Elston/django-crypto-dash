import aiofiles
import json

async def load_from_json(filepath):
    async with aiofiles.open(filepath, 'r') as file:
        content = await file.read()
        return json.loads(content)

# to do: input logic
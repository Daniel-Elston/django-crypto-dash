from __future__ import annotations

import json
import os

import aiofiles


async def temp_file_reset(filepath):
    """Reset a temp file."""
    if os.path.exists(filepath):
        os.remove(filepath)


async def save_json(data, filepath):
    """Save data to a json file."""
    async with aiofiles.open(filepath, 'w') as file:
        await file.write(json.dumps(data))


async def load_json(filepath):
    """Load data from a json file."""
    if os.path.exists(filepath):
        async with aiofiles.open(filepath, 'r') as file:
            content = await file.read()
            return json.loads(content)
    return []


async def amend_json(data, filepath):
    """Amend a json file with new data."""
    async with aiofiles.open(filepath, 'r') as file:
        content = await file.read()
        existing_data = json.loads(content)
        existing_data.append(data)

    async with aiofiles.open(filepath, 'w') as file:
        await file.write(json.dumps(existing_data))

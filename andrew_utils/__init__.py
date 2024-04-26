import hashlib

def second_to_time(seconds):
    """Converts seconds (including floating-point numbers) to hh:mm:ss format.

    Args:
        seconds: The number of seconds to convert (can be a float).

    Returns:
        A string representing the time in hh:mm:ss format.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{remaining_seconds:09.6f}"

def get_md5sum(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()
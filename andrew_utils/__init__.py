import datetime
import hashlib
import decimal

def seconds_to_time(seconds,include_decimals=True):
    
    if include_decimals:
        milliseconds = round(seconds*1000)
        minutes_remaining,remaining_milliseconds = divmod(milliseconds,60000)
        hours,minutes = divmod(minutes_remaining, 60)
        remaining_seconds=f"{remaining_milliseconds:05d}"
        remaining_seconds=remaining_seconds[:-3]+'.'+remaining_seconds[-3:]
        return f"{hours:02d}:{minutes:02d}:{remaining_seconds}"
    else:
        seconds = round(seconds)
        minutes_remaining,remaining_seconds = divmod(seconds,60)
        hours,minutes = divmod(minutes_remaining, 60)
        return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"

def time_to_seconds(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)

def get_md5sum_file(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()
def timeStringToInt(time: str) -> int:
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)


def intToTimeString(time: int) -> str:
    hour = time // 60
    minute = time % 60
    return f"{hour:02d}:{minute:02d}"

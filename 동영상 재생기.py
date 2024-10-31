def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(":"))
    return minutes * 60 + seconds


def seconds_to_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"


def check_and_skip_opening(pos, opening_start, opening_end):
    if opening_start <= pos <= opening_end:
        return opening_end
    return pos


def solution(video_len, pos, op_start, op_end, commands):
    video_length = time_to_seconds(video_len)
    position = time_to_seconds(pos)
    opening_start = time_to_seconds(op_start)
    opening_end = time_to_seconds(op_end)

    # 초기 오프닝 체크
    position = check_and_skip_opening(position, opening_start, opening_end)

    for command in commands:
        if command == "prev":
            position = max(0, position - 10)
        elif command == "next":
            position = min(video_length, position + 10)

        # 중간 오프닝 체크
        position = check_and_skip_opening(position, opening_start, opening_end)

    return seconds_to_time(position)

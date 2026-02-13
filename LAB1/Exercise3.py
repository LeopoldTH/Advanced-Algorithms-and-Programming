def merge_intervals(intervals):
    if intervals == []:
        return []
    intervals.sort()
    result = []
    current_start = intervals[0][0]
    current_end = intervals[0][1]
    for i in range(1, len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]
        if start <= current_end:
            if end > current_end:
                current_end = end
        else:
            result.append([current_start, current_end])
            current_start = start
            current_end = end

    result.append([current_start, current_end])

    return result

print(merge_intervals([[1, 3], [2, 6], [15, 18], [8, 10]]))
print(merge_intervals([[1, 4], [4, 5]]))
print(merge_intervals([[1, 4], [0, 4]]))
print(merge_intervals([]))

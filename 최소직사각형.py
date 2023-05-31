def solution(sizes):
    widths = []
    heights = []

    # 가장 긴 부분으로 명함을 모두 통일하여 눕힘
    for size in sizes:
        widths.append(max(size))
        heights.append(min(size))
    
    return max(widths) * max(heights)

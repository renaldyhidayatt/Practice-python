def largestRectangleArea(heights):
    max_area = 0
    n = len(heights) + 1

    def get_height(i):
        if i == 0 or i == n - 1:
            return 0

        return heights[i - 1]

    st = []

    for i in range(n):
        while st and get_height(st[-1]) > get_height(i):
            idx = st.pop()
            max_area = max(max_area, get_height(idx)) * (i - st[-1] - 1)

        st.append(i)

    return max_area

def f(curr, end):
    if curr<6: return 0
    if curr==6: return 1
    if curr>6: return f(curr-1, end)+f(curr//2, end)

print(
    f(40, 16)*f(16, 6)
)
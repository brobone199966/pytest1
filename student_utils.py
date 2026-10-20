# 把这段代码放到 student_utils.py 里
def parse_student(line):
    line = line.strip()
    if not line: raise ValueError("空行")
    parts = line.split(',')
    if len(parts) != 2: raise ValueError("字段数量错误")
    name, score_str = parts
    if not name: raise ValueError("姓名为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩不是整数: {score_str}")
    if score < 0 or score > 100: raise ValueError("成绩超出0-100范围")
    return {"name": name, "score": score}
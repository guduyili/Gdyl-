
import json
from collections import Counter
from typing import Dict, Tuple


def count_field_distribution(file_path: str, field_name: str) -> Tuple[Dict, int]:
    """
    读取JSON文件，统计指定字段的分布
    :param file_path: JSON文件路径
    :param field_name: 待统计的字段名
    :return: 字段分布字典, 有效数据总数
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"文件 {file_path} 不存在")
    except json.JSONDecodeError:
        raise ValueError(f"文件 {file_path} 不是合法的JSON格式")

    if not isinstance(data, list):
        raise ValueError("JSON文件顶层需为数组格式")

    # 提取 label 字段，过滤字段不存在的样本
    field_values = []
    for item in data:
        if field_name in item:
            field_values.append(item[field_name])

    # 统计字段分布
    field_distribution = Counter(field_values)
    return field_distribution, len(field_values)

if __name__ == "__main__":
    file_path = "data.json"
    target_field = "label"
    
    dist, total = count_field_distribution(file_path, target_field)
    
    print(f"有效样本总数：{total}")
    print(f"{target_field} 字段分布：")
    for value, count in sorted(dist.items(), key=lambda x: x[1], reverse=True):
        ratio = count / total * 100
        print(f"  {value}: {count} 条，占比 {ratio:.2f}%")
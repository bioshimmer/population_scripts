# -*- coding: UTF-8 -*-
from Bio import Phylo

# 读取进化树文件（假设是Newick格式）
tree = Phylo.read("tree.newick", "newick")

# 定义名称替换的字典
name_mapping = {
    "JM2023080101-2A": "CFC64-1A",
    "JM2023080101-3A": "CFC64-2A",
    "JM2023080101-4A": "CFC64-3A",
    "LiuJQ-G-03-1A": "CFC64-4A",
}

# 反转字典，将右边的名称映射到左边
reversed_mapping = {v: k for k, v in name_mapping.items()}

# 遍历叶节点并替换名称
for leaf in tree.get_terminals():
    if leaf.name in name_mapping:
        leaf.name = name_mapping[leaf.name]  # 将左边的名称换成右边的
    elif leaf.name in reversed_mapping:
        leaf.name = reversed_mapping[leaf.name]  # 将右边的名称换成左边的

# 保存修改后的进化树
Phylo.write(tree, "updated_tree.newick", "newick")

print("进化树叶节点名称已更新并保存为 updated_tree.newick")
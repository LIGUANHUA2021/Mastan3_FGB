from collections import defaultdict

split_dict = defaultdict(list)

dictionary = {1: 1, 2: 2, 3: 1, 4: 2, 5: 3}
# 将键值对的值添加到新字典中对应值的列表中
for key, value in dictionary.items():
    split_dict[value].append(key)

result = []

# 遍历新字典中的每个键值对
for value_list in split_dict.values():
    # 判断列表的长度
    if len(value_list) > 0:
        # 如果列表长度大于1，说明有多个键对应相同的值，可以进行拆分
        sub_dict = {}
        for key in value_list:
            sub_dict[key] = dictionary[key]
        result.append(sub_dict)
Fiber_Mat = sorted(result, key=lambda x: next(iter(x.values())))

values = [[value for value in sub_dict.values()] for sub_dict in Fiber_Mat]
Grad_Group = [[key for key in sub_dict.keys()] for sub_dict in Fiber_Mat]
Groups =  [row[0] for row in values]
print(Fiber_Mat)
print(Grad_Group)
print(Groups)
Group_maxminCoor = {}
Group_maxminCoor[Groups[1]] = [1,2]
print(Group_maxminCoor)

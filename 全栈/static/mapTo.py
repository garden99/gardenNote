import json

def read_json_file(input_filename):
    """从JSON文件中读取数据"""
    with open(input_filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json_file(output_filename, data):
    """将数据写入到JSON文件中"""
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def convert_data(data):
    """转换数据结构"""
    tree_dict = {}

    # 构建字典结构
    for item in data:
        tree_dict[item['treeID']] = {
            'value': item['treeID'],
            'label': item['name'],
            'treeName': item['treeName'],
            'parent': item['parent'],
            'children': []
        }

    # 连接父子关系
    for item in data:
        parent_id = item['parent']
        if parent_id is not None:
            tree_dict[parent_id]['children'].append(tree_dict[item['treeID']])

    # 构建最终的树形结构
    def build_tree(node):
        if node['children']:
            node['children'] = sorted(node['children'], key=lambda x: x['treeName'])
            for child in node['children']:
                build_tree(child)

    root_node = tree_dict['1']
    build_tree(root_node)

    return [root_node]

def main():
    # 源文件名和目标文件名
    input_filename = './map.json'
    output_filename = './newMap.json'

    # 读取原始数据
    data = read_json_file(input_filename)

    # 转换数据
    converted_data = convert_data(data)

    # 写入转换后的数据到新文件
    write_json_file(output_filename, converted_data)

    print(f"Data has been processed and saved to '{output_filename}'.")

if __name__ == '__main__':
    main()
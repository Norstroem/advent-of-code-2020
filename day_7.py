

def get_content(contents):
    new_contents = []
    for content in contents:
        if content == 'no other bags':
            new_contents.append(content)
        else:
            content = content.replace('bags', '').replace('bag', '').strip()[2:]
            new_contents.append(content)
    return new_contents


def get_content2(contents):
    new_contents = []
    for content in contents:
        if content == 'no other bags':
            new_contents.append(content)
        else:
            content = content.strip()
            new_contents.append(content)
    return new_contents


def get_bag_index(bags, desired_bag):
    for i, bag in enumerate(bags):
        if bag == desired_bag:
            return i


if __name__ == '__main__':
    with open('inputs/day_7.txt', 'r') as file:
        lines = file.readlines()
    lines = map(str.strip, lines)
    lines = list(map(lambda x: x.split('contain'), lines))
    bags = list(map(lambda x: x[0].replace(' bags', '').strip(), lines))
    contents_list = list(map(lambda x: x[1].strip(' .').split(','), lines))

    for i, contents in enumerate(contents_list):
        contents_list[i] = get_content(contents)
    print(contents_list)

    for j in range(0, 10):
        made_change = False
        for i, contents in enumerate(contents_list):
            contents_list[i] = get_content2(contents)
            new_contents = []
            for content in contents:
                if content == 'shiny gold':
                    new_contents.append('shiny gold')
                elif content == 'no other bags':
                    pass
                else:
                    made_change = True
                    for content2 in contents_list[get_bag_index(bags, content)]:
                        new_contents.append(content2)
            contents_list[i] = new_contents
        if not made_change:
            print(j)
            break

    unique_contents_list = list(map(lambda x: list(set(x)), contents_list))

    count = 0
    for content in unique_contents_list:
        if content == ['shiny gold']:
            count += 1
    print(count)

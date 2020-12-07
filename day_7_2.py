

def get_content(contents):
    new_contents = []
    for content in contents:
        if content == 'no other bags':
            count = 1
            new_contents.append((count, content))
        else:
            content = content.replace('bags', '').replace('bag', '').strip()
            count = int(content[0])
            content = content[2:]
            new_contents.append((count, content))
            new_contents.append((1, 'no other bags'))
    return new_contents


def get_content2(contents):
    new_contents = []
    for count, content in contents:
        new_contents.append((count, content))
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

    for j in range(0, 10):
        made_change = False
        for i, contents in enumerate(contents_list):
            contents_list[i] = get_content2(contents)
            new_contents = []
            for (count, content) in contents:
                if content == 'no other bags':
                    new_contents.append((count, content))
                else:
                    made_change = True
                    for content2 in contents_list[get_bag_index(bags, content)]:
                        content2_count, content2_content = content2
                        #new_contents.append((count, 'no other bags'))
                        new_contents.append((int(count*content2_count), content2_content))
            if i == 0:
                pass
                #print(new_contents)
            contents_list[i] = new_contents
        if not made_change:
            print(j)
            break

    shiny_index = None
    for i, bag in enumerate(bags):
        if bag == 'shiny gold':
            shiny_index = i

    for i, contents in enumerate(contents_list):
        number_of_bags = 0
        for count, content in contents:
            number_of_bags += count

        if i == shiny_index:
            print(i, number_of_bags-1)



# 0
# 2
# 6
#
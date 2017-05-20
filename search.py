from pyquery import PyQuery as pq


# ciyu_list = [
#     '窄窄', '踏踏', '踏损', '踏逐', '踏践', '踏营', '碎碎', '碎职', '碎催', '碎乳', '织罗', '织素',
#     '纱纱', '纱罗', '乞援', '乞遗', '著述', '愁愁', '愁促', '愁损', '愁恨', '愁端', '愁泣', '愁扰',
#     '询审', '陶陶', '陶醉', '陶纹', '陶均', '陶隐', '陶范', '陶染', '陶植', '陶蒸', '陶贯', '陶炼',
#     '醉狂', '醉魂', '企咏', '权威', '权竖', '权摄', '权宗', '权凶', '权宜', '颠颠', '颠齿', '颠饮',
#     '颠陷', '颠素', '颠狂', '势威', '势援', '势素', '凭凭', '凭社', '职权', '职势', '职职', '职素',
#     '呈询', '呈递', '呈案', '呈控', '屈屈', '屈威', '屈迹', '屈乏', '屈陷', '屈染', '屈驾', '攻权',
#     '攻势', '攻逐', '攻社', '攻陷', '撤职', '撤案', '撤营', '威权', '威势', '威禁', '威摄', '威泽',
#     '威武', '威凤', '衰衰', '衰促', '衰齿', '衰旺', '衰递', '衰损', '衰渐', '衰征', '衰莫', '衰乏',
#     '衰歇', '滔滔', '滔漫', '滔腾', '旋旋', '旋律', '旋返', '旋驾', '纹章', '弦胶', '弦诵', '纤碎',
#     '纤纤', '纤介', '纤隐', '纤旨', '纤维', '纤罗', '催促', '催眠', '催征', '催乳', '促弦', '促促',
#     '促恰', '促驾', '披披', '披昌', '披宣', '披拣', '披述', '披款', '披诵', '娇娇', '娇惯', '恰恰',
#     '恰莫', '恰合', '齿乞', '齿齿', '齿介', '齿痕', '齿迹', '齿叙', '柴营', '杏浆', '杏膏', '焦碎',
#     '焦愁', '焦衰', '焦焦', '焦躁', '焦魂', '躁脱', '躁狂', '躁欲', '躁扰', '禁职', '禁律', '禁营',
#     '禁庭', '禁欲', '茂齿', '茂茂', '茂范', '旺茂', '昌披', '昌茂', '昌旺', '昌昌', '昌辰', '昌符',
#     '昌繁', '昌诵', '昌庭', '昌狂', '咏赞', '赠恨', '赠遗', '赠枕', '宣陶', '宣威', '宣宣', '宣饮',
#     '宣赞', '宣述', '宣慰', '宣旨', '宣旬', '宣抚', '宣源', '宣章', '宣武', '宣腾', '眨眨', '眨摩',
#     '饮浆', '饮恨', '饮贫', '饮宗', '饮章', '饮储', '饮蒸', '饮泽', '饮徒', '饮咽', '饮泣', '浆汁',
#     '递呈', '递衰', '递递', '递述', '陆陆', '陆营', '陆盐', '陆泽', '托势', '托托', '托迹', '托援',
#     '托逃', '托植', '托嘱', '帆颠', '帆势', '辰寸', '辰驾', '均权', '均势', '裹合', '裹蒸', '胶胶',
#     '胶合', '胶扰', '栽植', '拣择', '磨旋', '磨磨', '磨损', '磨罗', '磨炼', '介介', '介绍', '绍述',
#     '肤躁', '肤敏', '肤合', '肤寸', '摩托', '摩抚', '摩罗', '律均', '律律', '律宗', '损撤', '损彻',
#     '逐势', '逐旋', '逐逐', '逐渐', '逐迹', '逐贫', '逐脱', '渐磨', '渐摩', '渐渐', '渐悟', '渐营',
#     '渐染', '渐泽', '渐稀', '痕痕', '痕迹', '迹痕', '征衫', '征询', '征催', '征帆', '征逐', '征迹',
#     '征摄', '征营', '征符', '征聚', '征驾', '征徒', '征搜', '隐介', '隐迹', '隐隐', '隐蔽', '隐燃',
#     '隐章', '隐逃', '隐符', '隐武', '蔽茂', '蔽隐', '侦罗', '莫莫', '乏乏', '滥职', '滥饮', '滥浆',
#     '滥漫', '赞咏', '赞赞', '赞述', '赞彻', '赞诵', '审权', '审势', '审律', '审案', '审择', '审端',
#     '审合', '刘陆', '恨恨', '案摩', '案抚', '案陷', '套衫', '套套', '套叙', '遵职', '遵途', '遵禁',
#     '遵陆', '遵迹', '遵述', '遵旨', '挨磨', '挨脱', '摄职', '摄威', '摄衰', '摄摄', '摄悟', '摄魂',
#     '述职', '述宣', '述律', '述赞', '述遵', '述叙', '援案', '社宗', '捐势', '捐职', '捐赠', '捐款',
#     '款纹', '款逐', '款案', '款款', '款歇', '款叙', '返攻', '返迹', '返盐', '返驾', '返朴', '返素',
#     '返魂', '贫乞', '贫乏', '贫宗', '贫素', '魔浆', '毅武', '慰抚', '尚齿', '尚章', '尚武', '恢宣',
#     '恢恢', '恢扩', '恢漫', '遗威', '遗弦', '遗焦', '遗禁', '遗咏', '遗赠', '遗饮', '遗绍', '遗痕',
#     '遗迹', '遗隐', '遗恨', '遗案', '遗捐', '遗遗', '遗宗', '遗旨', '遗章', '遗脱', '遗端', '遗储',
#     '遗范', '遗植', '遗泽', '遗宜', '遗碍', '遗武', '遗置', '遗朴', '遗徒', '遗魂', '遗泣', '遗叙',
#     '遗嘱', '签呈', '签合', '昔款', '昔昔', '践踏', '践迹', '宗职', '宗援', '宗社', '宗尚', '宗旨',
#     '宗贯', '宗徒', '旨蓄', '旨符', '旬呈', '旬宣', '旬旬', '抚弦', '抚摩', '抚迹', '抚征', '抚案',
#     '抚慰', '抚控', '源陆', '源源', '章旨', '章章', '章彻', '章武', '章狂', '凶权', '凶衰', '凶竖',
#     '凶凶', '凶狂', '凶欲', '凶徒', '脱赠', '脱胶', '脱迹', '脱套', '脱捐', '脱贫', '脱遗', '脱脱',
#     '脱逃', '脱敏', '脱营', '脱贯', '脱素', '脱脂', '逃隐', '逃返', '逃脱', '逃逃', '逗彻', '端衰',
#     '端茂', '端渐', '端审', '端端', '端敏', '端合', '措措', '措置', '悟宗', '悟敏', '悟彻', '控弦',
#     '控摄', '控款', '控驾', '控咽', '漠漠', '漠置', '敏茂', '敏悟', '陷脱', '储款', '储端', '储蓄',
#     '储聚', '储驾', '蓄储', '蓄聚', '营织', '营职', '营柴', '营援', '营尚', '营脱', '营陷', '营营',
#     '营合', '营殖', '营植', '营聚', '营置', '营欲', '营魂', '维摩', '枕纹', '枕痕', '枕套', '撒娇',
#     '撒脱', '撒撒', '撒漫', '撒盐', '撒旦', '符禁', '符征', '符旨', '符合', '合著', '合权', '合职',
#     '合律', '合莫', '合营', '合符', '合合', '合聚', '合宜', '甚莫', '染滥', '染尚', '染素', '寸介',
#     '寸旬', '寸寸', '倍诵', '倍欲', '繁碎', '繁弦', '繁促', '繁茂', '繁昌', '繁殖', '繁聚', '繁漫',
#     '繁泽', '繁滋', '繁扰', '殖殖', '植援', '植植', '蒸陶', '蒸裹', '蒸蒸', '蒸腾', '蒸徒', '浮躁',
#     '浮迹', '浮征', '浮滥', '浮套', '浮签', '浮蒸', '浮浮', '浮漫', '浮腾', '聚焦', '聚饮', '聚蓄',
#     '聚合', '冈岭', '漫漫', '漫滋', '漫狂', '盐汁', '盐禁', '盐裹', '盐宗', '盐徒', '泽泽', '彻案',
#     '彻贫', '彻悟', '彻旦', '罗织', '罗衫', '罗纹', '罗禁', '罗合', '罗罗', '罗搜', '贯辰', '贯蔽',
#     '贯彻', '贯叙', '武职', '武威', '武毅', '武敏', '武罗', '武旦', '奴奴', '置递', '置社', '置措',
#     '乃昔', '炼焦', '炼贫', '炼魔', '炼盐', '炼钢', '炼乳', '斜纹', '斜签', '诵弦', '诵咏', '诵述',
#     '腾踏', '腾茂', '腾逐', '腾迹', '腾践', '腾章', '腾驾', '驾盐', '陡斜', '陡搜', '朴茂', '朴素',
#     '素纱', '素威', '素弦', '素裹', '素律', '素隐', '素尚', '素昔', '素章', '素端', '素蓄', '素罗',
#     '素朴', '滋茂', '滋旨', '滋繁', '滋殖', '滋植', '滋漫', '滋滋', '滋乳', '滋膏', '滋扰', '庭审',
#     '狂颠', '狂竖', '狂躁', '狂饮', '狂蔽', '狂章', '狂奴', '狂狂', '狂徒', '歇乏', '歇案', '歇歇',
#     '赢储', '拥蔽', '拥社', '拥聚', '恒齿', '恒蔽', '旦莫', '旦昔', '旦旦', '恐恐', '徒践', '徒维',
#     '徒奴', '魂痕', '魂庭', '魂旦', '魂魂', '乳竖', '乳齿', '乳汁', '乳胶', '乳脂', '乳膏', '凤职',
#     '凤律', '凤迹', '凤章', '凤枕', '凤岭', '凤罗', '凤驾', '凤庭', '凤膏', '咽咽', '咽泣', '脂胶',
#     '脂泽', '脂驾', '脂膏', '膏泽', '膏乳', '敲磨', '敲朴', '叙齿', '叙述', '蚊聚', '扰毅', '扰扰',
#     '稀碎', '稀稀', '叮叮', '叮嘱', '嘱托', '嘱赞', '搜择', '搜遗', '搜罗', '搜搜'
# ]

ciyu_list = ['完璧归赵', '围魏救赵', '退避三舍', '毛遂自荐', '负荆请罪', '纸上谈兵', '一鼓作气', '千金买骨',
             '讳疾忌医', '卧薪尝胆', '杀妻求将', '惊弓之鸟', '高山流水', '围魏救赵']

def search(word):
    search_url = 'http://hanyu.baidu.com/s?wd={}'.format(word)
    search_html = pq(search_url)
    pinyin = search_html('#pinyin > h2:nth-child(1) > span:nth-child(2) > b:nth-child(1)') \
        .text().encode('latin1').decode('utf8').strip()
    try:
        jieshi = search_html('#basicmean-wrapper p').text().encode('latin1').decode('utf8').strip()
    except:
        jieshi = search_html('#basicmean-wrapper p').text().strip()
    try:
        jinyici = search_html('#synonym div').text().encode('latin1').decode('utf8').strip()
    except:
        jinyici = search_html('#synonym div').text().strip()
    try:
        fanyici = search_html('#antonym div').text().encode('latin1').decode('utf8').strip()
    except:
        fanyici = search_html('#antonym div').text().strip()
    try:
        diangu = search_html('#story-wrapper > div:nth-child(2)').text().encode('latin1').decode('utf8').strip()
    except:
        diangu = search_html('#story-wrapper > div:nth-child(2)').text().strip()

    return {
        '拼音': pinyin,
        '释义': jieshi,
        '近义词': jinyici,
        '反义词': fanyici,
        '典故': diangu
    }

for index, word in enumerate(ciyu_list):
    with open('/home/xiaozi/文档/成语.txt', 'a') as f:
        result = str(index+1) + ':' + word + '————' + '\n' + \
                 '拼音：' + search(word)['拼音'] + '\n' + \
                 '释义：' + search(word)['释义'] + '\n' + \
                 '近义词：' + search(word)['近义词'] + '\n' + \
                 '反义词：' + search(word)['反义词'] + '\n' + \
                 '典故：' + search(word)['典故'] + '\n'
        print(result)
        f.write(result)


#
# with open('/home/xiaozi/文档/双生词.txt', 'r') as f:
#     words_list = list(f.read()[1:-2].split(',').split("'"))
# for word in words_list:
#     with open('/home/xiaozi/文档/双生词释义.txt', 'a') as f:
#         print(word, search(word))
#         f.write(word, search(word))
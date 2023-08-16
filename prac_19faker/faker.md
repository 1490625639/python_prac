https://blog.csdn.net/ping233/article/details/121115265
# 关于faker库的使用

## 官方文档

https://faker.readthedocs.io/en/master/

## 常见参数

### 生成随机数
要生成中文，只需要在 Faker 类的第一个参数传入对应的语言代号即可
https://blog.csdn.net/ping233/article/details/121115265
from faker import Faker

faker = Faker('zh-CN')

def random_name():
    return faker.name()
def random_address():
    return faker.address()
def random_text():
    return faker.text()
def random_email():
    return faker.email()
def random_phone_number():
    return faker.phone_number()

### 生成地理信息类
city_suffix()：市，县

country()：国家

country_code()：国家编码

district()：区

geo_coordinate()：地理坐标

latitude()：地理坐标(纬度)

longitude()：地理坐标(经度)

postcode()：邮编

province()：省份 (zh_TW没有此方法)

address()：详细地址

street_address()：街道地址

street_name()：街道名

street_suffix()：街、路




### 基础信息类
ssn()：生成身份证号

bs()：随机公司服务名

company()：随机公司名（长）

company_prefix()：随机公司名（短）

company_suffix()：公司性质

credit_card_expire()：随机信用卡到期日

credit_card_full()：生成完整信用卡信息

credit_card_number()：信用卡号

credit_card_provider()：信用卡类型

credit_card_security_code()：信用卡安全码

job()：随机职位

first_name()：

first_name_female()：女性名

first_name_male()：男性名

first_romanized_name()：罗马名

last_name()：

last_name_female()：女姓

last_name_male()：男姓

last_romanized_name()：

name()：随机生成全名

name_female()：男性全名

name_male()：女性全名

romanized_name()：罗马名

msisdn()：移动台国际用户识别码，即移动用户的ISDN号码

phone_number()：随机生成手机号

phonenumber_prefix()：随机生成手机号段


### 个人账户信息类
ascii_company_email()：随机ASCII公司邮箱名

ascii_email()：随机ASCII邮箱

ascii_free_email()：

ascii_safe_email()：

company_email()：

email()：

free_email()：

free_email_domain()：

safe_email()：安全邮箱





### 网络基础信息类
domain_name()：生成域名

domain_word()：域词(即，不包含后缀)

ipv4()：随机IP4地址

ipv6()：随机IP6地址

mac_address()：随机MAC地址

tld()：网址域名后缀(.com,.net.cn,等等，不包括.)

uri()：随机URI地址

uri_extension()：网址文件后缀

uri_page()：网址文件（不包含后缀）

uri_path()：网址文件路径（不包含文件名）

url()：随机URL地址

user_name()：随机用户名

image_url()：随机URL地址




### 浏览器信息类
chrome()：随机生成Chrome的浏览器user_agent信息

firefox()：随机生成FireFox的浏览器user_agent信息

internet_explorer()：随机生成IE的浏览器user_agent信息

opera()：随机生成Opera的浏览器user_agent信息

safari()：随机生成Safari的浏览器user_agent信息

linux_platform_token()：随机Linux信息

user_agent()：随机user_agent信息




### 文件信息类
file_extension()：随机文件扩展名

file_name()：随机文件名（包含扩展名，不包含路径）

file_path()：随机文件路径（包含文件名，扩展名）

mime_type()：随机mime Type




### 数字信息类
numerify()：三位随机数字

random_digit()：0~9随机数

random_digit_not_null()：1~9的随机数

random_int()：随机数字，默认0~9999，可以通过设置min,max来设置

random_number()：随机数字，参数digits设置生成的数字位数

pyfloat()：left_digits=5 #生成的整数位数,

                  right_digits=2 #生成的小数位数,
    
                  positive=True #是否只有正数

pyint()：随机Int数字（参考random_int()参数）

pydecimal()：随机Decimal数字（参考pyfloat参数





### 文本加密类
pystr()：随机字符串

random_element()：随机字母

random_letter()：随机字母

paragraph()：随机生成一个段落

paragraphs()：随机生成多个段落，通过参数nb来控制段落数，返回数组

sentence()：随机生成一句话

sentences()：随机生成多句话，与段落类似

text()：随机生成一篇文章（不要幻想着人工智能了，至今没完全看懂一句话是什么意思）

word()：随机生成词语

words()：随机生成多个词语，用法与段落，句子，类似

binary()：随机生成二进制编码

boolean()：True/False

language_code()：随机生成两位语言编码

locale()：随机生成语言/国际 信息

md5()：随机生成MD5

null_boolean()：NULL/True/False

password()：随机生成密码,可选参数：length：密码长度；special_chars：是否能使用特殊字符；digits：是否包含数字；upper_case：是否包含大写字母；lower_case：是否包含小写字母

sha1()：随机SHA1

sha256()：随机SHA256

uuid4()：随机UUID




### 时间信息类
am_pm()：AM/PM

century()：随机世纪

date()：随机日期

date_between()：随机生成指定范围内日期，参数：start_date，end_date取值：具体日期或者today,-30d,-30y类似

date_between_dates()：随机生成指定范围内日期，用法同上

date_object()：随机生产从1970-1-1到指定日期的随机日期。

date_this_month()：

date_this_year()：

date_time()：随机生成指定时间（1970年1月1日至今）

date_time_ad()：生成公元1年到现在的随机时间

date_time_between()：用法同dates

future_date()：未来日期

future_datetime()：未来时间

month()：随机月份

month_name()：随机月份（英文）

past_date()：随机生成已经过去的日期

past_datetime()：随机生成已经过去的时间

time()：随机24小时时间

timedelta()：随机获取时间差

time_object()：随机24小时时间，time对象

time_series()：随机TimeSeries对象

timezone()：随机时区

unix_time()：随机Unix时间

year()：随机年份



### 集合信息类
profile()：随机生成档案信息

simple_profile()：随机生成简单档案信息



### 地区编号
    
    | 国家/地区          | 语言代码 | 国家/地区          | 语言代码 |
    | ------------------ | -------- | ------------------ | -------- |
    | 简体中文(中国)     | zh-cn    | 繁体中文(台湾地区) | zh-tw    |
    | 繁体中文(香港)     | zh-hk    | 英语(香港)         | en-hk    |
    | 英语(美国)         | en-us    | 英语(英国)         | en-gb    |
    | 英语(全球)         | en-ww    | 英语(加拿大)       | en-ca    |
    | 英语(澳大利亚)     | en-au    | 英语(爱尔兰)       | en-ie    |
    | 英语(芬兰)         | en-fi    | 芬兰语(芬兰)       | fi-fi    |
    | 英语(丹麦)         | en-dk    | 丹麦语(丹麦)       | da-dk    |
    | 英语(以色列)       | en-il    | 希伯来语(以色列)   | he-il    |
    | 英语(南非)         | en-za    | 英语(印度)         | en-in    |
    | 英语(挪威)         | en-no    | 英语(新加坡)       | en-sg    |
    | 英语(新西兰)       | en-nz    | 英语(印度尼西亚)   | en-id    |
    | 英语(菲律宾)       | en-ph    | 英语(泰国)         | en-th    |
    | 英语(马来西亚)     | en-my    | 英语(阿拉伯)       | en-xa    |
    | 韩文(韩国)         | ko-kr    | 日语(日本)         | ja-jp    |
    | 荷兰语(荷兰)       | nl-nl    | 荷兰语(比利时)     | nl-be    |
    | 葡萄牙语(葡萄牙)   | pt-pt    | 葡萄牙语(巴西)     | pt-br    |
    | 法语(法国)         | fr-fr    | 法语(卢森堡)       | fr-lu    |
    | 法语(瑞士)         | fr-ch    | 法语(比利时)       | fr-be    |
    | 法语(加拿大)       | fr-ca    | 西班牙语(拉丁美洲) | es-la    |
    | 西班牙语(西班牙)   | es-es    | 西班牙语(阿根廷)   | es-ar    |
    | 西班牙语(美国)     | es-us    | 西班牙语(墨西哥)   | es-mx    |
    | 西班牙语(哥伦比亚) | es-co    | 西班牙语(波多黎各) | es-pr    |
    | 德语(德国)         | de-de    | 德语(奥地利)       | de-at    |
    | 德语(瑞士)         | de-ch    | 俄语(俄罗斯)       | ru-ru    |
    | 意大利语(意大利)   | it-it    | 希腊语(希腊)       | el-gr    |
    | 挪威语(挪威)       | no-no    | 匈牙利语(匈牙利)   | hu-hu    |
    | 土耳其语(土耳其)   | tr-tr    | 捷克语(捷克共和国) | cs-cz    |
    | 斯洛文尼亚语       | sl-sl    | 波兰语(波兰)       | pl-pl    |
    | 瑞典语(瑞典)       | sv-se    | 西班牙语(智利)     |          |
    |                |      |                |      |###

## 
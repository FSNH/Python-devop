def save_detail():
    """字符处理"""
    with open('hongdun.csv', 'r',encoding='utf-8')as f:
        details = f.read()
        detail = details.replace(',', '').strip()
        with open('1.csv','a', encoding='utf-8')as f:
            f.write(detail)
if __name__ == '__main__':
    save_detail()